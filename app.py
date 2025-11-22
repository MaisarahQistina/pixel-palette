from flask import Flask, request, jsonify, render_template
import numpy as np
import cv2
from sklearn.cluster import KMeans
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def hex_from_rgb(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

@app.route('/extract_palette', methods=['POST'])
def extract_palette():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    file = request.files['image']
    in_memory_file = io.BytesIO()
    file.save(in_memory_file)
    in_memory_file.seek(0)

    # Read with PIL and convert to OpenCV
    pil_image = Image.open(in_memory_file).convert('RGB')
    img = np.array(pil_image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Convert to LAB
    lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    pixels = lab_img.reshape(-1, 3)

    # KMeans
    k = int(request.form.get('k', 4))
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(pixels)
    lab_centers = kmeans.cluster_centers_.astype(np.uint8)

    # Convert back to RGB for frontend
    rgb_centers = cv2.cvtColor(lab_centers.reshape(1, -1, 3), cv2.COLOR_LAB2BGR).reshape(-1, 3)
    rgb_centers = rgb_centers[:, ::-1]
    hex_colors = [hex_from_rgb(tuple(c)) for c in rgb_centers]
    
    return jsonify({'palette': hex_colors})

if __name__ == '__main__':
    app.run(debug=True)
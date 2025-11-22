# pixel-palette
PixelPalette is a web-based color palette extractor that extracts the main colors from any image. It generates a color strip with HEX codes based on how many colors specified and can be downloaded.

## How it works

1. Rasterize the Image

- When an image is uploaded, it is first converted to a raster format (if it isn’t already).
- This allows the program to access individual pixels and their RGB values.

2. Convert Colors to LAB Space

RGB values represent colors as combinations of Red, Green, and Blue, but this space is not perceptually uniform.

PixelPalette converts RGB to LAB color space:

L = lightness

A = green-red component

B = blue-yellow component

LAB is better for color clustering because distances in LAB correspond more closely to human perception of color differences.

3. Extract Main Colors Using KMeans

All pixels are treated as points in 3D LAB space.

KMeans clustering groups similar colors into k clusters (where k is the number of colors the user selects).

The centroid of each cluster represents the main color in that group.

4. Convert Back to RGB & Generate HEX Codes

After finding the cluster centroids in LAB space, they are converted back to RGB.

Each color is then converted to HEX format (#RRGGBB) for display and downloads.

5. Display Palette

The extracted colors are displayed as a strip of color blocks with HEX codes.

Users can download:

CSS classes for web use

PNG image with the colors and HEX codes

### References:
[1] https://www.youtube.com/watch?v=yI9IPU9JI5k
[2] https://informatika.stei.itb.ac.id/~rinaldi.munir/Citra/2023-2024/Makalah2023/Makalah-IF4073-Citra-2023%20%284%29.pdf
[3] https://medium.com/@ys3372/deconstructing-an-image-with-pixels-4c65c3a2268c
[4] https://opencv.org/blog/color-spaces-in-opencv/

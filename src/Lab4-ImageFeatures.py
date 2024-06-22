from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np


# image = Image.open(image_path)
# img_format = image.format
# img_size = image.size
# img_mode = image.mode
# print(f'Format: {img_format}, Size: {img_size}, Mode: {img_mode}')


image_path = '../assets/image/doge.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Select Edges
edges = cv2.Canny(image, threshold1=0, threshold2=50)

plt.imshow(edges, cmap='gray')
plt.title('Edge Image')
plt.show()

# Get Contrast
gray_arr = np.array(image)
print("Contrast : ", np.std(gray_arr))

# Get Textures
texture = cv2.Laplacian(image, cv2.CV_64F).var()
print("Texture : ", texture)

# Get KeyPoints
# Initialize the ORB detector
orb = cv2.ORB_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = orb.detectAndCompute(image, None)   # detectAndCompute(image, mask=None, descriptor=None)

# Draw keypoints on the image
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the image with keypoints
plt.imshow(image_with_keypoints, cmap='gray')
plt.title('Image with Keypoints')
plt.axis('off')
plt.show()

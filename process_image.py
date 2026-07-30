import cv2
import numpy as np
import os

# Create a sample gradient image (256x256)
size = (256, 256)
gradient = np.tile(np.arange(0, 256, dtype=np.uint8), (256, 1))
sample_img = cv2.merge([gradient, gradient, gradient])
# Save sample image using OpenCV
sample_path = os.path.join(os.getcwd(), "sample.jpg")
cv2.imwrite(sample_path, sample_img)
print(f"Sample image saved to {sample_path}")

# Load the image with OpenCV
img = cv2.imread(sample_path)
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (5,5), 0)
# Canny edge detection
edges = cv2.Canny(blur, 100, 200)
# Save edge image
edges_path = os.path.join(os.getcwd(), "edges.jpg")
cv2.imwrite(edges_path, edges)
print(f"Edge image saved to {edges_path}")

import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\yeshw\OneDrive\Documents\COMPUTER VISION\EXPERIMENTS\image.jpg")

if img is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(gray, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", gray)
    cv2.imshow("Dilated Image", dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
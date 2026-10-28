
import cv2
import numpy as np

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # Create a structuring element (kernel)
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    erosion = cv2.erode(
        binary, kernel, iterations=1
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Erosion Image", erosion)

    # Save the erosion output
    cv2.imwrite("erosion_output.jpg", erosion)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

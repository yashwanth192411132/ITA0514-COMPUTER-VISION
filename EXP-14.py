
import cv2
import numpy as np

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Get image dimensions
    rows, cols = img.shape[:2]

    # Define four points in the original image
    pts1 = np.float32([
        [50, 50],
        [cols - 50, 50],
        [50, rows - 50],
        [cols - 50, rows - 50]
    ])

    # Define corresponding destination points
    pts2 = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    # Calculate perspective transformation matrix
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply perspective transformation
    transformed = cv2.warpPerspective(img, M, (cols, rows))

    # Display original and transformed images
    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformed Image", transformed)

    # Save the transformed image
    cv2.imwrite("perspective_transformed.jpg", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


import cv2

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Rotate image 270 degrees clockwise
    rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display original and rotated images
    cv2.imshow("Original Image", img)
    cv2.imshow("270 Degree Clockwise Rotated Image", rotated)

    # Save the rotated image
    cv2.imwrite("rotated_270_image.jpg", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

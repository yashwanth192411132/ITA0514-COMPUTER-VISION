
import cv2

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Get original image dimensions
    height, width = img.shape[:2]
    print("Original Size:", width, "x", height)

    # Resize to a bigger size (2x)
    bigger = cv2.resize(
        img, None, fx=2, fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    # Resize to a smaller size (0.5x)
    smaller = cv2.resize(
        img, None, fx=0.5, fy=0.5,
        interpolation=cv2.INTER_AREA
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    # Save resized images
    cv2.imwrite("bigger_image.jpg", bigger)
    cv2.imwrite("smaller_image.jpg", smaller)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

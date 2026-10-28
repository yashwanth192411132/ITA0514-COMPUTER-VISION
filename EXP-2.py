import cv2

# Read image
img = cv2.imread(r"C:\Users\yeshw\OneDrive\Documents\COMPUTER VISION\EXPERIMENTS\image.jpg")

if img is None:
    print("Image not found!")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
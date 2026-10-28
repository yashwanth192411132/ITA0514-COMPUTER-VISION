import cv2

# Read image
img = cv2.imread(r"C:\Users\yeshw\OneDrive\Documents\COMPUTER VISION\EXPERIMENTS\image.jpg")

if img is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Display images
    cv2.imshow("Original Image", gray)
    cv2.imshow("Histogram Equalized Image", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save equalized image
    cv2.imwrite("equalized_image.jpg", equalized)
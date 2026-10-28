
import cv2

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Select Region of Interest (ROI)
    # Format: image[y1:y2, x1:x2]
    roi = img[50:200, 50:200]

    # Crop the selected ROI
    cropped = roi.copy()

    # Copy the original image
    result = img.copy()

    # Paste the ROI at a new location
    result[250:400, 250:400] = roi

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped ROI", cropped)
    cv2.imshow("Image with Pasted ROI", result)

    # Save output images
    cv2.imwrite("cropped_roi.jpg", cropped)
    cv2.imwrite("pasted_roi.jpg", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

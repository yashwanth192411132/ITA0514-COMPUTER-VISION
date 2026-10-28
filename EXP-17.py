
import cv2

# Read the original image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Copy the original image
    watermarked = img.copy()

    # Define watermark text
    text = "WATERMARK"

    # Set font properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)  # White color (BGR)
    thickness = 2

    # Get image dimensions
    height, width = img.shape[:2]

    # Position watermark at bottom-right corner
    text_size = cv2.getTextSize(
        text, font, font_scale, thickness
    )[0]

    x = width - text_size[0] - 20
    y = height - 20

    # Insert watermark into the image
    cv2.putText(
        watermarked,
        text,
        (x, y),
        font,
        font_scale,
        color,
        thickness,
        cv2.LINE_AA
    )

    # Display original and watermarked images
    cv2.imshow("Original Image", img)
    cv2.imshow("Watermarked Image", watermarked)

    # Save the watermarked image
    cv2.imwrite("watermarked_image.jpg", watermarked)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    # Read image
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found!")
        return

    # Display original image
    cv2.imshow("Original Image", img)

    # Calculate histogram for each color channel
    colors = ('b', 'g', 'r')

    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call function
analyze_histogram(
    r"C:\Users\yeshw\OneDrive\Documents\COMPUTER VISION\EXPERIMENTS\image.jpg"
)
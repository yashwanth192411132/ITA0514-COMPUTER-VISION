import cv2

# Read video
cap = cv2.VideoCapture(
    r"C:\Users\yeshw\OneDrive\Documents\COMPUTER VISION\EXPERIMENTS\video.mp4"
)

if not cap.isOpened():
    print("Video not found!")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Display slow motion
        cv2.imshow("Slow Motion", frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Reopen video for fast motion
    cap = cv2.VideoCapture(
        r"C:\Users\yeshw\OneDrive\Documents\COMPUTER VISION\EXPERIMENTS\video.mp4"
    )

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Display fast motion
        cv2.imshow("Fast Motion", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
# Experiment 7: Video processing: Slow Motion & Fast Motion
import cv2

cap = cv2.VideoCapture("assets/sample_video.mp4")

# Slow motion: Increase waitKey delay (e.g. waitKey(100) -> ~10 fps)
# Fast motion: Decrease waitKey delay (e.g. waitKey(5) -> ~200 fps) or skip frames

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video Player", frame)
    # Change delay to 80 for slow motion, 10 for fast motion
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

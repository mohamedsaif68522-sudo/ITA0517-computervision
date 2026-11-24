# Experiment 25: Recognize watch from image by Object Recognition
import cv2
import numpy as np

image = cv2.imread("assets/watch.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100,
                           param1=100, param2=50, minRadius=50, maxRadius=250)

output = image.copy()
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 3)
        cv2.rectangle(output, (i[0]-i[2]-10, i[1]-i[2]-10), (i[0]+i[2]+10, i[1]+i[2]+10), (255, 0, 0), 2)
        cv2.putText(output, "Recognized: Watch", (i[0]-i[2], i[1]-i[2]-20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

cv2.imshow("Detected Watch", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

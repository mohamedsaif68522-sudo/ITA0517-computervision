# Experiment 3: Show outline using Canny function
import cv2

image = cv2.imread("assets/building.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Canny Edge Detection with thresholds 100 and 200
edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Original", image)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

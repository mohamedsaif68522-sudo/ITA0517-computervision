# Experiment 9: Image scaling to bigger and smaller sizes
import cv2

image = cv2.imread("assets/scene.jpg")

# Scale smaller (0.5x)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Scale bigger (1.5x)
bigger = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Original", image)
cv2.imshow("Smaller (0.5x)", smaller)
cv2.imshow("Bigger (1.5x)", bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()

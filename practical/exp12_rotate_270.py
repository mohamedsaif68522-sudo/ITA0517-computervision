# Experiment 12: 270-degree clockwise rotation
import cv2

image = cv2.imread("assets/scene.jpg")
rot270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original", image)
cv2.imshow("270 Deg Clockwise", rot270)
cv2.waitKey(0)
cv2.destroyAllWindows()

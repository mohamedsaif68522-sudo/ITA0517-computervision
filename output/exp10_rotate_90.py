# Experiment 10: 90-degree clockwise rotation
import cv2

image = cv2.imread("assets/scene.jpg")
# cv2.ROTATE_90_CLOCKWISE rotates 90 degrees clockwise
rot90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original", image)
cv2.imshow("90 Deg Clockwise", rot90)
cv2.waitKey(0)
cv2.destroyAllWindows()

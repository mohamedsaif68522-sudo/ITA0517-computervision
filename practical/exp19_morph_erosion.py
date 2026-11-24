# Experiment 19: Erosion Morphological Operation
import cv2
import numpy as np

image = cv2.imread("assets/fruits.jpg")
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(image, kernel, iterations=3)

cv2.imshow("Original", image)
cv2.imshow("Erosion Morphological", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

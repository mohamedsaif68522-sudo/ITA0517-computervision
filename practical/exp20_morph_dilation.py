# Experiment 20: Dilation Morphological Operation
import cv2
import numpy as np

image = cv2.imread("assets/fruits.jpg")
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(image, kernel, iterations=3)

cv2.imshow("Original", image)
cv2.imshow("Dilation Morphological", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

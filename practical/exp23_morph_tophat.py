# Experiment 23: Top Hat Morphological Operation
import cv2
import numpy as np

image = cv2.imread("assets/building.jpg")
kernel = np.ones((15, 15), np.uint8)
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Original", image)
cv2.imshow("Top Hat", tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Experiment 24: Black Hat Morphological Operation
import cv2
import numpy as np

image = cv2.imread("assets/building.jpg")
kernel = np.ones((15, 15), np.uint8)
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original", image)
cv2.imshow("Black Hat", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()

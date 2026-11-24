# Experiment 21: Opening Morphological Operation (Noise removal)
import cv2
import numpy as np

image = cv2.imread("assets/fruits.jpg")
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.imshow("Original", image)
cv2.imshow("Opening Operation", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Experiment 6: Convert an Image to erode using Erode function
import cv2
import numpy as np

image = cv2.imread("assets/building.jpg")
kernel = np.ones((5, 5), np.uint8)
eroded_image = cv2.erode(image, kernel, iterations=2)

cv2.imshow("Original", image)
cv2.imshow("Eroded", eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

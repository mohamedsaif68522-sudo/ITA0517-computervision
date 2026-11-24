# Experiment 8: Dilate an Image using Dilate function
import cv2
import numpy as np

image = cv2.imread("assets/building.jpg")
kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(image, kernel, iterations=2)

cv2.imshow("Original", image)
cv2.imshow("Dilated", dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

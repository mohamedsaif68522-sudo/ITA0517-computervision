# Experiment 4: Implement Histogram Equalization and compare
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("assets/scene.jpg", cv2.IMREAD_GRAYSCALE)
equalized_image = cv2.equalizeHist(image)

cv2.imshow("Original Gray", image)
cv2.imshow("Histogram Equalized", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

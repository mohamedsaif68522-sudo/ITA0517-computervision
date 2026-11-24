# Experiment 16: Sobel Algorithm Filter
import cv2
import numpy as np

image = cv2.imread("assets/scene.jpg", cv2.IMREAD_GRAYSCALE)

# Sobel X and Sobel Y
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Combined Sobel magnitude
sobel_combined = cv2.magnitude(sobelx, sobely)
sobel_combined = np.uint8(np.clip(sobel_combined, 0, 255))

cv2.imshow("Original", image)
cv2.imshow("Sobel Combined", sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

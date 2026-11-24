# Experiment 15: Harris Corner Detection
import cv2
import numpy as np

image = cv2.imread("assets/building.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Harris corner detection parameters: blockSize=2, ksize=3, k=0.04
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate to mark corners clearly
dst = cv2.dilate(dst, None)

# Threshold for optimal corner display
corner_img = image.copy()
corner_img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow("Original", image)
cv2.imshow("Harris Corners", corner_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Experiment 13: Affine Transformation
import cv2
import numpy as np

image = cv2.imread("assets/scene.jpg")
rows, cols, ch = image.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)
affine_dst = cv2.warpAffine(image, M, (cols, rows))

cv2.imshow("Original", image)
cv2.imshow("Affine Transformed", affine_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

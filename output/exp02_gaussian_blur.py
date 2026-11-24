# Experiment 2: Convert an Image to Blur using Gaussian Blur
import cv2

image = cv2.imread("assets/scene.jpg")
# Applying Gaussian Blur with kernel size 15x15 and sigmaX = 0
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imshow("Original", image)
cv2.imshow("Gaussian Blurred", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

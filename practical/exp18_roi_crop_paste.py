# Experiment 18: Image cropping, copying and pasting (ROI)
import cv2

image = cv2.imread("assets/scene.jpg")

# Crop Region of Interest (e.g., face or center object)
roi = image[150:350, 180:380]

# Paste into another location
result = image.copy()
result[50:250, 20:220] = roi
cv2.rectangle(result, (20, 50), (220, 250), (0, 255, 0), 2) # outline pasted ROI

cv2.imshow("Cropped ROI", roi)
cv2.imshow("Copied and Pasted", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

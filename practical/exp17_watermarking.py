# Experiment 17: Watermarking Technique using OpenCV
import cv2

image = cv2.imread("assets/nature.jpg")
watermark = cv2.imread("assets/watermark.png")

# Resize watermark to 150x150
wm_resized = cv2.resize(watermark, (150, 150))
h, w, _ = wm_resized.shape
img_h, img_w, _ = image.shape

# Place watermark in bottom-right corner
top_y = img_h - h - 20
left_x = img_w - w - 20
roi = image[top_y:top_y+h, left_x:left_x+w]

# Blend ROI with watermark (alpha blending)
blended = cv2.addWeighted(roi, 0.6, wm_resized, 0.4, 0)
watermarked_image = image.copy()
watermarked_image[top_y:top_y+h, left_x:left_x+w] = blended

cv2.imshow("Watermarked Image", watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

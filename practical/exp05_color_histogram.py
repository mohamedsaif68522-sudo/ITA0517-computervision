# Experiment 5: Analyze histogram based on color levels using OpenCV
import cv2
import matplotlib.pyplot as plt

def analyze_color_histogram(image_path):
    img = cv2.imread(image_path)
    colors = ('b', 'g', 'r')
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Input Image")
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    for i, col in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col, label=f'{col.upper()} Channel')
        plt.xlim([0, 256])
    plt.title("Color Level Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.show()

analyze_color_histogram("assets/fruits.jpg")

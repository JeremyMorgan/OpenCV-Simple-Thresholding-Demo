import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("images/pickup.png", cv2.IMREAD_GRAYSCALE)

threshold_value = 127
max_value = 255


ret, thresholded_image = cv2.threshold(
    image, threshold_value, max_value, cv2.THRESH_TOZERO_INV)

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(thresholded_image, cmap='gray')
plt.title("THRESH_TOZERO_INV Image")
plt.axis("off")

plt.show()

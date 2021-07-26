import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png', cv2.IMREAD_GRAYSCALE)
# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(img, kernal, iterations = 2)
erosion = cv2.erode(img, kernal, iterations = 2)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernal)



titles = ['image', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, dilation, erosion, opening, closing, mg, th]

for i in range(7):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
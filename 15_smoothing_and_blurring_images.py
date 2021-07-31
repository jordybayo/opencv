# Homogeneousfilter, gaussian filter, median filter, bilateral filter, 

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('after.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 0)

title = ['image', '2D convulution', 'blur', 'gblur']
images = [img, dst, blur, gblur]


for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()

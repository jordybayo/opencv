import numpy as np
import cv2 as cv

def print_callback(x):
    print(x)

# creater a black image, a window
# img = np.zeros((300, 521, 3), np.uint8)

cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 10, 400, print_callback)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, print_callback)

while True:
    img = cv.imread('lena.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (150, 150), font, 4, (0, 255, 255) )
    
    
    k = cv.waitKey(1) & 0xff
    if k == 27:
        break
    
    s = cv.getTrackbarPos(switch, 'image')
    
    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('image', img)

cv.destroyAllWindows()
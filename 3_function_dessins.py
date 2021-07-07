import cv2
import numpy as np

img = np.zeros([521, 512, 3], np.uint8)

# img = cv2.imread('lena.jpg', 1)  # o graysacle, 1 rgb


img = cv2.line(img, (0, 0), (255, 255), (181, 79, 16), 5)  # 16, 79, 181
img = cv2.arrowedLine(img, (0, 255), (255, 255), (181, 79, 16), 5)  # 16, 79, 181


img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)


cv2.imshow('image', img)


k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.jpg', img=img)
    cv2.destroyAllWindows()

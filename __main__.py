import cv2
import numpy as np

img = cv2.imread('images/icon.png')
# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# img = cv2.GaussianBlur(img, (13,13), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 90, 90)
kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
# img[3:120, 12:116]
cv2.imshow('result', img)
print(img.shape)
cv2.waitKey(0)

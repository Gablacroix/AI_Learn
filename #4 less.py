import cv2
import numpy as np

img = cv2.imread('images/icon.png')
new_img = np.zeros(img.shape, dtype='uint8')
#img = cv2.flip(img, 1)
def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, mat, (width, height))
#img = rotate(img, 90)
def tranform(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param,mat, (img_param.shape[1], img_param.shape[0]))
#img = tranform(img, 30, 30 )
#img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 20, 20)
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img, con, -1, (230, 111, 222), thickness=1)
cv2.imshow('D', new_img)
cv2.waitKey(0)
import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')
# photo[100:150, 200:250] = 255, 0, 0
cv2.rectangle(photo, (70, 70), (100, 100), (120, 252, 50), thickness=cv2.FILLED)
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (120, 252, 50), thickness=3)
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (120, 252, 50), thickness=1)
cv2.putText(photo, 'SteelShark', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), thickness=1)
cv2.imshow('Photo', photo)
# print(cv2.__version__)

cv2.waitKey(0)

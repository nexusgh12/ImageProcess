import numpy as np
import cv2

img = cv2.imread('images/musk.jpg',0)
# 0 : gray 1 : color , -1: unchanged
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # 아스키 코드wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):   # 유니코드 읽어오기wait for 's' key to save and exit.
    cv2.imwrite('images/muskgray.png',img) # 저장
    cv2.destroyAllWindows()#모든 창 닫기




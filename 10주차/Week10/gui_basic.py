# Drawing lines, circles, ... on opencv window

import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

cv2.line(img,(0,0),(511,511),(255,0,0),10) # rgb, thickness=10
cv2.rectangle(img,(370,3),(510,135),(0,255,0),3)
cv2.circle(img,(440,70), 60, (0,0,255), 3) 
cv2.circle(img,(440,70), 30, (255, 255, 255),-1) # -1 : filled.
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts0 = np.array([[100,5],[100,200],[200,200]], np.int32)
pts = pts0.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(255,255,0), 2)
print('pts0={}, pts={}'.format(pts0.shape, pts.shape))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 1,(255,255,255),3,cv2.LINE_AA)
#글자 작성 (시작점, 텍스트, (시작점 x, y_), 폰트, 글자 간격, 글자 색, 두께< anti-aliasing_
cv2.imshow('drawings', img)
cv2.waitKey(0)

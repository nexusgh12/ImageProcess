import cv2

freezeFlag = False
font = cv2.FONT_HERSHEY_SIMPLEX


def sketchify(img, ksize=5):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median filter to the grayscale image
    img_gray = cv2.medianBlur(img_gray, 7)

    # Detect edges in the image and threshold it
    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=ksize)
    ret, sketch = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

    sketch_bgr = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
    return sketch_bgr


def onMouseEvent(event, x, y, flags, userdata) :
   global freezeFlag
   if event==cv2.EVENT_LBUTTONDOWN :
      freezeFlag = False
      #마우스 좌클릭하면 재생
   elif event==cv2.EVENT_RBUTTONDOWN :
      freezeFlag = True
       #우클릭하면 정지

cv2.namedWindow('videoWindow')
cv2.setMouseCallback('videoWindow', onMouseEvent)
cap = cv2.VideoCapture('images/video_Twice.mp4')
#비디오 캡쳐

#Ecap = cv2.VideoCapture(0)  # web cam에서 영상 불러옴

while(cap.isOpened()):
   if not freezeFlag :  # 화면 재생
      ret, frame = cap.read() # capture a frame 하나의 프레임을 리드함
      frame = sketchify(frame)
      frameCopy = frame.copy()
      cv2.putText(frame,'Playing',(10,50),font,1,(0,0,255),3)
      cv2.imshow('videoWindow', frame)
   else :   # 화면 정지
      cv2.putText(frameCopy,'Stopped',(10,50),font,1,(0,255,0),3)
      cv2.imshow('videoWindow', frameCopy)

   c = cv2.waitKey(10) # wait for 10ms
   print('freezeFlag ', freezeFlag)
   if c == 27 :
      break

cap.release()
cv2.destroyAllWindows()


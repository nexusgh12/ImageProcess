import cv2
import math

# Lists to store the points
center=[]
circumference=[]

def drawCircle(action, x, y, flags, userdata):
  # Referencing global variables 
  global center, circumference
  # Action to be taken when left mouse button is pressed
  if action==cv2.EVENT_LBUTTONDOWN:#누른것이 왼쪽 버튼이면
    center=[(x,y)]
    # Mark the center
    cv2.circle(source, center[0], 1, (0, 0, 255), 2)
    #눌렀을 때 빨간 점을 찍어라
    # Action to be taken when left mouse button is released
  elif action==cv2.EVENT_LBUTTONUP:#버든 뗄때
    circumference=[(x,y)]
    #버튼 뗀곳의 위치

    # Calculate radius of the circle
    radius = math.sqrt(math.pow(center[0][0]-circumference[0][0],2)+
                        math.pow(center[0][1]-circumference[0][1],2))
    #반지름 계산
    # Draw the circle
    cv2.circle(source, center[0], int(radius), (0,255,0), 2)
    #원 그리기

    cv2.imshow("Window",source)

source = cv2.imread("images/musk.jpg")
cv2.namedWindow("Window") #윈도우 이름 설정
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawCircle) #이벤트 설정
k = 0
# loop until escape character is pressed
while k!=27 :
    cv2.imshow("Window", source)
    cv2.putText(source, 'Choose center, and drag. ESC to exit' ,
              (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2 );
    k = cv2.waitKey(20)

cv2.destroyAllWindows()



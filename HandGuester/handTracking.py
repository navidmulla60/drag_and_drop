import cv2
import mediapipe as mp
import time

mpDraw=mp.solutions.drawing_utils
mpHand=mp.solutions.hands
hands=mpHand.Hands()
cap=cv2.VideoCapture(0)



# cap=cv2.VideoCapture('testvideos/1.mp4')

pTime=0
while True:
    success,img=cap.read()
    

    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w) , int(lm.y*h)
                if id ==0 :
                    cv2.circle(img,(cx,cy),25,(255,100,200),cv2.FILLED)
            mpDraw.draw_landmarks(img, handlms,mpHand.HAND_CONNECTIONS)
    
    ctime=time.time()
    fps=1/(ctime-pTime)
    pTime=ctime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
                        (255,0,255),3)
    cv2.imshow("image", img)
    cv2.waitKey(1)
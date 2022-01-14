from operator import le
import cv2
from cvzone.HandTrackingModule import HandDetector
from HandGuester.handTrackingModule import handDetector

wcam, hcap = 500, 500
pTime=0
# cap = cv2.VideoCapture('testvideos/1.mp4')
cap = cv2.VideoCapture(0)
# cap.set(3, wcam)
# cap.set(4, hcap) 
Rectcol=255,0,0

cx,cy,w,h=200,200,80,80


# class DragRect():
#     def __init__(self,posCentre,size=[200,200]):
#         self.poscentre=posCentre
#         self.size=size

#     def update(self,cursor):




detector=handDetector(minDetCon=0.8)





while True:
    success,img=cap.read()
    size=img.shape

    img=cv2.flip(img,1)
    img=detector.findHand(img,draw=False)
    lmList=detector.findPostion(img,draw=False)
    if lmList:
        point1=lmList[8][1],lmList[8][2]
        point2=lmList[12][1],lmList[12][2]
        leng=detector.findDistance(img,point1,point2)
        print(leng)
        if leng<35:
            cursor=lmList[8]
            print(cursor)

            if cx-w//2 <cursor[1]<cx+w//2 and cy-h//2<cursor[2]<cy+h//2:
                Rectcol=255,0,255
                i,cx,cy=cursor
            else:
                Rectcol=255,0,0   
            cv2.circle(img, (cursor[1],cursor[2]),15,(255,0,0),cv2.FILLED)
    cv2.rectangle(img, (cx-w//2,cy-h//2),(cx+w//2,cy+h//2),Rectcol,cv2.FILLED)
    
    cv2.imshow("image", img)
    cv2.waitKey(1)
import cv2
import mediapipe as mp
import time
import math

class handDetector():
    def __init__(self,mode=True,maxHand=2,minDetCon=0.5,minTraCon=0.5):
        self.mode=mode
        self.maxHand=maxHand
        self.minDetCon=minDetCon
        self.minTraCon=minTraCon

        self.mpDraw=mp.solutions.drawing_utils
        self.mpHand=mp.solutions.hands
        self.hands=self.mpHand.Hands(self.mode
                                    ,self.maxHand
                                    ,self.minDetCon
                                    ,self.minTraCon)

    def findHand(self,img,draw=True):

        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlms,self.mpHand.HAND_CONNECTIONS)
        return img
        
    def findPostion(self,img, handNo=0, draw=True):
        lmList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w) , int(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),25,(255,100,200),cv2.FILLED)
        return lmList

    def findDistance(self,img,point1,point2):
        x1,y1=point1
        x2,y2=point2
        length = math.hypot(x2-x1, y2-y1)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        return length

    

def main():
    cap=cv2.VideoCapture('testvideos/1.mp4')
    pTime=0
    while True:
        success,img=cap.read()
        detector=handDetector()
        img=detector.findHand(img)
        lmlist=detector.findPostion(img)
        # print(lmlist[4])
        ctime=time.time()
        fps=1/(ctime-pTime)
        pTime=ctime

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
                            (255,0,255),3)
        cv2.imshow("image", img)
        cv2.waitKey(1)

if __name__=="__main__":
    main()
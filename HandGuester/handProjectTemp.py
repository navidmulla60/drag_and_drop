import cv2
import time
import handTrackingModule as hm



cap=cv2.VideoCapture('testvideos/1.mp4')
pTime=0
while True:
    success,img=cap.read()
    detector=hm.handDetector()
    img=detector.findHand(img)
    lmlist=detector.findPostion(img)
    print(lmlist[4])
    ctime=time.time()
    fps=1/(ctime-pTime)
    pTime=ctime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
                        (255,0,255),3)
    cv2.imshow("image", img)
    cv2.waitKey(1)
import cv2
import numpy as np


def roi(img,ver):
    mask=np.zeros_like(img)
    #c=(255,)*img.shape[2]
    cv2.fillPoly(mask,np.int32([ver]),255)
    maskimg=cv2.bitwise_and(img,mask)
    return maskimg
def drow(img,lines):
    img=np.copy(img)
    bi=np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)
    img=cv2.addWeighted(img,0.8,bi,1,0.0)
    return img
def pro(img):
    #print(img.shape)
    h=img.shape[0]
    w=img.shape[1]
    re=np.array([(0,h),(w/2,h/1.7),(w,h)])
    
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    canny=cv2.Canny(gray,100,200)
    cp=roi(canny,re)
    lines=cv2.HoughLinesP(cp,6,np.pi/180,160,np.array([]),40,30)
    #lines = cv2.HoughLinesP(cp,
                            #rho=6,
                            #theta=np.pi/180,
                            #hreshold=160,
                            #lines=np.array([]),
                            #minLineLength=40,
                            #maxLineGap=25)
    last=drow(img,lines)
    return last
cap=cv2.VideoCapture("test.mp4")
while cap.isOpened():
    ret,fram=cap.read()
    frames=pro(fram)
    cv2.imshow("fram",frames)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()


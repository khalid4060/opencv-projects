import numpy as np
import cv2
#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("vtest.avi")
_,fram1=cap.read()
_,fram2=cap.read()
#img=cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
while cap.isOpened():
  fram=cv2.absdiff(fram1,fram2)
  img=cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
  blur=cv2.GaussianBlur(img,(5,5),0)
  ret,thres=cv2.threshold(blur,15,255,cv2.THRESH_BINARY)
  dilat=cv2.dilate(thres,None,iterations=3)
  cont,hi=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  centers=[]
  #cv2.drawContours(fram1,cont,-1,(0,255,0),3)
  for conts in cont:
      (x,y,w,h)=cv2.boundingRect(conts)
      if cv2.contourArea(conts)<900:
          continue
      #elif cv2.contourArea(conts)>2000:
            #continue  
      M = cv2.moments(conts)
      cX = int(M['m10'] /M['m00'])
      cY = int(M['m01'] /M['m00'])
      centers.append([cX,cY])
      if len(centers)>=2:
       dx= centers[0][0] - centers[1][0]
       dy = centers[0][1] - centers[1][1]
       D = np.sqrt(dx*dx+dy*dy)
       #print(D)
       #if D<300:
          #cv2.rectangle(fram1,(x,y),(x+w,y+h),(0,0,255),2)
       #else:    
         #cv2.rectangle(fram1,(x,y),(x+w,y+h),(0,255,0),2)
       cv2.rectangle(fram1,(x,y),(x+w,y+h),(0,255,0),2)  
         
  cv2.imshow("frame",fram1)
  #cv2.imshow("fr",blur)
  fram1=fram2
  _,fram2=cap.read()
  cv2.waitKey(50)
cap.release()

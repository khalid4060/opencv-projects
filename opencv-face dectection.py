import cv2
facecas=cv2.CascadeClassifier("cas.xml")
cap=cv2.VideoCapture(0)
while cap.isOpened():
    _,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=facecas.detectMultiScale(gray,1.1,10)
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("fram",img)
    cv2.waitKey(1)
cap.release()     

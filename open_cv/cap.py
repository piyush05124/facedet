import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier(r'C:\Users\user\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml ')
#eye_cascade =cv2.CascadeClassifier(r'E:\crawler\open_cv\cascades\data\haarcascade_eye_tree_eyeglasses.xmlhaarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.Canny(frame,150,100)
    face=face_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=3)
    for(x,y,w,h) in face:
        #print(x,y,w,h)
        org = (x,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (0, 255, 10)  
        thickness = 3        
        if face.all() :
            cv2.rectangle(frame, (x,y), (x+w ,y+h),(255,0,0) , 2)
            cv2.putText(frame, 'Person', org, font,fontScale, color, thickness, cv2.LINE_AA)
        #roi=frame[y:y+h , x:x+w]
        #ee=eye_cascade.detectMultiScale(roi)
        #for(ex,ey,ew,eh) in ee:
           # cv2.rectangle(roi, (ex,ey), (ex+ew,ey+eh),(0,255,0),2)

      
    #cv2.putText(frame, 'Person', cv2.FONT_HERSHEY_DUPLEX, 2,(0, 255, 0), 3)    
    cv2.imshow('frame',frame )
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()


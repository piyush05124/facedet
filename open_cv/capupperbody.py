import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier(r'C:\Users\user\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml    ')
#eye_cascade =cv2.CascadeClassifier(r'C:\Users\user\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_smile.xml ')


path=r'E:\crawler\open_cv\test_p2.jpg '
frame=cv2.imread(path)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#gray = cv2.Canny(frame,150,100)
face=face_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5)
for(x,y,w,h) in face:
    print(x,y,w,h)
    org = (x,y)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0, 255, 10)  
    thickness = 3        
    if face.all() :
        cv2.rectangle(frame, (x,y), (x+w ,y+h),(255,0,100) , 2)
        cv2.putText(frame, 'Person', org, font,fontScale, color, thickness, cv2.LINE_AA)

      
       
cv2.imshow('frame',frame )
cv2.waitKey(0)
cv2.destroyAllWindows()


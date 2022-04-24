
import cv2

boy = cv2.imread("boy.jpg")
gray= cv2.cvtColor(boy, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray)

print(len(faces))

for (x,y,w,h) in faces:
       
       cv2.rectangle(boy,(x,y),(x+w,y+h),(255,0,0),2)  

       # Crop the image to save the face image.
       roi_color = boy[y:y+h, x:x+w]
       cv2.imwrite("New_Boy.jpg",roi_color)
              
cv2.imshow('img',boy)
cv2.waitKey(0)
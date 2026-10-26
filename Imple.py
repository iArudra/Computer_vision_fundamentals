import os
import cv2 as cv

#This file identifies the person in the picture sent as input, and prints the name of the identified person

harchar = cv.CascadeClassifier('Face.xml')
rec = cv.face.LBPHFaceRecognizer_create()
rec.read("Daddy.yml")
p = []
for i in os.listdir(r'C:\1.Nikhil\STUDIES\Additional\AI - Cibi sir\Pictures\Face R'):
    p.append(i)
img = cv.imread(r"C:\1.Nikhil\PERSONAL\PICS\FAMILY\DSC00287.JPG")
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
fr = harchar.detectMultiScale(grey, scaleFactor= 1.1, minNeighbors=15)
for (x,y,w,h) in fr:
    roi = grey[y:y+h, x:x+h]
    label, con = rec.predict(roi)
    print("Label = "+ p[label], "confidence value", con)
    cv.putText(img, str(p[label]), (x+15,y-50), cv.FONT_HERSHEY_SIMPLEX, 5, (0,255,0), thickness=  5)
    cv.rectangle(img, (x,y), (x+w, y+w), (0, 255,0), thickness=2)
img = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA) # Cubic or liner will be used when img is enlargerd
cv.imshow("Detected", img)
cv.waitKey(0)

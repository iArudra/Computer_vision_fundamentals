import cv2 as cv
# This file detects faces in the img passed through
#Using Hard Cascade
#Its very sensitive to noice, they are most popular but not most advance and perfect


"""img = cv.imread("Pictures/201213-team-photo-of-german-bundesliga-club-borussia-dortmund-last-CMF36D.jpg")
#Face detection doesnt involve color tone So,
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
harcas = cv.CascadeClassifier('Face.xml')
face= harcas.detectMultiScale(grey, scaleFactor= 1.1, minNeighbors=3) #By increasing the minNeigh.. we can cut short the no. of face detect
for (x,y,w,h) in face:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0))

print(len(face))
cv.imshow("FACE", img)
cv.waitKey(0)"""

#Live Camera
cam = cv.VideoCapture(0)
cv.namedWindow("Camera")
count =0
while True:
    ret, frame = cam.read()
    har = cv.CascadeClassifier('Face.xml')
    face = har.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)
    for(x,y,w,h) in face:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255))
    cv.imshow("Face", frame)
    if not ret:
        print("Failed to connect")
        break
    k = cv.waitKey(0)
    if k%256 ==27:
        break
    if k%256 ==32:
        img = "opencv_capture_{}.png".format(count)
        cv.imwrite(img, frame)
        count += 1
cam.release()
cv.destroyAllWindows()

"""
cam = cv.VideoCapture(0)
cv.namedWindow("Camera")
count =0
while True:
        ret, frame = cam.read()
        har = cv.CascadeClassifier('Face.xml')
        face = har.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)
        for(x,y,w,h) in face:
            count +=1
            cv.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255))
            cropped = frame[y:y+h, x:x+w]
            cv.imshow("Face", cropped)
        break
cam.release()
print(count)"""
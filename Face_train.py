import os
import cv2 as cv
import numpy as np

#This file is to train the system to recognize a person face to identify the person

p = []
for i in os.listdir(r'C:\1.Nikhil\STUDIES\Additional\AI - Cibi sir\Pictures\Face R'):
    p.append(i)
print(p)
dir = r"C:\1.Nikhil\STUDIES\Additional\AI - Cibi sir\Pictures\Face R"
features = []
labels = []
harcas = cv.CascadeClassifier('Face.xml')
def create_train():
    for person in p:
        path = os.path.join(dir, person)
        label = p.index(person)

        for img in os.listdir(path):
            paths = os.path.join(path, img)
            img_aray = cv.imread(paths)
            grey = cv.cvtColor(img_aray, cv.COLOR_BGR2GRAY)
            faces = harcas.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=15)
            for (x, y, w, h) in faces:
                face_roi = grey[y:y + h, x:x + w]
                features.append(face_roi)
                labels.append(label)
                cv.destroyAllWindows()


create_train()
print("Training done")
features = np.array(features, dtype='object')
labels = np.array(labels)
Face_re = cv.face.LBPHFaceRecognizer_create()
Face_re.train(features, labels)
np.save('Features.npy', features)
np.save('Labels.npy', labels)
Face_re.save('Daddy.yml')

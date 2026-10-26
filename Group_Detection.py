"""import cv2 as cv

imgpre = cv.imread("Pictures/wp1862740.jpg")
def frame_size(frame, scale= 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0] *scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation= cv.INTER_AREA)
img = frame_size(imgpre, scale=0.25)
p=[]
n = 0
same = 0
diff = 0
features = []
labels = []
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
harcas = cv.CascadeClassifier('Face.xml')
face= harcas.detectMultiScale(grey, scaleFactor= 1.1, minNeighbors=3)
for (x,y,w,h) in face:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0))
    p.append(n+1)
    face_roi = grey[y:y + h, x:x + w]
    features.append(face_roi)
    labels.append(n)
    cv.destroyAllWindows()
print("Total faces in picture 1 ", len(face))
cv.imshow("FACES of team 1", img)
cv.waitKey(0)

img1pre = cv.imread("Pictures/wp4012092.jpg")
img1 = frame_size(img1pre, scale=0.25)
grey1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
harcas = cv.CascadeClassifier('Face.xml')
face1= harcas.detectMultiScale(grey, scaleFactor= 1.1, minNeighbors=3)
for (x,y,w,h) in face1:
    face_roi1 = grey1[y:y + h, x:x + w]
    for i in features:
        if face_roi1.all()== i.all():
            same +=1
            cv.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0))
        else:
            diff +=1
            cv.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255))
    cv.destroyAllWindows()
print("Total faces in picture 2 ", len(face1))
cv.imshow("FACES of team 2", img1)
cv.waitKey(0)
print("Percentage of same members are: ", (same/(same+diff))*100)
"""
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=25, minSize=(30, 30))
    return faces

def extract_faces(image, faces):
    face_images = []
    for (x, y, w, h) in faces:
        a = image[y:y+h, x:x+w]
        face_images.append(a)
        cv2.imshow("Face", a)
        cv2.waitKey(1000)
    return face_images

def compare_faces(face1, face2):
    face1 = cv2.resize(face1, (100, 100))
    face2 = cv2.resize(face2, (100, 100))
    error = np.mean((face1 - face2) ** 2)
    return error

def find_similar_faces(faces1, faces2, threshold=1000):
    similar_count = 0
    for face1 in faces1:
        for face2 in faces2:
            if compare_faces(face1, face2) < threshold:
                similar_count += 1
                break
    return similar_count

# Load two images
image1 = cv2.imread("Pictures/20160828_105252.jpg")
image2 = cv2.imread('Pictures/20160828_105221(0).jpg')


# Detect faces in each image
faces1 = detect_faces(image1)
faces2 = detect_faces(image2)

# Extract face regions
face_images1 = extract_faces(image1, faces1)
face_images2 = extract_faces(image2, faces2)

# Count the number of similar faces
similar_faces_count = find_similar_faces(face_images1, face_images2)

print(f'Number of similar faces: {similar_faces_count-1}')

import cv2
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import cv2 as cv
import numpy as np
unique_faces =[]
features = []
no=0
def frame_size(frame, scale= 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0] *scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation= cv.INTER_AREA)

def is_unique(face, unique_faces):
    face_hist = cv.calcHist([face], [0], None, [256], [0, 256])
    for u_face_hist in unique_faces:
        comp = cv.compareHist(face_hist, u_face_hist, cv.HISTCMP_CORREL)
        if comp > 0.6:  # Threshold for histogram similarity (adjust as necessary)
            return False
    return True

capture  = cv.VideoCapture("Pictures/VID-20220815-WA0005.mp4")
while True:
    isTrue, frame = capture.read()
    frame_b = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    h = cv.CascadeClassifier("Face.xml")
    f = h.detectMultiScale(frame_b, scaleFactor= 1.1, minNeighbors= 10, minSize=(40,40))
    for (x,y,w,h) in f:
        cv.rectangle(frame_b, (x,y), (x+w,y+h), (255,0,0))
        face_roi = frame_b[y:y + h, x:x + w]
        fare = cv.resize(face_roi,(100,100))
        if is_unique(fare, unique_faces):
            face_hist = cv.calcHist([fare], [0], None, [256], [0, 256])
            unique_faces.append(face_hist)
        fa_fl = fare.flatten()
        features.append(fa_fl)
    cv.imshow("Gif", frame_size(frame_b, scale= 0.5))
    if cv.waitKey(1) &  0xFF==ord("d"):
        break
capture.release()
cv.destroyAllWindows()
features = np.array(features)
print(f"Number of unique faces: {len(unique_faces)}")

"""
import cv2 as cv
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the video and Haar cascade for face detection
capture = cv.VideoCapture("WhatsApp Video 2024-08-05 at 16.03.19.mp4")
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

face_features = []

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4)

    for (x, y, w, h) in faces:
        face = gray_frame[y:y+h, x:x+w]
        face = cv.resize(face, (100, 100))  # Resize face region to fixed size
        face_flat = face.flatten()  # Flatten the face image
        face_features.append(face_flat)  # Collect the flattened face features

        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv.imshow("Frame", frame)
    if cv.waitKey(1) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()

# Convert to NumPy array
face_features = np.array(face_features)

# Apply PCA for dimensionality reduction
pca = PCA(n_components=50)  # Reduce to 50 dimensions
face_features_pca = pca.fit_transform(face_features)

# Determine the optimal number of clusters using the Silhouette method
silhouette_scores = []
range_n_clusters = list(range(2, 10))
for n_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(face_features_pca)
    cluster_labels = kmeans.labels_
    silhouette_avg = silhouette_score(face_features_pca, cluster_labels)
    silhouette_scores.append(silhouette_avg)

optimal_clusters = range_n_clusters[np.argmax(silhouette_scores)]
print(f"Optimal number of clusters: {optimal_clusters}")

# Apply K-means clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_clusters)
kmeans.fit(face_features_pca)
labels = kmeans.labels_

unique_faces = len(set(labels))
print(f"Number of unique faces detected: {unique_faces}")
"""
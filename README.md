# 👁️ OpenCV Face Recognition & Computer Vision

A hands-on learning project covering **OpenCV fundamentals through to a fully functional face recognition system** — capable of detecting, training on, and identifying specific people by name in images and live video.

> 📚 Built as part of an AI/Computer Vision course.

---

## 🚀 Features

- 🎥 **Live Webcam Face Detection** — Real-time face detection with bounding boxes and screenshot capture
- 🧠 **Face Recognition Training** — Train a model on labeled face images using LBPH algorithm
- 🪪 **Person Identification** — Identify a specific person in a photo and display their name
- 👥 **Group Face Comparison** — Compare two group photos to find common members
- 🎞️ **Video Unique Face Counting** — Count distinct faces across a video using histogram comparison and optional PCA + K-Means clustering
- 🛠️ **Core OpenCV Techniques** — Image transforms, blurring, edge detection, histograms, masking, bitwise ops, and more

---

## 🗂️ Project Structure

```
├── main.py               # Core OpenCV concepts & experimentation scratch pad
├── Detection.py          # Live webcam face detection + screenshot capture
├── Face_train.py         # Train LBPH face recognizer on labeled images
├── Imple.py              # Identify a person in a photo using the trained model
├── Group_Detection.py    # Compare faces across two group photos
├── Video_Detect.py       # Count unique faces in a video file
├── Face.xml              # Haar Cascade classifier for frontal face detection
├── Daddy.yml             # Saved trained LBPH face recognizer model
├── Features.npy          # Saved face feature arrays (from training)
├── Labels.npy            # Saved label array (from training)
└── Pictures/             # Input images and videos
    └── Face R/           # Labeled training images (one subfolder per person)
```

---

## 🧠 How It Works

### Training Pipeline
```
Pictures/Face R/
    ├── Person_A/   (multiple photos)
    └── Person_B/   (multiple photos)
         │
         ▼
    Face_train.py
    (Haar Cascade detects faces → LBPH Recognizer trains)
         │
         ▼
    Daddy.yml  ←  saved model
    Features.npy + Labels.npy  ←  saved data
```

### Recognition Pipeline
```
Input Image / Webcam
      │
      ▼
Haar Cascade (Face.xml)  →  Detect face region
      │
      ▼
LBPH Recognizer (Daddy.yml)  →  Predict label + confidence
      │
      ▼
Display name on image
```

---

## 📋 Topics Covered (main.py)

| # | Topic |
|---|-------|
| 1 | Reading & displaying images and videos |
| 2 | Drawing shapes & writing text |
| 3 | Grayscale, blurring, edge detection (Canny, Laplacian, Sobel) |
| 4 | Image transformations — translation, rotation, flip |
| 5 | Contour detection |
| 6 | Color spaces (BGR, RGB, HSV, LAB) and color channel splitting |
| 7 | Blurring techniques (Average, Gaussian, Median, Bilateral) |
| 8 | Bitwise operators & masking |
| 9 | Histograms (grayscale, color, interactive live chart) |
| 10 | Thresholding (simple, inverse, adaptive) |
| 11 | Quadrant-wise image analysis |
| 12 | Mouse callback interactions |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- pip

### Install Dependencies

```bash
pip install opencv-python opencv-contrib-python numpy scikit-learn
```

> ⚠️ `opencv-contrib-python` is required for the `cv2.face.LBPHFaceRecognizer` module.

---

## ▶️ Usage

### 1. Live Face Detection (Webcam)
```bash
python Detection.py
```
- Press **`Space`** to capture a screenshot
- Press **`Esc`** to quit

### 2. Train the Face Recognizer
```bash
# First, organize your training images:
# Pictures/Face R/<Person_Name>/<image1.jpg> ...

python Face_train.py
```
Outputs: `Daddy.yml`, `Features.npy`, `Labels.npy`

### 3. Identify a Person in a Photo
```bash
python Imple.py
```
Displays the detected person's name overlaid on the image.

### 4. Compare Faces in Two Group Photos
```bash
python Group_Detection.py
```
Prints the number of similar faces found between two photos.

### 5. Count Unique Faces in a Video
```bash
python Video_Detect.py
```
Press **`d`** to stop processing and print the unique face count.

---

## 🛠️ Tech Stack

| Library | Use |
|---|---|
| `OpenCV (cv2)` | Core computer vision operations |
| `opencv-contrib-python` | LBPH Face Recognizer |
| `NumPy` | Array and matrix operations |
| `scikit-learn` | PCA dimensionality reduction & K-Means clustering |

---

## 📌 Notes

- The Haar Cascade method is fast but sensitive to noise and lighting.
- LBPH (Local Binary Patterns Histograms) is a classical, lightweight face recognition algorithm — no deep learning required.
- For better accuracy, use more training images per person (10–30 recommended).
- The `minNeighbors` parameter in `detectMultiScale` controls detection sensitivity — increase it to reduce false positives.

---

## 📄 License

This project is for educational purposes.


"""
#Reading videos
capture = cv.VideoCapture("Pictures/Xiao.gif")
while True:
     isTrue, frame = capture.read()
     cv.imshow("Gif", frame)
     if cv.waitKey(20) & 0xFF==ord('d'):
         break
capture.release()
cv.destroyAllWindows()
"""

"""
#Resizing
def frame_size(frame, scale= 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0] *scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation= cv.INTER_AREA)

#Video resizing
capture = cv.VideoCapture("Pictures/Xiao.gif")
while True:
     isTrue, frame = capture.read()
     frame_re = frame_size(frame)
     cv.imshow("Gif", frame)
     cv.imshow("gif_resize", frame_re)
     if cv.waitKey(20) & 0xFF==ord('d'):
         break
capture.release()
cv.destroyAllWindows()

#Image resizing
img = cv.imread("Pictures/Ganesha.jpeg")
imgre = frame_size(img, scale = 0.2)
cv.imshow("img", img)
cv.imshow("img re", imgre)
cv.waitKey(0)
"""
"""
#Draw and Write
import numpy as np
img = cv.imread("Pictures/Ganesha.jpeg")
cv.imshow("Image", img)
#To draw on a pic we can use 2 methods
#One of which is to creat a blank pic using numpy
blank = np.zeros((500,500,3), 'uint8')
cv.imshow("Blank", blank)
#Paint green
blank[:] = 0,0,255
cv.imshow("Red", blank)
#Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness=3) #cv.FILLED : to fill the rectangle with specified color or we could also use -1
cv.imshow("Rectangle", blank)
#Draw a circle
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (255,0,0), thickness= -1)
cv.imshow("Blue circle", blank)
#Draw a line
cv.line(blank, (blank.shape[0]//2, blank.shape[1]//2), (0,0), (0,255.0), thickness=4)
cv.imshow("With line", blank)
#Write text
cv.putText(blank, "HELLO WORLD!!!",(150,250), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), thickness=3)
cv.imshow("With words", blank)
cv.waitKey(0)
"""
"""
#Essential functions
img = cv.imread("Pictures/Ganesha.jpeg")
cv.imshow("Pic", img)

#Converting to grey scale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

#Bluring an image
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)
#Edge cascade
ec = cv.Canny(img, 125,175)
cv.imshow("Edge Cascade", ec)

#Dilating the imgage
dilate = cv.dilate(ec, (7,7), iterations=3)
cv.imshow("Dilate", dilate)

#Erode
er = cv.erode(dilate, (7,7), iterations=3)
cv.imshow("Erode", er)


#Resizing img
resize = cv.resize(img, (500,500), interpolation= cv.INTER_AREA) #Cubic or liner will be used when img is enlargerd
cv.imshow("Resize", resize)

#Crop
crop = img[200:700, 200:700]
cv.imshow('Crop', crop)
cv.waitKey(0)
"""
"""
#Image transformations
#Translation
def translte(img, x,y):
    trans = np.float32([[1,0,x], [0,1,y]])
    dim = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, trans, dim)
imgt = translte(img, 200,200) # +y ; down :: -y; up
cv.imshow('Transtated ', imgt)
cv.waitKey(0)

#Rotate
def rotate(img, angle, rotpoint = None):
    (height, width) = img.shape[:2]
    if rotpoint ==None:
        rotpoint = (width//2, height//2)
    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dim = (width, height)
    return cv.warpAffine(img, rotmat, dim)
roated = rotate(img, 45) # -angle ; clockwise
cv.imshow("rotated", roated)

#fliping
flip = cv.flip(img, 1)# 0 : vertical 1: horizontal -1:Both
cv.imshow("flip", flip)
cv.waitKey(0)
"""

"""
#Contour detection
#Using Edge Cascade
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(grey, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125,175)
cv.imshow("Canny", canny)
contour, hirar = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)# Retr_tree: hierarchy : Retr_external: ecternal
print(f"{len(contour)} contours found")
cv.waitKey(0)

#Using threshold
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(grey, 125,255, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)
contour, hirac = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contour)} contours found")
cv.waitKey(0)
"""
"""
#Color spaces
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("grey", grey)
cv.imshow("RGB", rgb)
cv.imshow("HSV", hsv)
cv.imshow("LAB", lab)
"""
"""
#Color channels
#In grey scale
b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('red', r)
mer  =cv.merge([b,g,r])
cv.imshow("Merged", mer)

#In their respective color
blank = np.zeros(img.shape[:2], 'uint8')
bl = cv.merge([b, blank, blank])
gr = cv.merge([blank, g, blank])
re = cv.merge([blank, blank, r])
cv.imshow("Blue", bl)
cv.imshow("Green", gr)
cv.imshow("Red", re)
cv.waitKey(0)
"""
"""
#Smoothing and bluring
#Average Bluring
av = cv.blur(img, (9,9))
cv.imshow("Average", av)
gs = cv.GaussianBlur(img, (9,9),0)
cv.imshow("Gs blur", gs)
#Gaussian blur gives lesser blur compared to average but it looks more natural
#Median Blur - More effective than both
med = cv.medianBlur(img, 9)
cv.imshow("Median blur", med)
#Bilateral bluring - Advance as it retains edges and only blurs its contents
bi = cv.bilateralFilter(img, 5, 15,15)
cv.imshow("Bilateral", bi)
"""

"""
#Bitwise operators
blank = np.zeros((400,400), 'uint8')
rec = cv.rectangle(blank.copy(), (30,30), (350, 350), 255, -1)
cir = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow("Rectangle", rec)
cv.imshow("Circle", cir)

band = cv.bitwise_and(rec, cir)
bor= cv.bitwise_or(rec,cir)
bxor = cv.bitwise_xor(rec, cir)
bnot = cv.bitwise_not(rec)
cv.imshow("And", band)
cv.imshow("OR", bor)
cv.imshow("XOR", bxor)
cv.imshow("Not", bnot)
"""

"""
#Masking
blank = np.zeros(img.shape[:2], 'uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 350,225, -1)
masked = cv.bitwise_and(img,img, mask = mask)
cv.imshow("Masked ", masked)
cv.waitKey(0)
"""

#Histogram
"""
#For grey scale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Image", grey)
ghist = cv.calcHist(grey, [0], None, [256], [0, 256])
plt.figure()
plt.title("Grey Scale Histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")
plt.plot(ghist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)

#For color
colors = ('b', 'g', 'r')
plt.figure()
plt.title("Grey Scale Histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")
for i, col in enumerate(colors):
    hist = cv.calcHist(img, [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()
"""
"""
#Different colors
b,g,r = cv.split(img)
plt.hist(b.ravel(), 256, [0,256], color= "Blue")
plt.title("Blue")
plt.show()
plt.hist(g.ravel(), 256, [0,256], color= "Green")
plt.title("Green")
plt.show()
plt.hist(r.ravel(), 256, [0,256], color="Red")
plt.title("Red")
plt.show()
cv.waitKey(0)

"""
"""
#Live chart
import cv2
def mouse_event(event, x, y, flags, param):
    global point
    if event == cv2.EVENT_MOUSEMOVE:
        i
        pixel_value = img[y, x]
        x = pixel_value
        y = hist[x]
        point, = plt.plot(x, y, 'ro')
        plt.draw()
        
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_event)
cv2.imshow("Image", img)

colors = ('b', 'g', 'r')
plt.figure()
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")
for i, col in enumerate(colors):
    hist = cv.calcHist(img, [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""Rough
max_bin_value = np.argmax(hist)
        max_pixel_value = max_bin_value * (256 // hist.shape[0])
        plt.hist(pixel_value, density=True)
        plt.hist(max_pixel_value, hist[max_bin_value], color='blue', marker='o')
        plt.show()
        plt.draw()

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel_value = img[y, x]
        val = cv.split(img)
        print(f"Pixel value at ({x}, {y}): {pixel_value}")
        plt.hist(pixel_value, density=True)
        plt.show()
        del hist
       
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        pixel_value = img[y, x]
        max_bin_value = np.argmax(hist)
        max_pixel_value = max_bin_value * (256 // hist.shape[0])
        plt.cla()  # Clear the previous plot
        plt.plot(hist, color='black')
        plt.hist(pixel_value, 256, color='red', marker='o')
        plt.hist(max_pixel_value, hist[max_bin_value], color='blue', marker='o')  # Highlight the max point
        plt.xlim([0, 256])
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.title(f'Pixel Value: {int(pixel_value)}')
        plt.draw()

# Set the mouse callback
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_event)
"""
"""
#Smoothing and bluring
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(grey, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125,175)
bi = cv.bilateralFilter(img, 5, 15,15)
cv.imshow("Bilateral", bi)
cv.imshow("Canny", canny)
cv.imshow("Blur", blur)
#Contour
contour, hirar = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)# Retr_tree: hierarchy : Retr_external: ecternal
print(f"Edge cascade: {len(contour)} contours found")
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(grey, 125,255, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)
contour, hirac = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"Threshold: {len(contour)} contours found")
cv.waitKey(0)
"""

#Quadrant analysis
"""
#Quadrant 1
blank = np.zeros(img.shape[:2], 'uint8')
x = img.shape[0]/2
y = img.shape[1]/2
mask = cv.rectangle(blank, (0,0), (int(x),int(y)), (225,0), thickness=-1)
masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Maksed",masked)
b,g,r = cv.split(masked)
plt.ylim(0,13000)
plt.xlim(5,249)
plt.hist(b.ravel(), 256, [0,256], color= "Blue")
plt.hist(g.ravel(), 256, [0,256], color= "Green")
plt.hist(r.ravel(), 256, [0,256], color="Red")
plt.title("Quadrant 1")
plt.show()
cv.waitKey(0)

#Quadrant 2
blank = np.zeros(img.shape[:2], 'uint8')
x = img.shape[0]
y = img.shape[1]
mask = cv.rectangle(blank,(int(x/2),int(y/2)), (x,0), (225,0,0), thickness=-1)
masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Maksed",masked)
b,g,r = cv.split(masked)
plt.ylim(0,13000)
plt.xlim(5,249)
plt.hist(b.ravel(), 256, [0,256], color= "Blue")
plt.hist(g.ravel(), 256, [0,256], color= "Green")
plt.hist(r.ravel(), 256, [0,256], color="Red")
plt.title("Quadrant 2")
plt.show()
cv.waitKey(0)


#Quadrant 3
blank = np.zeros(img.shape[:2], 'uint8')
x = img.shape[0]
y = img.shape[1]
mask = cv.rectangle(blank,(int(x/2),int(y/2)), (0,y), (225,0,0), thickness=-1)
masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Maksed",masked)
b,g,r = cv.split(masked)
plt.ylim(0,13000)
plt.xlim(5,249)
plt.hist(b.ravel(), 256, [0,256], color= "Blue")
plt.hist(g.ravel(), 256, [0,256], color= "Green")
plt.hist(r.ravel(), 256, [0,256], color="Red")
plt.title("Quadrant 3")
plt.show()
cv.waitKey(0)

#Quadrant 4
blank = np.zeros(img.shape[:2], 'uint8')
x = img.shape[0]
y = img.shape[1]
mask = cv.rectangle(blank,(int(x/2),int(y/2)), (x, y), (225,0,0), thickness=-1)
masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Maksed",masked)
b,g,r = cv.split(masked)
plt.ylim(0,13000)
plt.xlim(5,249)
plt.hist(b.ravel(), 256, [0,256], color= "Blue")
plt.hist(g.ravel(), 256, [0,256], color= "Green")
plt.hist(r.ravel(), 256, [0,256], color="Red")
plt.title("Quadrant 4")
plt.show()
cv.waitKey(0)
"""
"""
#Thresholding and Binarizing
#Simple Thresholding
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
threshold, thresh = cv.threshold(grey, 150, 255, cv.THRESH_BINARY) #Here 150 is the min thresh value and we use 255 as we have to convert it to 1 in binary
cv.imshow("Threshold" ,thresh)
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
threshold1, thresh_inv = cv.threshold(grey, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Inverse threshold", thresh_inv)

#Adaptive Thresholding
Adap = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adap", Adap)
cv.waitKey(0)
"""
"""
#Edge detection
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Laplacian
lap = cv.Laplacian(grey, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Lap", lap)

#Sobel
sobelx = cv.Sobel(grey, cv2.CV_64F, 1,0)
sobely = cv.Sobel(grey, cv2.CV_64F, 0,1)
com = cv.bitwise_or(sobelx, sobely)
cv.imshow("Com", com)
cv.waitKey(0)
#Canny is an advanced algorithm for sobel
"""

"""
import cv2

# Define the callback function that will be executed when a mouse event occurs
def mouse_callback(event, x, y, flags, param):
    # Check if the left mouse button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Access the pixel value at the (x, y) coordinate
        if len(param.shape) == 2:  # Grayscale image
            intensity = param[y, x]
            print(f"Grayscale intensity at ({x}, {y}) is {intensity}")
        else:  # Color image (BGR)
            (b, g, r) = param[y, x]
            print(f"BGR intensity at ({x}, {y}) is Blue: {b}, Green: {g}, Red: {r}")

# Load the image
image = cv2.imread('Pictures/IR1.png')  # Change the path to your image

# Create a window and set the mouse callback function
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_callback, param=image)

# Display the image and wait for the user to click
while True:
    cv2.imshow("Image", image)
    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
"""
"""
import cv2
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#Reading images
img = cv.imread("Pictures/20241009_232034.jpg")
# Live chart
import cv2
def mouse_event(event, x, y, flags, param):
    global point
    if event == cv2.EVENT_MOUSEWHEEL:
        i
        pixel_value = img[y, x]
        print(pixel_value)
        x = pixel_value
        y = hist[x]
        point, = plt.plot(x, y, 'ro')
        plt.draw()

img = cv.resize(img, (1000,1000), interpolation= cv.INTER_AREA) #Cubic or liner will be used when img is enlargerd
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_event)
cv2.imshow("Image", img)

colors = ('b', 'g', 'r')
plt.figure()
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")
for i, col in enumerate(colors):
    hist = cv.calcHist(img, [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

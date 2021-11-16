import cv2 

face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")

img = cv2.imread("image/boy.jpg")
img = cv2.resize(img, (800,800))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scaleFactor = 1.1
minNeighber = 3
face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

for (x,y,w,h) in face_detect:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 5, cv2.FILLED)

cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

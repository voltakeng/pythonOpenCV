import cv2 

eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

img = cv2.imread("image/boy.jpg")
img = cv2.resize(img, (800,800))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scaleFactor = 1.05
minNeighber = 3
eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

for (x,y,w,h) in eye_detect:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 5, cv2.FILLED)

cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

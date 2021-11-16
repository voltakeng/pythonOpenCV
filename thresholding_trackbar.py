import cv2 

img = cv2.imread("image/ant.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Thresholding_Trackbar")

def display(value):
    pass
cv2.createTrackbar("Thresh value", "Thresholding_Trackbar", 255, 255, display)

while True: 
    th_value = cv2.getTrackbarPos("Thresh value", "Thresholding_Trackbar")
    thresh, th = cv2.threshold(gray_img, th_value, 255, cv2.THRESH_BINARY)

    cv2.imshow("result",th)
    if cv2.waitKey(1) & 0xFF == ord("e"): 
        break

cv2.destroyAllWindows()
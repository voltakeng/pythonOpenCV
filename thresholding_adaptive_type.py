import cv2 

img = cv2.imread("image/map.jpg", 0)

thresh, th1 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 1)

cv2.imshow("THRESHOLD", th1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
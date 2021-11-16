import cv2 

img = cv2.imread("image/cat.jpg",0)
img_resize = cv2.resize(img,(400,400))
cv2.imshow("Output",img_resize)

cv2.imwrite("output.jpg",img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()

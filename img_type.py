import cv2 

# gray_scale
img_0 = cv2.imread("image/cat.jpg",0)

# rgb
img_1 = cv2.imread("image/cat.jpg",1)

img_0_resize = cv2.resize(img_0,(400,400))
img_1_resize = cv2.resize(img_1,(400,400))

cv2.imshow("gray_scale", img_0_resize)
cv2.imshow("rgb", img_1_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
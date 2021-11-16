import cv2 

img = cv2.imread("image/cat.jpg")
img_resize = cv2.resize(img, (700,700))

# ภาพ, center, radius, สี, ความหนา
# ถ้า ความหนา = -1 คือทึบ
cv2.circle(img_resize, (350,350), 70, (0,0,255), 5)

cv2.imshow("output", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
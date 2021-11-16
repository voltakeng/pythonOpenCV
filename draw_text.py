import cv2 

img = cv2.imread("image/cat.jpg")
img_resize = cv2.resize(img, (700,700))

# ภาพ, ข้อความ, พิกัด, font, ขนาด, สี, ความหนา, ประเภทเส้น
# เลือกfontที่: https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html
cv2.putText(img_resize, "CAT", (350,350), cv2.FONT_HERSHEY_DUPLEX, 2.5, (0,255,0), 5,cv2.LINE_4)

cv2.imshow("output", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
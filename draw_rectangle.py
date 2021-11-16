import cv2 

img = cv2.imread("image/cat.jpg")
img_resize = cv2.resize(img, (700,700))

# ภาพ, มุม1(บนซ้าย), มุม2(ล่างขวา), สี, ความหนา
# ถ้า ความหนา = -1 คือสี่เหลี่ยมทึบ
cv2.rectangle(img_resize, (100,100), (500,500), (0,0,255), 5)

cv2.imshow("output", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

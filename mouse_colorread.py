import cv2 

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        color = str(blue)+","+str(green)+","+str(red)

        cv2.putText(img, color, (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.imshow("output", img)

img = cv2.imread("image/color.jpg")

cv2.imshow("output", img)
cv2.setMouseCallback("output", clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2 

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = str(x)+","+str(y)
        cv2.putText(img, pos, (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,0), 3, cv2.LINE_AA)
        cv2.imshow("output", img)

img = cv2.imread("image/tree.jpg")

cv2.imshow("output", img)
cv2.setMouseCallback("output", clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()
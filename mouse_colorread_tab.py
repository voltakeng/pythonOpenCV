import cv2 
import numpy as np

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]

        width = 300
        high = 300
        rgb = 3 
        imgcolor=np.zeros([width,high,rgb],np.uint8)
        imgcolor[:] = [blue,green,red]
        #print(imgcolor)
        cv2.imshow("result", imgcolor)

img = cv2.imread("image/color.jpg")

cv2.imshow("output", img)
cv2.setMouseCallback("output", clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()
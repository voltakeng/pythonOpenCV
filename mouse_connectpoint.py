import cv2 
import numpy

img = numpy.zeros([800,800,3])
points = []

def clickPosition(event, x, y, flags, param): 
    if event == cv2.EVENT_LBUTTONDOWN: 
        cv2.circle(img, (x,y), 10, (255,255,255), 2, cv2.FILLED)

        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-2], points[-1], (255,255,255), 5)
            #print(points)
            #print(points[-1])
            #print(points[-2])
            
        cv2.imshow("output", img)


cv2.imshow("output",img)
cv2.setMouseCallback("output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()
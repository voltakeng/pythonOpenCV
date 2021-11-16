import cv2 

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check, frame  = cap.read()

    if check == True :
        cv2.imshow("output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"): 
            break
    else: 
        break

cap.release()
cv2.destroyAllWindows()
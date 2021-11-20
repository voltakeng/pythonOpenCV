import cv2 

cap = cv2.VideoCapture("image/Walking.mp4")

check, frame1 = cap.read()
check, frame2 = cap.read()

while (cap.isOpened()): 

    if check == True: 
        motiondiff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(motiondiff, cv2.COLOR_BGR2GRAY)
        gaussian = cv2.GaussianBlur(gray, (7,7), 10)
        thresh, binary = cv2.threshold(gaussian, 20, 255, cv2.THRESH_BINARY)
        dilation = cv2.dilate(binary, None, iterations=7)
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours: 
            (x,y,w,h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour)<2000: 
                continue
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2,cv2.FILLED)
                
        cv2.imshow("result", frame1)
        frame1 = frame2 
        check, frame2 = cap.read()

        if cv2.waitKey(1) & 0xFF == ord("e"):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()


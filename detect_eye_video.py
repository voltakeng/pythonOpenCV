import cv2 

eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")
cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):   
    check, frame  = cap.read()

    if check == True :

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        scaleFactor = 1.05
        minNeighber = 20
        eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

        for (x,y,w,h) in eye_detect:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 5, cv2.FILLED)

        cv2.imshow("output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"): 
            break

    else: 
        break

cap.release()
cv2.destroyAllWindows()

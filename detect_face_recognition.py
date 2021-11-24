import cv2 

face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture("image/Video.mp4")

clf = cv2.face.LBPHFaceRecognizer_create() 
clf.read("Detect/steve_jobs.xml")

while (cap.isOpened()):   
    check, frame  = cap.read()

    if check == True :

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        scaleFactor = 1.7
        minNeighber = 5
        face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 5, cv2.FILLED)

            id,confidence = clf.predict(gray_img[y:y+h,x:x+w])
    
            cv2.putText(frame, "Steve Jobs " + str(int(confidence)) + " %", (x,y-4), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,255), 2)
            print(confidence)

        cv2.imshow("output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"): 
            break

    else: 
        break

cap.release()
cv2.destroyAllWindows()

import cv2 
import datetime

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    check, frame  = cap.read()

    if check == True :
        currentDate = str(datetime.datetime.now())
        cv2.putText(frame,currentDate,(10,30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,0), 3, cv2.FILLED)

        cv2.imshow("output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"): 
            break
    else: 
        break

cap.release()
cv2.destroyAllWindows()
import cv2 
import numpy 

while True: 
    img = cv2.imread("image/ball2d.jpg")
    img = cv2.resize(img, (500,500))

    #ช่วงที่สีเข้มที่สุด
    lower = numpy.array([5,111,10])
    #ช่วงที่สีอ่อนที่สุด
    upper = numpy.array([124,255,133])

    mask = cv2.inRange(img,lower,upper)

    #เอาสีจากภาพต้นแบบไปทับmaskอีกที
    result = cv2.bitwise_and(img,img,mask=mask)
        
    cv2.imshow("Original",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",result)


    if cv2.waitKey(0) & 0xFF == ord("e"):
        break


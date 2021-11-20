import cv2 
import matplotlib.pyplot as plt 

img = cv2.imread("image/currency.jpg")

sobelX = cv2.Sobel(img, -1, 1, 0)
sobelY = cv2.Sobel(img, -1 ,0, 1)
sobelXY = cv2.bitwise_or(sobelX, sobelY)

titles = ["ORI","X","Y","XY"]
images = [img,sobelX,sobelY,sobelXY]

for i in range(len(images)): 
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

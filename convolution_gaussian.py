import cv2 
import matplotlib.pyplot as plt 
import numpy as np

img = cv2.imread("image/noise.png")

convo = cv2.filter2D(img, -1, np.ones((5,5), np.float32)/25) 
blur = cv2.blur(img,(5,5))
median = cv2.medianBlur(img,5)
gaussian = cv2.GaussianBlur(img,(7,7),100)

titles = ["ORIGINAL","Filter","Blur","MBlur","GBlur"]
images = [img,convo,blur,median,gaussian]

for i in range(len(images)): 
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

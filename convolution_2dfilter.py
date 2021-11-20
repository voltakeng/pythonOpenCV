import cv2 
import matplotlib.pyplot as plt 
import numpy as np

img = cv2.imread("image/noise.png")

convo3x3 = cv2.filter2D(img, -1, np.ones((3,3), np.float32)/9)
convo5x5 = cv2.filter2D(img, -1, np.ones((5,5), np.float32)/25) 

titles = ["ORIGINAL","3x3", "5x5"]
images = [img,convo3x3,convo5x5]

for i in range(len(images)): 
    plt.subplot(1,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()



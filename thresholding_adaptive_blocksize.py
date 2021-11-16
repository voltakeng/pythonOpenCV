import cv2 
import matplotlib.pyplot as plt 

gray_img = cv2.imread("image/map.jpg", 0)
blocksize = [3,5,9,17,33]
plt.subplot(231,xticks=[],yticks=[])
plt.title("Original")
plt.imshow(gray_img,cmap="gray")

for i in range(len(blocksize)): 
    result = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blocksize[i], 1)
    plt.subplot(232+i)
    plt.title("%d"%blocksize[i])
    plt.imshow(result,cmap="gray")
    plt.xticks([]),plt.yticks([])

plt.show()

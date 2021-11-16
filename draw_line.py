import cv2 

img = cv2.imread("image/cat.jpg")

img_resize = cv2.resize(img,(700,700))

init_x = 100
init_y = 100
final_x = 500
final_y = 200
color_b = 255
color_g = 0
color_r = 0
thickness = 10

#cv2.line(img_resize, (init_x,init_y), (final_x,final_y), (color_b,color_g,color_r), thickness)
cv2.arrowedLine(img_resize, (init_x,init_y), (final_x,final_y), (color_b,color_g,color_r), thickness)

cv2.imshow("output", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

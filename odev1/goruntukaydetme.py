import cv2 

carimage = cv2.imread("bugatti-centodieci.jpg")
cv2.imshow("Car Image", carimage)


cv2.imwrite("araba.jpg", carimage)
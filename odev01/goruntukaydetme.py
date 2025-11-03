import cv2 

carimage = cv2.imread("bugatti-centodieci.jpg")
cv2.imshow("Car Image", carimage)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite("araba.jpg", carimage)







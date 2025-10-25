import cv2 

carimage = cv2.imread("bugatti-centodieci.jpg")

cv2.imshow("Car Image", carimage)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite("araba.jpg", carimage)

gray_carimage = cv2.cvtColor(carimage, cv2.COLOR_BGR2GRAY)






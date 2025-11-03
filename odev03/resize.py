import cv2 

carimage = cv2.imread("bugatti-centodieci.jpg")

cv2.imshow("Car Image", carimage)
cv2.waitKey(0)


cv2.imwrite("araba.jpg", carimage)

gray_carimage = cv2.cvtColor(carimage, cv2.COLOR_BGR2GRAY)

resized_gray_carimage = cv2.resize(gray_carimage, (800, 600))

cropped_image = resized_gray_carimage[200:600, 100:500]

cv2.imshow("Car Image", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows




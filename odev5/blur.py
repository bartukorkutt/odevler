import cv2 

carimage = cv2.imread("bugatti-centodieci.jpg")

cv2.imshow("Car Image", carimage)
cv2.waitKey(0)


cv2.imwrite("araba.jpg", carimage)

gray_carimage = cv2.cvtColor(carimage, cv2.COLOR_BGR2GRAY)

resized_gray_carimage = cv2.resize(gray_carimage, (800, 600))

cropped_image = resized_gray_carimage[200:600, 100:500]

cropped_image_tobgr = cv2.cvtColor(cropped_image, cv2.COLOR_GRAY2BGR)

cropped_image_tobgr[200:300, 200:300] = (0,255,255)

cv2.imshow("Car Image2",cropped_image_tobgr)
cv2.waitKey(0)

cropped_image_gray = cv2.cvtColor(cropped_image[200:300, 200:300], cv2.COLOR_GRAY2BGR)

cropped_image_tobgr[200:300, 200:300] = cropped_image_gray

cropped_image_tobgr[200:300, 200:300] = cv2.blur(cropped_image_tobgr[200:300, 200:300],(20,20))

cv2.imshow("Car Image3", cropped_image_tobgr)
cv2.waitKey(0)
cv2.destroyAllWindows




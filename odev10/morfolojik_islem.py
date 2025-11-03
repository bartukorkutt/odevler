import cv2
import numpy as np

yaprak = cv2.imread("yaprak.jpg")
gray_yaprak = cv2.cvtColor(yaprak, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray_yaprak, 0,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(thresh,kernel,iterations = 1)
dilate = cv2.dilate(thresh,kernel,iterations = 1)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)

cv2.imshow("erosion",erosion)
cv2.imshow("dilate",dilate)
cv2.imshow("opening",opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

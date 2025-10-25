import cv2 

yaprak = cv2.imread("yaprak.jpg")

gray_yaprak = cv2.cvtColor(yaprak, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray_yaprak, 127,255, cv2.THRESH_BINARY)

cv2.imshow("Threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

yaprak = cv2.imread("yaprak.jpg")
gri_yaprak = cv2.cvtColor(yaprak,cv2.COLOR_BGR2GRAY)
gri_yaprak = cv2.cvtColor(gri_yaprak,cv2.COLOR_GRAY2BGR)

fark = cv2.absdiff(yaprak,gri_yaprak)

cv2.imshow("kiyasalama",fark)
cv2.waitKey(0)
cv2.destroyAllWindows()

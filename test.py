import cv2 as cv

src = cv.imread("/home/dey/Desktop/深度截图_dde-file-manager_20190112225003.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
cv.waitKey(0)
cv.destroyAllWindows()
print("hi")
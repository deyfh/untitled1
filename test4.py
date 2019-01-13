import cv2 as cv
import numpy as np


def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BAYER_BG2BGR)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb",ycrcb)


src = cv.imread("/home/dey/Desktop/深度截图_dde-file-manager_20190112225003.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
cv.waitKey(0)
cv.destroyAllWindows()
print("hi")
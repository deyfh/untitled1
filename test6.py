import cv2 as cv
import numpy as np


def add_dempo(m1,m2):
    #dst = cv.add(m1,m2)#相加
    #dst = cv.subtract(m1,m2)#相减
    #dst = cv.divide(m1,m2)#相除
    dst = cv.multiply(m1,m2)#相乘
    cv.imshow("dst",dst)


def others(m1,m2):
    M1=cv.mean(m1)#各通道的均值 判断色调？
    M2=cv.mean(m2)
    m=cv.meanStdDev(m1)#各通道方差 对比度？图像是否有用？
    print(M1)
    print(M2)
    print(m)


src1 = cv.imread("/home/dey/Desktop/IMG_20180903_172249.jpg")
src2 = cv.imread("/home/dey/Desktop/IMG_20180223_152935.jpg")
#cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image1",src1)
cv.imshow("input image2",src2)
print(src1.shape)
print(src2.shape)
#add_dempo(src1,src2)
others(src1,src2)


cv.waitKey(0)
cv.destroyAllWindows()
print("hi")
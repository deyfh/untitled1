import cv2 as cv
import numpy as np



def logic_demo(m1,m2):
    dst = cv.bitwise_not(m1,m2)#非
    dst = cv.bitwise_or(m1, m2)#像素或
    dst = cv.bitwise_and(m1, m2)#与
    dst = cv.bitwise_xor(m1, m2)#亦或
    cv.imshow("dst",dst)



src1 = cv.imread("/home/dey/Desktop/IMG_20180903_172249.jpg")
src2 = cv.imread("/home/dey/Desktop/IMG_20180223_152935.jpg")

cv.imshow("input image1",src1)
cv.imshow("input image2",src2)

print(src1.shape)
print(src2.shape)

logic_demo(src1,src2)


cv.waitKey(0)
cv.destroyAllWindows()
print("hi")
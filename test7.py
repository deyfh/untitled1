import cv2 as cv
import numpy as np


def logic_demo(m1,m2):
    dst = cv.bitwise_not(m1,m2)#非
    dst = cv.bitwise_or(m1, m2)#像素或
    dst = cv.bitwise_and(m1, m2)#与
    dst = cv.bitwise_xor(m1, m2)#亦或
    cv.imshow("dst",dst)


def contrast_brightness_demo(image,c,b):
    #c 对比度   b 亮度
    h,w,ch=image.shape
    blank=np.zeros([h,w,ch], image.dtype)
    dst=cv.addWeighted(image,c,blank,1-c,b)
    #（要加权的数组1，权重，要加权的数组2，权重，输出的数组）
    cv.imshow("con_bri_demo",dst)


src1 = cv.imread("/home/dey/Desktop/IMG_20180903_172249.jpg")
src2 = cv.imread("/home/dey/Desktop/IMG_20180223_152935.jpg")

cv.imshow("input image1",src1)
#cv.imshow("input image2",src2)

#print(src1.shape)
#print(src2.shape)

#logic_demo(src1,src2)
contrast_brightness_demo(src1,1.2,20)

cv.waitKey(0)
cv.destroyAllWindows()
print("hi")
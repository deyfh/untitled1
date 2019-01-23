import cv2 as cv
import numpy as np


def blur_demo(image):
    #均值模糊 (5,5)区域内的像素取均值
    dst = cv.blur(image, (5,5))
    cv.imshow("blur_demo",dst)


def median_demo(image):
    #中值模糊 去除椒盐噪声（黑白点）该函数使用具有ksize*ksize孔径大小的中值滤波器来平滑图像
    dst = cv.medianBlur(image, 5)
    cv.imshow("blur_demo",dst)


def custom_blur_demo(image):
    #自定义模糊
    #kernel = np.ones([5,5],np.float32)/25
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], np.float32)#锐化？
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("blur_demo",dst)


src = cv.imread("/home/dey/Desktop/深度截图_dde-file-manager_20190112225003.png")
cv.imshow("input image",src)

custom_blur_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
print("hi")
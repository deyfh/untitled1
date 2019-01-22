import cv2 as cv
import numpy as np


def fill_color_demo(image):
    # 泛洪填充：即指定图中某一像素点，以该像素点为基准点，设置像素值的上限与下限
    #          所有处于上下限范围内的像素，都会被填充为指定的新颜色
    copyimage = image.copy()
    h, w = image.shape[ :2]
    mask = np.zeros([h+2,w+2], np.uint8)
    cv.floodFill(copyimage,mask,(30,30),(0,255,255),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo", copyimage)
    ''' 
    # 调用泛洪填充时，只有mask参数中像素值为0的区域才会被填充，为了覆盖整个图像，mask 区域必须要比填充的图像大2个像素 
    FLOODFILL_FIXED_RANGE- 改变图像，泛洪填充
    floodFill(image,mask,seedPoint,newVal,rect,loDiff,upDiff,flags)   
    seedPoint:种子像素，填充的起始点像素   
    newVal：要填充的颜色   
    loDiff:规定像素值的下限
    upDiff:规定像素值的上限   
    seedPoint.BGR - loDiff <= 被填充像素值 <= seedPoint.BGR + upDiff
    即 seedPoint的BGR各减去loDiff <= 要填充的颜色范围 <= seedPoint的BGR各加上upDiff
    '''



def fill_binary():
    #二值填充： 通过限定mask中像素值为0的区域来规定填充区域。
    image = np.zeros([400,400,3],np.uint8)
    # 在进行二值填充是  mask层必须全部初始化为1 想填充的区域 初始化为0
    image[100:300,100:300,:] = 255
    cv.imshow("fill_binary",image)
    mask = np.ones([402,402,1],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image,mask,(200,200),(0,0,255),cv.FLOODFILL_MASK_ONLY)
    # FLOODFILL_MASK_ONLY - 不改变图像，只填充遮罩层本身，忽略新的颜色值参数
    cv.imshow("filled_binary",image)




src = cv.imread("/home/dey/Desktop/深度截图_选择区域_20190122223136.png")
cv.imshow("input image",src)

#fill_color_demo(src)
"""
#获取ROI
face = src[200:500, 100:300]#ROI :range of interest
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[200:500, 100:300] = backface
cv.imshow("face",src)
"""

fill_binary()
cv.waitKey(0)
cv.destroyAllWindows()
print("hi")
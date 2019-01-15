import cv2 as cv
import numpy as np


def extrace_object_demo():
    #转换到hsv色彩空间并提取某种颜色
    capture= cv.VideoCapture("/home/dey/Desktop/VID_20180712_152914.mp4")
    while(True):
        ret, frame=capture.read()
        if ret == False:
            break
        hsv=cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv=np.array([100,43,46])#提取hsv色彩空间中的特定颜色的数组上下界
        upper_hsv=np.array([124,255,255])
        mask=cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)#inrage 提取
        dst = cv.bitwise_and(frame,frame,mask=mask)#只显示某一颜色
        cv.imshow("video", frame)
        cv.imshow("video", dst)
        c=cv.waitKey(40)
        if c==27:
            break



src = cv.imread("/home/dey/Desktop/深度截图_dde-file-manager_20190112225003.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)


b, g, r=cv.split(src)#将三通道分离
cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)

src[:, :, 2]= 0#将第二通道赋值为0
cv.imshow("12",src)

merge = cv.merge([b,g,r])#混合三个通道
cv.imshow("merge",merge)

extrace_object_demo()
cv.waitKey(0)
cv.destroyAllWindows()
print("hi")
import cv2 as cv
import numpy as np


def get_image_info_(image): #函数前后空两行
    print(type(image))
    print(image.shape)#长宽通道
    print(image.size)#总像素
    print(image.dtype)#通道类型
    pixel_data = np.array(image)
    print(pixel_data)


def video_demo():
    # 摄像头捕获视频
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c >=0 : # if c == 27: #ascall 27？ ESC
            break



src = cv.imread("/home/dey/Desktop/深度截图_dde-file-manager_20190112225003.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
# 显示
# get_image_info_(src)
# cv.imwrite("/home/dey/Desktop/asda.jpg",src)#另存
cv.startWindowThread()
video_demo()


cv.waitKey(0)#延时等待 任意键关闭窗口
cv.destroyAllWindows()
print("hi")

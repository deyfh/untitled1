import cv2 as cv
import numpy as np


def access_pixeal(image):
    print(image.shape)
    height=image.shape[0]
    width=image.shape[1]
    channels=image.shape[2]
    print("width:%s, height:%s,channels:%s"%(width,height,channels))#输出
    for r in range(height):
        for s in range(width):
            for t in range(channels):
                pv = image[r,s,t]
                image[r,s,t] = 255-pv
    cv.imshow("pixel_demo",image)


def create_image():
    img=np.zeros([400,400,3],np.uint8)#三维数组0.0.0
    img[:,:,2] =np.ones([400,400])*255#三通道分别是 bgr 012
    cv.imshow("create",img)
    """
    #灰度 单通道
    img2=np.zeros([400,400,1],np.uint8)#1维数组0
    img2[:,:,0] =np.ones([400,400])*255
    cv.imshow("create2",img2)
    cv.imwrite("////asd.png",img)    
    """
    m1 = np.ones([3,3],np.uint8)
    m1.fill(156.5546289)
    print(m1)
    m2 = m1.reshape([1,9])
    print(m2)


src = cv.imread("/home/dey/Desktop/深度截图_dde-file-manager_20190112225003.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
t1=cv.getTickCount()
#access_pixeal(src)
create_image()
t2=cv.getTickCount()
time=((t2-t1)/cv.getTickFrequency())*1000
print("time: %s ms"%time)


cv.waitKey(0)
cv.destroyAllWindows()
print("hi")
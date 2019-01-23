import cv2 as cv
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    #产生高斯噪声
    h, w, c=image.shape
    for row in range(0,h,1):
        for col in range(w):
            s = np.random.normal(0,20,3)
            #numpy.random.normal(loc=0.0, scale=1.0, size=None)
            #loc：此概率分布的均值（对应着整个分布的中心centre）
            #scale：此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
            #size：输出的shape，默认为None，只输出一个值
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise_image", image)
    dst = cv.GaussianBlur(image, (5, 5), 15)
    cv.imshow("GAUSS_D", dst)


src = cv.imread("/home/dey/Desktop/深度截图_dde-file-manager_20190112225003.png")
cv.imshow("input image",src)
'''
t1 = cv.getTickCount()
gaussian_noise(src)
t2 = cv.getTickCount()
time = (t2 - t1)/cv.getTickFrequency()
print("time_comsume=%dms"%(time*1000))
'''
dst = cv.GaussianBlur(src, (5,5), 0)
cv.imshow("GAUSS", dst)
#高斯模糊对高斯噪声有一定抑制作用

gaussian_noise(src)
cv.waitKey(0)
cv.destroyAllWindows()
print("hi")
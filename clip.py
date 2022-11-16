# 导入cv模块
 
import cv2 as cv
import numpy as np
 
 
# 读取图像，支持 bmp、jpg、png、tiff 等常用格式
# 第二个参数是通道数和位深的参数，有四种选择，参考https://www.cnblogs.com/goushibao/p/6671079.html
# 1彩色2灰度
 
img_A = cv.imread(r"E:\Datasets\shaoxing\bhfx1\bhfx1\fw1_2020.tif", 1)
img_B = cv.imread(r"E:\Datasets\shaoxing\bhfx1\bhfx1\fw1_2021.tif", 1)
h,w=img_A.shape[0],img_A.shape[1]
# m,n=range(0,h,1024),range(0,w,1024)
n=0
for i in range(0,h,1024):
    for j in range(0,w,1024): 
        end_i,end_j=min(h,i+1024),min(w,j+1024)      
        cropped_A = img_A[i:end_i, j:end_j] 
        cropped_B = img_B[i:end_i, j:end_j]  
        cv.imwrite(r"E:/Datasets/shaoxing/bhfx1/bhfx1/cropped/A/"+str(n)+".jpg", cropped_A)
        cv.imwrite(r"E:/Datasets/shaoxing/bhfx1/bhfx1/cropped/B/"+str(n)+".jpg", cropped_B)
        n+=1

# print(img)
# print(img.shape)
# print(img.dtype)
# print(img.min())
# print(img.max())
 
# 创建窗口并显示图像
'''
cv.namedWindow("image", cv.WINDOW_NORMAL)
cv.imshow("image", img)
cv.waitKey(0)
# 释放窗口
cv.destroyAllWindows()
'''
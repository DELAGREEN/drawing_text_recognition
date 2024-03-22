import cv2
import numpy as np

img = cv2.imread('D:\REP\projects\drawing_text_recognition\images\sxema65-1.png')
#new_image = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2)) #Изменение размера изображения, первый параметр ширина, второй высота
#new_image = cv2.Canny(new_image, 90, 90)   #контуры 
print(img.shape) #Размер изображения 

crop_img = img[img.shape[0] - 1200:img.shape[0] - 470, img.shape[1] - 1200:img.shape[1]-200] #Вырезать определенную область

gray_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) #картинка в сером цвете, что бы убрать слои RGB

ret, thresh = cv2.threshold(gray_img, 0, 255, cv2.ADAPTIVE_THRESH_MEAN_C)
#print('ret', ret)
#print('tresh', thresh)

img_erode = cv2.erode(thresh, np.ones((1, 1), np.uint8), iterations=1)

contours, hierarchy = cv2.findContours(img_erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

output = crop_img.copy()

def _contours():
    for idx, contour in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(contour)
        #print("R", idx, x, y, w, h, cv2.contourArea(contour), hierarchy[0][idx])
        # hierarchy[i][0]: the index of the next contour of the same level
        # hierarchy[i][1]: the index of the previous contour of the same level
        # hierarchy[i][2]: the index of the first child
        # hierarchy[i][3]: the index of the parent
        if hierarchy[0][idx][3] == 0:
            cv2.rectangle(output, (x, y), (x + w, y + h), (57, 255, 20), 1)
_contours()
cv2.imshow('Result_ret', ret)
cv2.imshow('Result', output)
cv2.imshow('Result_tresh', thresh)
cv2.imshow('Result_img_erode', img_erode)
cv2.waitKey(0)
import cv2
import numpy

img = cv2.imread('D:\REP\projects\drawing_text_recognition\images\sxema65-1.jpg')
#new_image = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2)) #Изменение размера изображения, первый параметр ширина, второй высота
#new_image = cv2.Canny(new_image, 90, 90)   #контуры 
print(img.shape) #Размер изображения 

crop_img = img[img.shape[0] - 1200:img.shape[0] - 470, img.shape[1] - 1200:img.shape[1]-200] #Вырезать определенную область
new_image = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) #картинка в сером цвете, что бы убрать слои RGB
ret, thresh = cv2.threshold(new_image, 0, 255, cv2.THRESH_BINARY)
print('ret', ret)
print('tresh', thresh)

img_erode = cv2.erode(thresh, numpy.ones((3, 3), numpy.uint8), iterations=1)

contours, hierarchy = cv2.findContours(new_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

output = crop_img.copy()

def _contours():
    for idx, contour in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(contour)
        print("R", idx, x, y, w, h, cv2.contourArea(contour), hierarchy[0][idx])
        # hierarchy[i][0]: the index of the next contour of the same level
        # hierarchy[i][1]: the index of the previous contour of the same level
        # hierarchy[i][2]: the index of the first child
        # hierarchy[i][3]: the index of the parent
        if hierarchy[0][idx][3] == 0:
            cv2.rectangle(output, (x, y), (x + w, y + h), (57, 255, 20), 1)
_contours()

cv2.imshow('Result', output)
cv2.waitKey(0)
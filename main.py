import cv2
import numpy
import test_pytesseract

img = cv2.imread('D:\REP\projects\drawing_text_recognition\images\sxema65-1.jpg')
#new_image = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2)) #Изменение размера изображения, первый параметр ширина, второй высота
#new_image = cv2.Canny(new_image, 90, 90)   #контуры 
#print(img.shape) #Размер изображения 

crop_img = img[img.shape[0] - 1200:img.shape[0] - 470, img.shape[1] - 1200:img.shape[1]-200] #Вырезать определенную область
#print(crop_img.shape)

new_image = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) #картинка в сером цвете, что бы убрать слои RGB

ret, thresh = cv2.threshold(new_image, 0, 255, cv2.THRESH_BINARY)
#print('ret', ret)
#print('tresh', thresh)

img_erode = cv2.erode(new_image, numpy.ones((1, 1), numpy.uint8), iterations=1)

contours, hierarchy = cv2.findContours(img_erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

output = crop_img.copy()

def _contours():
    for idx, contour in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(contour)
        #print("R", idx, x, y, w, h, cv2.contourArea(contour), hierarchy[0][idx])
   
        if hierarchy[0][idx][3] == 0:

            cv2.rectangle(output, (x, y), (x + 50, y + 50), (57, 255, 20), 1)

        #cv2.rectangle(output, (215, 319), (215 + 14, 319 + 14), (57, 255, 20), 1)
#_contours()

test_pytesseract.test_pytesseract.tesseract_cmd = 'D:\\REP\projects\\drawing_text_recognition\\tesseract\\tesseract.exe'

tes_img = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

print(test_pytesseract.image_to_string(tes_img, lang='num'))
#print(pytesseract.image_to_boxes(tes_img))
cv2.imshow('Result', output)
cv2.waitKey(0)
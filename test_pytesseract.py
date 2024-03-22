import cv2
import numpy
import pytesseract

img = cv2.imread('D:\REP\projects\drawing_text_recognition\images\sxema65-1.jpg')
#img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
print(img.shape)
#cv2.imshow('img', img)
crop_img = img[img.shape[0] - 1200:img.shape[0] - 470, img.shape[1] - 1200:img.shape[1]-200] #Вырезать определенную область
print(crop_img.shape)
img_h, img_w, *args = crop_img.shape
pytesseract.pytesseract.tesseract_cmd = 'D:\\REP\projects\\drawing_text_recognition\\tesseract\\tesseract.exe'

tes_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(tes_img, lang='num'))
#print(pytesseract.image_to_boxes(tes_img))
boxes= pytesseract.image_to_boxes(tes_img)
for data_set in boxes.splitlines():
    data = data_set.split(' ')
    word, x, y, w, h,*args = data
    #print(x, y, w, h)
    cv2.rectangle(crop_img, (int(x),  img_h - int(y)), (int(w), img_h - int(h)), (57, 255, 20), 1)
    #cv2.imshow(word, crop_img[int(x) : img_h + int(y), int(w) : img_h + int(h)]) 
    #cv2.waitKey(0)
#print(data_set_list)
cv2.imshow('Result', crop_img)
print(type(crop_img))
cv2.waitKey(0)
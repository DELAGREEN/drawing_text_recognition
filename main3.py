import imutils
import cv2
from matplotlib import pyplot as pl
import numpy as np
img = cv2.imread('D:\REP\projects\drawing_text_recognition\images\sxema65-1.jpg')
crop_img = img[img.shape[0] - 1200:img.shape[0] - 470, img.shape[1] - 1200:img.shape[1]-200] #Вырезать определенную область
gray = cv2.cvtColor(crop_img, cv2.COLOR_BAYER_BG2GRAY)
img_filter = cv2.bilateralFilter(gray, 11,15,15)
edges = cv2.Canny(img_filter, 30,200)

count = cv2.findContours(edges.copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
count = imutils.grab_contours(count)
pos = None
for c in count:
        approx = cv2.approxPolyDP(c, 5, True)

        if len(approx) == 4:
                pos = approx
                break

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask)
pl.imshow(cv2.cvtColor(bitwise_img, cv2.COLOR_BGR2RGB))
pl.show()

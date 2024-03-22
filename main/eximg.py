from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import cv2
import numpy
import icecream
import pytesseract



##def convert_pdf_to_tiff(input_pdf, output_folder):
##    convert_from_path(input_pdf, output_folder= output_folder)
##    #pages = convert_pdf_to_tiff(input_pdf)
##    #for page in pages:
##    #    im = Image.open(page)
##    #    filename = f"{output_folder}{im.format}.tiff"
##    #    im.save(filename)
##
### Пример использования
##input_pdf = "D:\\REP\\projects\\drawing_text_recognition\\pdf\\001сб.dwg.pdf"
##output_folder = "D:\\REP\\projects\\drawing_text_recognition\\main"
##convert_pdf_to_tiff(input_pdf=input_pdf, output_folder=output_folder)

pytesseract.pytesseract.tesseract_cmd = 'D:\\REP\projects\\drawing_text_recognition\\tesseract\\tesseract.exe'

def convert_pdf_to_tiff(path):
    #pages = convert_from_path(path, dpi=300, poppler_path="D:\\REP\\projects\\drawing_text_recognition\\main\\poppler-24.02.0\\Library\\bin")
    pages1 = convert_from_path(path, dpi=300, 
                               #output_folder="D:\\REP\\projects\\drawing_text_recognition\\main", 
                                poppler_path="D:\\REP\\projects\\drawing_text_recognition\\main\\poppler-24.02.0\\Library\\bin", fmt="png")
    print(len(pages1))
    print(type(pages1))
    print(type(pages1[0]))
    img = numpy.array(pages1[0])
    print(type(img))
    #img=cv2.imread(pages1[0])
    #img_np = cv2.imdecode(img)
    #img1 = cv2.imread(img)
    #print(f"img type: {type(img1)}")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #print(img_rgb)
    #print(pytesseract.image_to_string(img))
    print(type(img_rgb))
    print(pytesseract.image_to_string(img_rgb, "num"))
    #print(pytesseract.pytesseract.image_to_string(image=img_rgb, lang="num"))

    cv2.imshow('Result', img)
    cv2.waitKey(0) 
   # for page in pages:
   #
   #      Image.open(page).save(f"{path.stem}.tif")

path = 'D:\\REP\\projects\\drawing_text_recognition\\pdf\\001сб.dwg.pdf'
convert_pdf_to_tiff(path)

#images = convert_from_path('D:\\REP\\projects\\drawing_text_recognition\\pdf\\001сб.dwg.pdf', poppler_path='D:\\REP\\projects\\drawing_text_recognition\\main\\poppler-24.02.0\\Library\\bin')
#print(images[0])
#print(len(images))
#for i in images:
#    Image.open(i, 'r').save('D:\\REP\\projects\\drawing_text_recognition\\main\\tmp1.tiff')

#import tempfile
#
#with tempfile.TemporaryDirectory() as path:
#    images_from_path = convert_from_path('D:\\REP\\projects\\drawing_text_recognition\\pdf\\001сб.dwg.pdf', output_folder='D:\\REP\\projects\\drawing_text_recognition\\main', 
#                                         poppler_path="D:\\REP\\projects\\drawing_text_recognition\\main\\poppler-24.02.0\\Library\\bin")    

import argvparser
import sys
import cv2
import numpy
#from pdf2image import convert_from_path
import PyPDF2
from pdf2image import convert_from_path

if  len(sys.argv) > 1:
    print(f'lenght: {len(sys.argv)}')
    parser = argvparser.argvparser.parse(sys.argv)
    options = parser['options']
    print(options)

#if "-t" or "--t" in options:
#    print("is T")
#elif "-f"  or "--f"in options:
#    print("is F")


#pdf_file = open('D:\\REP\\projects\\drawing_text_recognition\\pdf\\001сб.dwg.pdf', 'rb')
#pdf_reader = PyPDF2.PdfReader(pdf_file)
#for page_num in range(pdf_reader.numPages):
#    page = pdf_reader.getPage(page_num)
#    images = page.extract_images()

import PyPDF2

pdf_file = open('D:\\REP\\projects\\drawing_text_recognition\\pdf\\001сб.dwg.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

for page_num in range(pdf_reader.pages):
    page = pdf_reader.getPage(page_num)
    images = page.extract_images()


    
    for image_num, image in enumerate(images):
        image_data = image[0]['image']
#print(page)
        img = cv2.imread(image_data)
        cv2.imshow('Result', img)
cv2.waitKey(0)




#import glob
#import re
#
#infiles = glob.glob('D:\REP\projects\drawing_text_recognition\pdf')
#
#for infile in infiles:
#    print(f'infile: {infile}')
#    #outfile = re.sub("pdf$", "TIFF", infile)
#    #print(outfile)


class Convert_To_Tiff():

    def __init__(self) -> None:
        _path_to_pdf = options['-path_to_pdf']
        
    def from_pdf():
        pass
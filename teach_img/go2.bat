
echo Run 
D:\REP\projects\drawing_text_recognition\tesseract\tesseract.exe num.font.exp0.png num.font.exp0 --psm 6 -l rus lstm.train


echo Run

D:\REP\projects\drawing_text_recognition\tesseract\combine_tessdata.exe -e "D:\\REP\\projects\\drawing_text_recognition\\tesseract\\tessdata\\rus.traineddata" rus.lstmf

D:\REP\projects\drawing_text_recognition\tesseract\unicharset_extractor.exe --output_unicharset my.unicharset --norm_mode 2 num.font.exp0.box



echo. & pause
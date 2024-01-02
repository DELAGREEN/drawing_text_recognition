rem Создайте файл font_properties в каталоге перед выполнением пакетного процесса 

echo Run Tesseract for Training.. 
D:\REP\projects\drawing_text_recognition\tesseract\tesseract.exe num.font.exp0.png num.font.exp0.box nobatch box.train  
 
echo Compute the Character Set.. 
D:\REP\projects\drawing_text_recognition\tesseract\unicharset_extractor.exe num.font.exp0.box 
D:\REP\projects\drawing_text_recognition\tesseract\mftraining.exe -F font_properties -U unicharset -O num.unicharset num.font.exp0.box.tr 

echo Clustering.. 
D:\REP\projects\drawing_text_recognition\tesseract\cntraining.exe num.font.exp0.box.tr 

echo Rename Files.. 
rename normproto num.normproto 
rename inttemp num.inttemp 
rename pffmtable num.pffmtable 
rename shapetable num.shapetable  

echo Create Tessdata.. 
D:\REP\projects\drawing_text_recognition\tesseract\combine_tessdata.exe num 

echo. & pause
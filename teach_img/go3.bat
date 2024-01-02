
echo Run 
D:\REP\projects\drawing_text_recognition\tesseract\tesseract.exe num.font.exp0.tif num.font.exp0 --psm 6 lstm.train

D:\REP\projects\drawing_text_recognition\tesseract\combine_tessdata.exe -e "rus.traineddata" rus_f.lstm

D:\REP\projects\drawing_text_recognition\tesseract\lstmtraining.exe --model_output="D:\REP\projects\drawing_text_recognition\teatch_img" --continue_from="D:\REP\projects\drawing_text_recognition\teatch_img\rus_f.lstm" --train_listfile="D:\REP\projects\drawing_text_recognition\teatch_img\num.training_files.txt" --traineddata="rus.traineddata" --debug_interval -1 --max_iterations 800




echo. & pause
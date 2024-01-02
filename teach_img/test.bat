
echo Run 

lstmtraining 
	--model_output output\ 
  	--continue_from rus_f.lstm
  	--old_traineddata D:\REP\projects\drawing_text_recognition\tesseract\tessdata\rus.traineddata 
  	--traineddata train/rus/rus.traineddata 
  	--train_listfile train/rus.training_files.txt 
  	--eval_listfile eval/rus.training_files.txt 
  	--U train/my.unicharset 
  	--max_iterations 140000

echo. & pause
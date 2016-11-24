chmod +x run.sh
tar czvf kaggle_assignment.tar.gz run.sh CNNDigitRecognizer.py
base64 kaggle_assignment.tar.gz > kaggle_assignment.tar.gz.b64
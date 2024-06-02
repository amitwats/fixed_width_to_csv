'''
python -m venv venv
venv\Scripts\activate
deactivate

venv\Scripts\python main.py
venv\Scripts\python -m pip install --upgrade pip
venv\Scripts\python -m pip install -r requirements.txt


'''


from parser.fw_2_csv_parser import FW2CSVParser
from configs.config import INPUT_FILE_PATH, OUTPUT_FILE_PATH, SPECIFICATIONS_FILE 

if __name__=="__main__":
    # sp=FW2CSVParser.from_json(SPECIFICATIONS_FILE)
    # sp.parse_fw_to_csv(INPUT_FILE_PATH,OUTPUT_FILE_PATH)
    




    
from parser.fw_2_csv_parser import FW2CSVParser
import os
import shutil

def create_file_with_content(file_path: str, content: str):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def create_file_with_list(file_path,content):
    with open(file_path, 'w', encoding='utf-8') as file:
        for row in content:
            file.write( row + '\n')

def read_file_content(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def test_fw_parser():
    tmp_folder_path = './tmp'
    input_file_name=os.path.join(tmp_folder_path,"input.txt")
    output_file_name=os.path.join(tmp_folder_path,"output.csv")
    specs_file_name=os.path.join(tmp_folder_path,"specs.json")

    specs_content='{"ColumnNames":["Name","Age","City"], "Offsets":[10, 3, 15], "FixedWidthEncoding":"utf-8", "IncludeHeader":"True", "DelimitedEncoding":"utf-8"}'

    input_content=["John Doe  023New York       ",
                "Jane Doe  015New Jersey     ",
                "Bon Jovie 053California     "]

    expected_output_content="Name,Age,City\n"+\
                            "John Doe,023,New York\n"+\
                            "Jane Doe,015,New Jersey\n"+\
                            "Bon Jovie,053,California\n"

    if not os.path.exists(tmp_folder_path):
        os.makedirs(tmp_folder_path)

    create_file_with_content(specs_file_name,specs_content)
    create_file_with_list(input_file_name,input_content)
    parser=FW2CSVParser.from_json(specs_file_name)
    parser.parse_fw_to_csv(input_file_name,output_file_name)
    actual_output=read_file_content(output_file_name)
    assert expected_output_content==actual_output
    shutil.rmtree(tmp_folder_path)
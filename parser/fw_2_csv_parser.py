import csv
import json
import os
from typing import List


class FW2CSVParser:
    def __init__(self, column_names:List[str], offsets:List[int], fixed_width_encoding:str, include_header:bool, delimited_encoding:str):
        """
        Args:
            column_names (List[str]): List of all column names got from the json specs.
            offsets (List[int]):  List of all column offsets got from the json specs.
            fixed_width_encoding (str): The encoding of the input file
            include_header (bool): A boolean value specifying to include headers in the CSV files or not.
            delimited_encoding (str): The encoding of the output CSV file.

        Raises:
            ValueError: In case the number of columns do not match the number of offsets specified an error is thrown.
        """

        self.column_names:List[str] = column_names
        self.offsets:List[int] = offsets
        self.fixed_width_encoding:str = fixed_width_encoding
        self.include_header:bool = include_header
        self.delimited_encoding:str = delimited_encoding
        if len(self.column_names)!=len(self.offsets):
            raise ValueError(f"The length of columns is {len(self.column_names)} \
                             and offsets is {len(self.offsets)}. They should be the same.")

    @staticmethod
    def from_json(file_path:str): # type: ignore
        """
        Create the object from a json file

        Args:
            file_path (str): The json specs file path

        Raises:
            FileNotFoundError: Thrown when an invalid path is specified

        Returns:
            FW2CSVParser: An object of the class.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file at path '{file_path}' does not exist.")
        else:
            with open(file_path, 'r') as file:
                data = json.load(file)
            column_names = data.get('ColumnNames', [])
            offsets = data.get('Offsets', [])
            offsets=list(map(lambda x:int(x), offsets))
            fixed_width_encoding = data.get('FixedWidthEncoding', '')
            include_header = data.get('IncludeHeader', '') == 'True'
            delimited_encoding = data.get('DelimitedEncoding', '')
            specs=FW2CSVParser(column_names, offsets, fixed_width_encoding, include_header, delimited_encoding)
            return specs

    def parse_fw_to_csv(self,input_file_path:str,output_file_path:str):
        """
        This method parses an input fixed width file to a CSV file.

        Args:
            input_file_path (str): The path of the input fixed width file
            output_file_path (str): The path of the output csv file
        """
        with open(input_file_path, 'r',encoding=self.fixed_width_encoding) as input_file:
            with open(output_file_path, 'w', newline="", encoding=self.delimited_encoding) as output_file:
                writer=csv.writer(output_file)
                if self.include_header:
                    writer.writerow(self.column_names)
                line = input_file.readline()
                while line:
                    csv_row=self.convert_row_to_fields(line)
                    writer.writerow(csv_row)
                    line = input_file.readline()

    def get_column_offset(self, column_name:str)->int:
        """
        Returns the corresponding offset associated with a column name

        Args:
            column_name (str): The name of the column for which the offset is required.

        Returns:
            int: The offset of the column. 
        """
        index=self.column_names.index(column_name)
        return self.offsets[index]

    def get_row_length(self)->int:
        """
        The length of the row of the fixed width file.

        Returns:
            int: The length of the row of the fixed width file.
        """
        return sum(self.offsets)

    def convert_row_to_fields(self, row_str:str)->List[str]:
        """
        Extracts the field values from a fixed width row.

        Args:
            row_str (str): The row as read from he fixed width file

        Raises:
            ValueError: If the row length is not as specified in the specs an error is thrown.

        Returns:
            List[str]: Extracts the field values from a fixed width row. Returns a list of field values.
        """
        if len(row_str)!=self.get_row_length():
            raise ValueError(f"The length of the row should be {self.get_row_length()} instead it is {len(row_str)}")
        last_index=0
        data_list=[]
        for column_name in self.column_names:
            offset=self.get_column_offset(column_name)
            data:str=row_str[last_index:last_index+offset]
            data_list.append(data.strip())
            last_index=last_index+offset

        return data_list

    def __repr__(self):
        return (f"FW2CSVParser(column_names={self.column_names}, offsets={self.offsets}, "
                f"fixed_width_encoding={self.fixed_width_encoding}, include_header={self.include_header}, "
                f"delimited_encoding={self.delimited_encoding})")
from faker import Faker
from abc import ABC, abstractmethod
from typing import Any
from datetime import datetime

class DataSpec(ABC):
    @staticmethod
    def convert_to_length(obj:Any,length:int):
        typ=type(obj)
        str_obj=str(obj)
        if len(str_obj)>length:
            str_obj=str_obj[:length]

        match typ:
            case "int":
                converted_obj = str_obj.rjust(length)
                return converted_obj
            case _:
                converted_obj = str_obj.ljust(length)
                return converted_obj
            
    @abstractmethod
    def get_fw_data(self):
        pass


{
    "ColumnNames": [
        "Name",
        "id",
        "address",
        "data_of_birth",
        "phone_number",
        "gender",
        "amount",
        "transaction_date",
    ],
    "Offsets": [
        20,
        12,
        80,
        11,
        30,
        15,
        8,
        10,
    ],
    "FixedWidthEncoding": "windows-1252",
    "IncludeHeader": "True",
    "DelimitedEncoding": "utf-8"
}

class DataSpecPurchaseHistory(DataSpec):
    def __init__(self,name:str,id:int, address:str,data_of_birth:str,phone_number:str,gender:str,amount:int, transaction_date:str) -> None:
        self.name=self.convert_to_length(name,20)
        self.id=self.convert_to_length(id,12)
        self.address=self.convert_to_length(address,80)
        self.data_of_birth=self.convert_to_length(data_of_birth,11)
        self.phone_number=self.convert_to_length(phone_number,30)
        self.gender=self.convert_to_length(gender,15)
        self.amount=self.convert_to_length(amount,8)
        self.transaction_date=self.convert_to_length(transaction_date,11)
    
    def get_fw_data(self):
        return self.name+ self.id+ self.address+ self.data_of_birth+ self.phone_number+ self.gender+ self.amount+ self.transaction_date
    

def generate_spec_purchase_history_row_data():
    fake = Faker()
    date_format="%d/%m/%Y"
    name=fake.name()
    id=fake.random_int(200,200000000)
    address=fake.address().replace("\n"," ")
    data_of_birth=fake.date_of_birth()
    data_of_birth=data_of_birth.strftime(date_format)
    phone_number=fake.phone_number()
    gender=fake.passport_gender()
    amount=fake.random_int(500,200000000)
    transaction_date=fake.date_time_between_dates(datetime(2020, 1, 1), datetime(2023, 12, 31))
    transaction_date=transaction_date.strftime(date_format)
    data=DataSpecPurchaseHistory(name, id, address, data_of_birth, phone_number, gender, amount, transaction_date)
    return data.get_fw_data()

def generate_data_file(file_path,row_generator_function, number_of_rows=20):
    with open(file_path, 'w') as file:
        for _ in range(number_of_rows):
            row=row_generator_function()
            file.write( row + '\n')

if __name__=="__main__":
    generate_data_file("spec_purchase_history_data.txt", generate_spec_purchase_history_row_data, 50)
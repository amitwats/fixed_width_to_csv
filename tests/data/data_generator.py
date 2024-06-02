from faker import Faker
from abc import ABC, abstractmethod
from typing import Any
from datetime import datetime
import random 
import string 

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

    @staticmethod
    @abstractmethod
    def generate_row_data():
        pass

    @classmethod
    def generate_data_file(cls,file_path,number_of_rows=20):
        with open(file_path, 'w') as file:
            for _ in range(number_of_rows):
                row=cls.generate_row_data() #row_generator_function()
                file.write( row + '\n')

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
        11,
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
    
    @staticmethod
    def generate_row_data():
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


{
    "ColumnNames": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10"
    ],
    "Offsets": [
        "5",
        "12",
        "3",
        "2",
        "13",
        "7",
        "10",
        "13",
        "20",
        "13"
    ],
    "FixedWidthEncoding": "windows-1252",
    "IncludeHeader": "True",
    "DelimitedEncoding": "utf-8"
}

class DataSpecGivenData(DataSpec):
    def __init__(self,f1:str,f2:str,f3:str,f4:str,f5:str,f6:str,f7:str,f8:str,f9:str,f10:str) -> None:
        self.f1=self.convert_to_length(f1,5)
        self.f2=self.convert_to_length(f2,12)
        self.f3=self.convert_to_length(f3,3)
        self.f4=self.convert_to_length(f4,2)
        self.f5=self.convert_to_length(f5,13)
        self.f6=self.convert_to_length(f6,7)
        self.f7=self.convert_to_length(f7,10)
        self.f8=self.convert_to_length(f8,13)
        self.f9=self.convert_to_length(f9,20)
        self.f10=self.convert_to_length(f10,13)


    def get_fw_data(self):
        return self.f1+ self.f2+self.f3+self.f4+self.f5+self.f6+self.f7+self.f8+self.f9+self.f10
    
    @staticmethod
    def generate_row_data():

        attr_len=[ 5, 12, 3, 2, 13, 7, 10, 13, 20, 13]
        fake = Faker()
        attr_values=[]
        for l in attr_len:
            if l<5: # limitation of faker that it connot generate length below 5
                letters = string.ascii_letters + string.digits + string.punctuation
                attr_values.append(''.join(random.choice(letters) for _ in range(l)) )               
            else:
                attr_values.append(fake.text(l))
        
        data= DataSpecGivenData(*attr_values)
        return data.get_fw_data()


if __name__=="__main__":
    # DataSpecPurchaseHistory.generate_data_file("input/spec_purchase_history_data.txt", 50)
    DataSpecPurchaseHistory.generate_data_file("C:\\AmitFiles\\tryStuff\\latitude_financials_coding_challenge\\coding-challenges\\coding-challenges\\P2_fixed_width\\input\\spec_purchase_history_data.txt", 50)
    # print(DataSpecGivenData.generate_row_data())
    # DataSpecGivenData.generate_data_file(r".\\a.txt",5)


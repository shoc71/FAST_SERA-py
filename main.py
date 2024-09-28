# Imports
import os

DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_TXT_DIRECTORY_PATH = f"{DIRECTORY_PATH}/assets/data/data.txt"

with open (DATA_TXT_DIRECTORY_PATH, 'r', encoding='utf-8', errors="ignore") as file:
    line = file.readline()
    main_data = eval(line) # expected return to be a single line of string

# print(f"{main_data}\n{type(main_data)}")

class Search_Data:
    pass

class Edit_Data:
    pass

class Remove_Data:
    pass

class Add_Data:
    def __init__(self, storage, keyword, user_input_keys, user_input_values) -> None:
        self.storage = storage
        self.keyword = keyword
        self.user_input_keys = user_input_keys
        self.user_input_values = user_input_values

    def add_key(storage, user_input_keys, user_input_values):
        try:
            storage[user_input_keys].append(user_input_values)
        except:
            storage[user_input_keys] = user_input_values
        
        return storage

    def add_tags(self, storage, keyword):
        pass

class Program:
    pass

Add_Data.add_key(main_data, "test", ["hi"])

print(main_data)
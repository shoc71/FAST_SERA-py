# Imports
import os

DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_TXT_DIRECTORY_PATH = f"{DIRECTORY_PATH}/assets/data/data.txt"

with open (DATA_TXT_DIRECTORY_PATH, 'r', encoding='utf-8', errors="ignore") as file:
    line = file.readline()
    main_data = eval(line) # expected return to be a single line of string



class Search_Data:
    pass

class Edit_Data:
    pass

class Remove_Data:
    pass

class Add_Data:
    def __init__(self, storage) -> None:
        self.storage = storage
        pass

    def add_key(self, user_input_keys, user_input_values):
        try:
            # If the key already exists, append the new value
            self.storage[user_input_keys].append(user_input_values)
        except KeyError:
            # If the key doesn't exist, create a new entry
            self.storage[user_input_keys] = user_input_values
        
        return self.storage

    def add_tags(self, user_input_keys, user_input_values):
        try:
            self.storage[user_input_keys].append(user_input_values)
        except KeyError:
            self.storage[user_input_keys] = [user_input_values]
        
        return self.storage

class Program:
    def __init__(self) -> None:
        # self.add_data = Add_Data() # Create an instance of Add_Data
        pass

    def log(self, string):
        return print(f"{string}")
        
    def start(self):
        OPTIONS = f"""
Welcome to the FAST SERA. [Filter Address Scoure Track - Search Edit Remove Add] Program.
We are using (local directory)
{DIRECTORY_PATH}
as your local database. 

To SERA the local database, select an option.

1. Search
2. Edit
3. Remove
4. Add
99. Quit

--> """
        start_check = input(OPTIONS)
        return start_check
    
    def check_options(self, result):
        self.log(f"YOu have selected an option. {result}")

        if result in ["4", "a", 'add', "four", "ADD", "Add"]:
            self.clear_terminal()
            self.log("You have selected the Add option.")
            
    def clear_terminal(self):
        """
        Clears the terminal screen.
        """
        # Clear command for Windows
        if os.name == 'nt':
            _ = os.system('cls')
        # Clear command for Unix/Linux/MacOS
        else:
            _ = os.system('clear')

    def main(self):
        self.clear_terminal()
        result = self.start()

        self.clear_terminal()
        self.check_options(result)

# if __name__ == "__main__":
#     program = Program()
#     program.main()
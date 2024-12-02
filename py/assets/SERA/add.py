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
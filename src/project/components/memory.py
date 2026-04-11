# Checks if Memory class has already been built and stored in the cache, if not do, if yes return
def singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class Memory:
    def __init__(self) -> None:
        self.memory:dict = dict({}) # Creates the storage
    
    def get(self, variable_name:str) -> object:
        assert variable_name in self.memory, f"Variable '{variable_name}' does not exist in Memory"
        return self.memory[variable_name]
    
    def set(self, variable_name:str, value:object, data_type:str):
        # Crash when variable name already exists in the memory
        # {'x': {'value': True, 'data_type': 'bool'}}
        assert variable_name not in self.memory, f"Variable '{variable_name}' already exists!"
        self.memory[variable_name] = {"value": value, "data_type": data_type}

    def __repr__(self) -> str:
        # formats the dictionary into a string
        string = ""
        string += f"Name\tValue\tData Type\n"
        string += "-"*30+"\n"
        for var, data in self.memory.items():
            value = data["value"]
            data_type = data["data_type"]
            string += f"{var}\t{value}\t{data_type}\n"
        string += "-"*30+"\n"
        return string

if __name__ == "__main__":
    memory = Memory()
    memory.set(variable_name='a', value=10, data_type=int)
    memory.set(variable_name='b', value="20", data_type=str)
    print(memory)
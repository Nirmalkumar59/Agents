# create a function for sample python file
from datetime import datetime
def sample(name)->str:
    return f"Hello, {name}! , DateTime :{datetime.now()}"
if __name__ == "__main__":
    name = input("Enter The Name:")
    print(sample(name))
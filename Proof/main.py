import random
"""
list1 = []
for i in range(1,101):
    list1.append(random.randint(1, 100))
print(list1)
"""
import time
import json
from dataclasses import dataclass

def timeFunction(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # Your code goes here
        end_time = time.time()
        result = func(*args, **kwargs)
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper

@timeFunction
def generateNumbers():
    list2 = [random.randint(1,100) for i in range(1, 101)]
    return list2


def formatNumbers(list1):
    result = ["Index {} Value {}".format(index, value)
          for index, value in enumerate(list1)]
    my_string_numbers = "\n".join(map(str, result))
    return  my_string_numbers

def readJsonFile():
    list_username = []
    #list_id = []
    with open("data_tracing.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in data["users"]:
            try:
                list_username.append(i["name"])
                #list_id.append(i["id"])
            except KeyError:
                pass
    return list_username#,list_id


@dataclass
class User:
    name: str
    id: int

r = readJsonFile
u = User(r[0], 0)

#readJsonFile()
#print(formatNumbers(generateNumbers()))
#print(generateNumbers())
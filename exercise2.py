import sys
import numpy as np
import random
import math
import json

numbers = [ int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6])]

op=True

while op:
    print("""
    1 - Perform subtraction and show output on screen comma separated
    2 - Perform multiplication and store result in a JSON file 
    3 - Pick randomly a number and show it on screen
    4 - Print sorted (highest to lowest) array/list numbers
    5 - Print sorted (lowest to highest) array/list numbers
    6 - Exit
    """)

    op = input ( " Option : ")
    
    if op == "1":
        subt = numbers[0]
        for item in numbers[1:]:
            print (f"{subt}-{item}=" )
            subt -= item
            print (f"{subt} , " )
    elif op == "2":
        mult = math.prod(numbers)
        print(mult)
        MultList = {"InputNumber1": int(sys.argv[1]), "InputNumber2": int(sys.argv[2]), "InputNumber3": int(sys.argv[3]),
        "InputNumber4": int(sys.argv[4]), "InputNumber5": int(sys.argv[5]), "InputNumber6": int(sys.argv[6]), 
        "Multiplication": mult}
        print(MultList)
        jsonString = json.dumps(MultList)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    elif op == "3":
        number = random.choice(numbers)
        print(number)
    elif op == "4":
        sort_inv = sorted( numbers, reverse=True )
        print(sort_inv)
    elif op == "5":
        sort = sorted( numbers )
        print(sort)
    elif op == "6":
        print(" Bye ...")

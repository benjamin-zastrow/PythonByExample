
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError: # catching specific errors
    print("Invalid Input!")
except ValueError as err: # storing error in variable
    print(err)
except:
    print("Default error!") # not good practice
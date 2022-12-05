is_male = False
is_tall = False


if is_male and is_tall: # &&
    print("You are a male and tall!")

elif is_male or is_tall: # ||
    print("You are either a male or tall!")

elif not(is_tall) and not(is_male):
    print("You are neither male nor tall!") 

else:
    print("Help! This shouldn't happen at all!")

#comparison 

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

I1 = input("Gimme Numba 1: ")
I2 = input("Gimme Numba 2: ")
I3 = input("Gimme Numba 3: ")
print("Biggest of these: " + max_num(I1, I2, I3))

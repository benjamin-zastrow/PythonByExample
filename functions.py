def hello(user): # defines function with parameter
    print("Hello " + user)
    return True

def cube(x):
    return x*x*x
print("Beginning")
hello("Benjamin")
print(cube(3))
result = cube(4)
print(result)
print("End")

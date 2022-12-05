n1 = float(input("Numba 1: "))
op = input("Gimme operator: ")
n2 = float(input("Numba 2: "))

if op == "+":
    res = n1 + n2
elif op == "-":
    res = n1 - n2
elif op == "*":
    res = n1 * n2
elif op == "/":
    res = n1 / n2
else:
    print("Wrong operator, you idiot!")

print("Result: " + str(res))
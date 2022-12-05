#reading data

file = open("test.txt", "r") # opens file in read mode (w: write, a: append, r+: read and write)
if file.readable:
    for line in file.readlines(): # puts every line into array
        print(line)
file.close() # closes file

# appending data, be careful!

file = open("employees.txt", "a") # w would overwrite file
file.write("\n" + input("neuer Kollege: "))
file.close()


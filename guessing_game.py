secret = "Peter"
limit = 3

while True:
    if limit <= 0:
        break
    guess = input("Enter your guess: ")
    if guess == secret:
        print("Very well, nice one!")
        break
    else:
        limit = limit - 1
        print("You Idiot, try again!\nYou got " + str(limit) + " tries left!")
# Giraffe Language: Every vowel is being turned into a g

def translate(phrase):
    translation = ""
    for letter in phrase: # iterate through array / string / list / whatever
        if letter in "AEIOU": # very cool
            translation += "G"
        elif letter in "aeiou":
            translation += "g"
        else:
            translation += letter
    return translation

input_phrase = input("Gimme Phrase: ")
print("New Phrase: " + translate(input_phrase))
import random

word_list = ["Apple", "Pear", "Orange", "Blueberry", "Bananna"]
print(word_list)

word = random.choice(word_list)

print(word)


guess = input("Please choose a letter: ")

if len(guess) == 1:
    print("Good Guess!")
else:
    print("Oops! That is not a valid input!")
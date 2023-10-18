import random

word_list = ["Apple", "Pear", "Orange", "Blueberry", "Banana"]

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
        else:
            print(f"Sorry, {guess} is not in the word")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Call the check_guess method and pass the guess as an argument to this method
                self.check_guess(guess)
                # Finally, append the guess to the list_of_guesses.
                self.list_of_guesses.append(guess)


hangman_game = Hangman(word_list)
hangman_game.ask_for_input()

from milestone_2 import word

def check_guess():
    while True:
        guess = input("Guess a letter: ")
        x = len(guess)
        
        if x == 1 and guess.isalpha():
            lower_case = guess.lower()  # Moved here to ensure correct case conversion
            if lower_case in word:
                print(f"Good Guess, {lower_case} is in the word")
            else:
                print(f"Sorry, {lower_case} is not in the word")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


# Step 3: Call the check_guess function
def ask_for_input():
    check_guess()

# Step 4: Call the ask_for_input function to test your code
ask_for_input()

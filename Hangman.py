import random

word_list = ["apple", "banana", "cherry", "dates", "figs", "Grapes"]
word = random.choice(word_list)
guessed_letters = set()
max_guesses = 6
guesses_left = max_guesses


def print_game_state():
    print(f"Word: {''.join([letter if letter in guessed_letters else '_' for letter in word])}")
    print(f"Guesses left: {guesses_left}")
    print(f"Guessed letters: {' '.join(sorted(list(guessed_letters)))}")
    print()


while True:
    print_game_state()

    
    if set(word) == guessed_letters:
        print("Congratulations, you won!")
        break
    elif guesses_left == 0:
        print("Game over, you lost!")
        print(f"The word was: {word}")
        break

    
    guess = input("Guess a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid guess, please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter, try again.")
        continue

    
    guessed_letters.add(guess)
    if guess not in word:
        guesses_left -= 1
        print(f"Sorry, '{guess}' is not in the word.")

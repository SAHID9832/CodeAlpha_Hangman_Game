import random
import time

# List of 5 predefined words
words = ["python", "java", "coding", "logic", "array"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")
print("Rule: Repeated letters will NOT reduce chances")

while wrong_guesses < max_wrong:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    # WIN condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        print("Game Completed Successfully!")
        time.sleep(2)
        break

    guess = input("Enter a letter: ").lower()

    # Validation: single alphabet only
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter only ONE alphabet letter.")
        continue

    # Repeated guess check (NO chance loss)
    if guess in guessed_letters:
        print("⚠️ You already guessed this letter. Try a new one.")
        continue

    # Correct guess
    if guess in word:
        guessed_letters.append(guess)
        print("✅ Correct guess!")
    else:
        guessed_letters.append(guess)
        wrong_guesses += 1
        print("❌ Wrong guess!")

# GAME OVER
if wrong_guesses == max_wrong:
    print("\n❌ Game Over!")
    print("The correct word was:", word)
    print("Better luck next time!")
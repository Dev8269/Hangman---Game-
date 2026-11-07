# HANGMAN GAME
import random

words = ["python", "java", "kotlin", "javascript"]

word = random.choice(words)
guessed =  ["_"] * len(word)

attempts = 6
#lives = 6
guessed_letters = []

print("Welcome to Single Hangman Game Created by DEV !")
print("guess the word")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a alphabet letter: ")
        continue

    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    print(" ".join(guessed))
if "_" not in guessed:
    print("Congratulations! You win!")
    print("The word was:", word)
else:
    print("Better luck next time! You lose.")
    print("The word was:", word)
                           

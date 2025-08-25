import random

word_list = ['apple','house','river','chair','plant']
word = random.choice(word_list)
guessed = ['-'] * len(word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", attempts,"incorrect guesses allowed.\n")

while attempts > 0 and '-' in guessed:
    print("word:",''.join(guessed))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a singlr alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.\n")
        continue
    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempta -= 1
        print(f"wrong guess! You have {attempts} attempts left.\n")
        if '_' not in guesed:
            print("Congratulations! You guessed t+he word:", word)
else:
    print("Game Over! The word was:", word)
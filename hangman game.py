import random
words = ["apple","mango","banana","grapes","orange"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
print("Welcome to Hangman!")
print("Guess the word one letter at the time.")
print("you have 6 incorrect gusses.")
while wrong_guesses<max_wrong_guesses:
    display_word = "_"
    for letter in word:
        if letter in guessed_letters:
            display_word += letter 
    else:
        display_word += "_"
        print("\nword:",display_word)
        if "_" not in display_word:
            print("congratulations! you guessed the word:",word)
            break
        guess = input("guess a letter:").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("please enter only one leter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print("correct guess!")
        else:
            wrong_guesses += 1
            print("wrong guesses!")
            print("incorrect guesses:", wrong_guesses,"/",max_wrong_guesses)
else:
    print("\n game over!")
    print("the correct word was:",word)
    
import random
def hangman_loop():
    attempts = int(5)
    guessed = False
    words = ['house', 'dog', 'train', 'colony']
    word = random.choice(words)
    letters = int(len(word))

    print(f"The word is {letters} letters long")
    lost = False
    guessed = False

    while not guessed:
        action = input("Do you want to guess the word (W) or a letter (L)?: ")
        action = action.capitalize()
        if action == str("W"):
            guess = input("What do you think the word is?: ")
            guess = guess.lower()
            if guess == word:
                print(f"You got it right! The word was {word}!")
                guessed = True
            else:
                attempts = attempts - 1
                print(f"That's not the word... You have {str(attempts)} attempts left.")
        elif action == str("L"):
            guessletter = input("What letter do you think the word may contain?: ")
            amount = int(len(guessletter))
            if word.count(guessletter) > 0:
                slots = [i for i in range(len(word)) if word.startswith(guessletter, i)]
                print(f"The word contains that letter in the slots: {slots}")
            else:
                attempts = attempts - 1
                print(f"The word doesnt contain that letter, you have " + str(attempts) + " attempts left.")
        else:
            print("Invalid input")
        if attempts == 0:
            print(f"The word was {word}, better luck next time!")
            guessed = True
    if guessed:
        again = input("Do you want to play again?(Y or N): ")
        again = again.upper()
        if again == "Y":
            hangman_loop()
            guessed = False
        elif again == "N":
            print("See you next time!")
        else:
            print("Invalid Input")


hangman_loop()
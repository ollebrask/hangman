from simple_term_menu import TerminalMenu
import words
import stages
import random


def rules():
    """
    Presents the rules for the user, and showing the choose difficulty menu
    """
    print("1. You can choose by 3 difficulties")
    print("   '1' for easy, '2' for medium, '3' for hard")
    print(
        "2. If you guess a correct letter, the letter will appear in the word")
    print("3. If you guess all the correct letters in the word, you win!")
    print(
        "4. If you guess a incorrect letter, a part of hangmans body is shown")
    print("5. If you guess 5 incorrect letters, you lose\n")
    difficulty()


def difficulty():
    """
    Shows a menu for choosing difficulties.
    Based on selected level it chooses a random word and starts game
    """
    difficulty = ["1", "2", "3"]
    terminal_menu = TerminalMenu(difficulty, title="Choose difficulty:")
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        print("You choose difficulty 1")
        # https://www.w3schools.com/python/ref_random_choice.asp
        word = random.choice(words.words_1)
        game(word)
    elif menu_entry_index == 1:
        print("You choose difficulty 2")
        # https://www.w3schools.com/python/ref_random_choice.asp
        word = random.choice(words.words_2)
        game(word)
    elif menu_entry_index == 2:
        print("You choose difficulty 3")
        # https://www.w3schools.com/python/ref_random_choice.asp
        word = random.choice(words.words_3)
        game(word)


def retry():
    """
    Shows a menu where user can decide to play again
    If yes, main function runs. If no, string is shown.
    """
    difficulty = ["Yes", "No"]
    terminal_menu = TerminalMenu(difficulty, title="Play again?")
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        main()
    elif menu_entry_index == 1:
        print("Thank you for playing :)")


def game(word):
    """
    Printing the stage based on guesses and guessed letters
    Input for guessing letters
    When out of guesses or all correct letters, retry function runs
    """
    guesses = 5
    # set function found at https://www.w3schools.com/python/ref_func_set.asp
    guessed_letters = set()
    while guesses > 0 and not all(
            letter in guessed_letters for letter in word):
        print(stages.stages[5 - guesses])
        # join found at https://www.w3schools.com/python/ref_string_join.asp
        print("Guessed:", " ".join(guessed_letters))
        print(
            "Word:", " ".join(
                letter if letter in guessed_letters
                else "_" for letter in word))

        # To make sure nothing else than a letter is inputted
        # found at https://www.w3schools.com/python/ref_string_isalpha.asp
        while True:
            guess = input("Guess a letter: \n").strip()
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("Invalid input. Please enter only a single letter.")

        if guess in guessed_letters:
            print("You alredy guessed that letter!")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            guessed_letters.add(guess)
            guesses -= 1
            print(f"Incorrect. You have {guesses} guesses left.")

    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations! You guessed the word: {word}")
        retry()
    else:
        print(stages.stages[5 - guesses])
        print(f"Game Over. The word was: {word}\n")
        retry()


def main():
    print("Welcome to Hangman game, please choose one of the following:\n")
    options = ["Read rules", "Choose difficulty"]
    # Terminal menu found at https://pypi.org/project/simple-term-menu/
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        rules()
    elif menu_entry_index == 1:
        difficulty()


main()

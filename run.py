from simple_term_menu import TerminalMenu
from colorama import Fore, Back, Style
import words
import stages
import rules
import random
import os


def clear_terminal():
    """ Clears the terminal """
    #found at https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
    os.system('cls' if os.name == 'nt' else 'clear')


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
        word = random.choice(words.words_2)
        game(word)
    elif menu_entry_index == 2:
        print("You choose difficulty 3")
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
        clear_terminal()
        main()
    elif menu_entry_index == 1:
        clear_terminal()
        print(Fore.YELLOW + "Thank you for playing 😄")
        print(Style.RESET_ALL)


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
        print("Used letters:", " ".join(guessed_letters))
        print(
            "Word:", " ".join(
                letter if letter in guessed_letters
                else "_" for letter in word))

        while True:
            guess = input("Guess a letter: \n").strip()
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("Invalid input. Please enter only a single letter.")

        if guess in guessed_letters:
            clear_terminal()
            print("You alredy guessed that letter!")
        elif guess in word:
            clear_terminal()
            guessed_letters.add(guess)
            print("Correct!")
        else:
            clear_terminal()
            guessed_letters.add(guess)
            guesses -= 1
            print(f"Incorrect. You have {guesses} guesses left.")

    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations! You guessed the word: {word}")
        retry()
    else:
        clear_terminal()
        print(stages.stages[5 - guesses])
        print(f"Game Over. The word was: {word}\n")
        retry()


def main():
    print(Fore.RED + "Welcome to the 😵 Hangman 😵 game!")
    print(Fore.YELLOW + "Please choose one of the following:\n")
    print(Style.RESET_ALL)
    options = ["Read rules", "Choose difficulty"]
    # Terminal menu found at https://pypi.org/project/simple-term-menu/
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        rules.rules()
    elif menu_entry_index == 1:
        difficulty()


if __name__ == "__main__":
    main()

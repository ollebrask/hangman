from simple_term_menu import TerminalMenu
import words
import random

def rules():
    print("1. You can choose by 3 difficulties.")
    print("'1' for easy, '2' for medium, '3' for hard")
    print("2. If you guess a correct letter, the letter will appear in the word")
    print("3. If you guess all the correct letters in the word, you win!")
    print("4. If you guess a incorrect letter, a body part is shown.")
    print("5. If you guess 5 incorrect letters, you lose")

def game(word):
    guesses = 5
    #https://www.w3schools.com/python/ref_func_set.asp
    guessed_letters = set()
    while guesses > 0 and not all(letter in guessed_letters for letter in word):
        #https://www.w3schools.com/python/ref_string_join.asp
        print("Guessed:", " ".join(guessed_letters))
        print("Word:", " ".join(letter if letter in guessed_letters else "_" for letter in word))
        guess = input("Guess a letter: \n")
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
    else:
        print(f"Game Over. The word was: {word}")

def main():
    print("Welcome to Hangman game, please choose on of the following!\n")
    options = ["Read rules", "Choose difficulty"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    #print(f"You have selected {options[menu_entry_index]}!")

    if menu_entry_index == 0:
        rules()
    elif menu_entry_index == 1:
        difficulty = ["1", "2", "3"]
        terminal_menu = TerminalMenu(difficulty, title="Difficulty:")
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            print("You choose difficulty 1")
            #https://www.w3schools.com/python/ref_random_choice.asp
            word = random.choice(words.words_1)
            game(word)
        elif menu_entry_index == 1:
            print("You choose difficulty 2")
        elif menu_entry_index == 2:
            print("You choose difficulty 3")
        


main()

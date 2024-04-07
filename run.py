from simple_term_menu import TerminalMenu

def rules():
    print("1. You can choose by 3 difficulties.")
    print("'1' for easy, '2' for medium, '3' for hard")
    print("2. If you guess a correct letter, the letter will appear in the word")
    print("3. If you guess all the correct letters in the word, you win!")
    print("4. If you guess a incorrect letter, a body part is shown.")
    print("5. If you guess 5 incorrect letters, you lose")

def main():
    print("Welcome to Hangman game, please choose on of the following!\n")
    options = ["Read rules", "Choose difficulty"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    #print(f"You have selected {options[menu_entry_index]}!")

    if menu_entry_index == 0:
        rules()
    elif menu_entry_index == 1:
        print("Choose difficulty is under construction:)")


main()

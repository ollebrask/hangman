from simple_term_menu import TerminalMenu

def main():
    print("Welcome to Hangman game, please choose on of the following!")
    options = ["Read rules", "Choose difficulty"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")


main()
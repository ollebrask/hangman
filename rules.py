import run


def rules():
    """
    Presents the rules for the user.
    Showing the choose difficulty menu.
    """
    run.clear_terminal()
    print(f"""
    RULES:

    1. You can choose by 3 difficulties
       '1' for easy, '2' for medium, '3' for hard
    2. If you guess a correct letter, the letter will appear in the word
    3. If you guess all the correct letters in the word, you win!
    4. If you guess a incorrect letter, a part of hangmans body is shown
    5. If you guess 5 incorrect letters, you lose
    """)
    run.difficulty()

"""
Name(s): Duany Pena and Jaivan Gordon
Name of Project: The Game House
"""

#Write the main part of your program here. Use of the other pages is optional.
import os
import time

print(
    "Welcome to the Game House."
print(
    "If you would like to play Rock Paper Scissors, write Rock Paper Scissors on the next line. If you would like to play Hangman, write Hangman. If you would like to play Tic Tac Toe, enter Tic Tac Toe."
)
code = input("Which game would you like to play? ")
if code == 'Rock Paper Scissors':
    os.system('clear')
    time.sleep(0.5)
    import page2
elif code == 'Hangman':
    os.system('clear')
    time.sleep(0.5)
    import page1
elif code == 'Tic Tac Toe':
    os.system('clear')
    time.sleep(0.5)
    import page3
while code != 'Rock Paper Scissors' and code != 'Hangman' and code != 'Tic Tac Toe':
    print("Not a valid game. Try again")
    time.sleep(1)
    os.system('clear')
    print(
    "If you would like to play Rock Paper Scissors, write Rock Paper Scissors on the next line. If you would like to play Hangman, write Hangman. If you would like to play Tic Tac Toe, enter Tic Tac Toe."
)
    code = input("Which game would you like to play? ")
    if code == 'Rock Paper Scissors':
        os.system('clear')
        time.sleep(0.5)
        import page2
    elif code == 'Hangman':
        os.system('clear')
        time.sleep(0.5)
        import page1
    elif code == 'Tic Tac Toe':
        os.system('clear')
        time.sleep(0.5)
        import page3
#import page1
#import page2
#import page3
#import page4  # uncomment if you're using page4

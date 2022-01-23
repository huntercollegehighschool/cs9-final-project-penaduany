"""
Name(s): Duany Pena and Jaivan Gordon
Name of Project: The Game House
"""

#Write the main part of your program here. Use of the other pages is optional.
import os
import time

print(
    "Welcome to the Game House."
)  #You can change 'Game House' to whatever you want it to be, I just put it there for now
print(
    "If you would like to play Rock Paper Scissors, write Rock Paper Scissors on the next line. If you would like to play Hangman, write Hangman."
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
while code != 'Rock Paper Scissors' and code != 'Hangman' :
    print("Not a valid game. Try again")
    time.sleep(1)
    os.system('clear')
    print(
    "If you would like to play Rock Paper Scissors, write Rock Paper Scissors on the next line. If you would like to play Hangman, write Hangman. "
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
#import page1
#import page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

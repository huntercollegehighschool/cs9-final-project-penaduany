import os
import random
import time
name = input("What is your name? ")
print("Hello,", name)
time.sleep(1)
print("Let's play hangman")

def get_guess():
  dashes = "-" * len(secret_word)
  guesses_left = 10
  while guesses_left > -1 and not dashes == secret_word:
    print("The word is:", dashes)
    print ("You have", guesses_left, "incorrect guesses left")
    guess = input("Guess:")
    if len(guess) != 1:
      print ("Your guess must have exactly one character!")
    elif guess in secret_word:
      print ("That letter is in the secret word!")
      dashes = update_dashes(secret_word, dashes, guess)
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1
  if guesses_left < 0:
    print ("You lose. The word was: " + str(secret_word))
  else:
    print ("Congrats! You win. The word was: " + str(secret_word))
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess
    else:
      result = result + cur_dash[i]
  return result

    
words = ["amazing", "amazon", "spider", "man", "electric", "lizard", "giant", "goblin", "fast", "slower", "shark", "doctor", "thirteen", "chair", "lamp", "jazz", "music", "skull", "gorilla", "dog", "cat", "computer", "refrigerator"]

secret_word = random.choice(words)
get_guess()

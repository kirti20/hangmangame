# -*- coding: utf-8 -*-
"""Hangman.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dcRsf4UlZDWZ5iWIWb3kZyCoWHeMy6dr
"""

import random
def hangman():
  word = random.choice( ["apple","eat","song","instagram","facebook","whatsapp"])
  validletters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  turns = 10
  guessmade = ''
  
  while len(word)>0:
    main=""
    missed = 0
    for letter in word :
       if letter in guessmade:
          main = main +letter
       else:
           main = main +"_" + " "

    if main == word:
       print(main)
       print("you win!!!!!!!!")
       break
    print("Guess the word :" ,main)
    guess = input()

    if guess in validletters:
      guessmade = guessmade + guess
    else:
      print("enter a valid character")
      guess = input()
    if guess not in word:
       turns = turns -1
       if turns ==9:
         print("9 turns left")
         print("--------")
       if turns == 8:
          print("8 turns left")
          print("---------")
          print("    o    ")
       if turns == 7:
          print("7 turns left")
          print("---------")
          print("    o    ")
          print("    |    ")
       if turns == 6:
          print("6 turns left")
          print("---------")
          print("    o    ")
          print("    |    ")  
          print("   /     ")
       if turns == 5:
          print("5 turns left")
          print("---------")
          print("    o    ")
          print("    |    ")  
          print("   / \   ")
       if turns == 4: 
          print("4 turns left")
          print("---------")
          print("   \o    ")
          print("    |    ")  
          print("   / \   ")
       if turns == 3: 
          print("3 turns left")
          print("---------")
          print("   \o/    ")
          print("    |    ")  
          print("   / \   ")
       if turns == 2: 
          print("2 turns left")
          print("---------")
          print("   \o/|  ")
          print("    |    ")  
          print("   / \   ")
       if turns == 1: 
          print("1 turns left")
          print("---------")
          print("   \o|/  ")
          print("    |    ")  
          print("   / \   ")
       if turns == 0: 
          print("you lost and let a kind man die")
          print("---------")
          print("      |  ")
          print("    o_|  ")
          print("   /|\   ")  
          print("   / \   ")
          break
         


name = input("enter ur name")
print("welcome",name)
print("****************************")
print("try to guess the word in less than 10th attempts")
hangman()
print()
c
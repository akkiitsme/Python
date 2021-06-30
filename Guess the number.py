#In this game the computer will select a random number from 1 to 20. You will the. be asked to choose a number between 1 and 20. Try and guess the same number as the computer. No One has ever won...
from random import randint
guess= int(input())
x = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
answer= x[randint(0,21)]
if guess == answer:
   print ("correct.")
else:
   print ("incorrect. Would you like to try again?")
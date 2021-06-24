import random

number=random.randint(1,9)
chance=0
print("number guessing name")
guess = int(input("guess a number between 1 & 9 :-"))

if (guess<7):
    print("your guess is too low(guess a higher number this)")
    
if guess == 9:
    print("you won !!")



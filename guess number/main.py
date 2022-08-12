from art import *
from random import *
print(logo)
answer = randint(1,100)
level = input("Choose a difficulty. Type easy or hard :")
if level=="easy": life=10
else: life = 5
while life > 0:
    print(f"You have {life} attempts remaining to guess the number")
    user_guess=int(input("Make a guess:"))
    if user_guess > answer:
        print("To high")
        print("Guess again")
    elif user_guess < answer:
        print("To low")
        print("Guess again")
    elif user_guess == answer:
        print(f"You got it! The answer was {user_guess}")
        break
    life-=1
else:
    print("You run out of guesses you loose")


import sys

# importing random package and randint method
from random import randint

# generating a number from 1 to 10
answer = randint(1, 10)
# getting an input from user and checking whether it is between 1 and 10 and is equal to answer
while True:
    try:
        guess = int(input("Guess a number 1~10: "))
        if 0 < guess < 11:
            if guess == answer:
                print("Congrats!! you are a genius!!")
                break
        else:
            print("Ohh man try again All the best!!")
    except ValueError:
        print("enter a number")
        continue

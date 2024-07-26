# This program makes a guess the number game
import random

print("Hello, what is your name?")
myName = input()
print("Well, " + myName +", I am thinking of a number between 1 and 20")
print("Take a guess")
guess = int(input())
count = 0
number = random.randint(1, 20)
for count in range(6):
    if (guess < number):
        print("Your guess is too low. Try again.")
        guess = int(input())
    if (guess > number):
        print("Your guess is too high. Try again.")
        guess = int(input())
    if (guess == number):
        break

if guess == number:
    guessesTaken = str(count + 1)
    print("Good job, " + myName + "! You guessed my number in " + guessesTaken + " guesses!")

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
    
    

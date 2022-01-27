import random

n = random.randint(0, 10)

guess = int(input("Enter your guess (0 to 10): "))

if guess==n:
    print("Voila ! you hit the jackpot ")
else: 
    print("Better luck next time")

import random

answer = random.randint(1,100)

attempts = 0

def guess(num, ans):
    if ans > num:
        return print("Too low! Try again!")
    elif ans < num:
        return print("Too high! Try again!")

number = int(input("Guess a number between 1 and 100. "))
attempts += 1

while number != answer:
    guess(number, answer)
    number = int(input("Guess a number between 1 and 100. "))
    attempts += 1

print(f"Congrats!!! The number was {answer}")
print(f"It took you {attempts} attempt(s)")

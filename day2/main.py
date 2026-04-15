import random

attempts = 0

def guess(num, ans):
    if ans > num:
        return print("Too low! Try again!")
    elif ans < num:
        return print("Too high! Try again!")
    else:
        return print("Correct!")
running = True

while running:
    print("What difficulty would you like to play at?: ")
    diff = input(f"Easy: 1-50, 10 attempts \nMedium: 1-100, 7 attempts \nHard: 1-200, 5 attempts \nDifficulty: ").lower()

    while diff != "easy" and diff != "medium" and diff != "hard":
        diff = input("Please type: Easy, Medium, or Hard!: ").lower()

    if diff == "easy":
        answer = random.randint(1,50)
        attempts = 10
        rng = 50
        print(f"You chose {diff} which means you have {attempts} attempts.")
    elif diff == "medium":
        answer = random.randint(1,100)
        attempts = 7
        rng = 100
        print(f"You chose {diff} which means you have {attempts} attempts.")
    elif diff == "hard":
        answer = random.randint(1,200)
        attempts = 5
        rng = 200
        print(f"You chose {diff} which means you have {attempts} attempts.")
    
    number = int(input(f"Guess a number between 1 and {rng}. "))
    attempts -= 1  

    while number != answer and attempts != 0:
        guess(number, answer)
        number = int(input(f"Guess a number between 1 and {rng}. "))
        attempts -= 1

    if attempts <= 0:
        print(f"That was your last attempt! The correct number was {answer}")
    else:
        print(f"Congrats!!! The number was {answer}")
        print(f"It took you {attempts} attempt(s)")

    again = input("Would you like to play again? ").lower()
    while again != "yes" and again != "no":
        again = input("Would you like to play again?(Yes or No): ").lower
    
    if again == "no":
        running = False

print("Thanks for playing!")

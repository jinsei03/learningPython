import random

def guess(num, ans):
    if ans > num:
        print("Too low! Try again!")
        return False
    elif ans < num:
        print("Too high! Try again!")
        return False
    else:
        print("Correct!")
        return True

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
    
    correct = False
    attemptNum = 0

    while attempts and not correct:
        number = int(input(f"Guess a number between 1 and {rng}. "))
        correct = guess(number, answer)
        if not correct:
            attempts -= 1
        attemptNum += 1

    if correct:
        print(f"Congrats!!! The number was {answer}")
        print(f"It took you {attemptNum} attempt(s)")
    else:
        print(f"That was your last attempt! The correct number was {answer}")

    again = input("Would you like to play again? ").lower()
    while again != "yes" and again != "no":
        again = input("Would you like to play again?(Yes or No): ").lower()
    
    if again == "no":
        running = False

print("Thanks for playing!")

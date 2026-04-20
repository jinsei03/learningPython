numOfHabits = None
completed = 0
INcompleted = 0
rank = 0

while True:
    try:
        numOfHabits = int(input("Please enter a number between 3 and 5 only!: "))
        while numOfHabits < 3 or numOfHabits > 5:
            numOfHabits = int(input("Only numbers between 3 and 5: "))
        break
    except ValueError:
            print("Invalid input. Please try again.")

print()
habits = [[0 for j in range(2)] for i in range(numOfHabits)]
for i in range(numOfHabits):
    habits[i][0]  = input(f"What is the {i + 1} habit: ")
    while not habits[i][0].strip():
        habits[i][0] = input(f"Please type something!\nWhat is the {i + 1} habit: ")

print()
for i in range(numOfHabits):
    habits[i][1] = input(f"Did you complete {i + 1} task?: ").lower()
    while habits[i][1] != "y" and habits[i][1] != "yes" and habits[i][1] != "n" and habits[i][1] != "no":
        habits[i][1] = input(f"Please only put y/n or yes/no!!!\nDid you complete {i+1} habit: ").lower()
    if habits[i][1] == "y" or habits[i][1] == "yes":
        completed += 1
    elif habits[i][1] == "n" or habits[i][1] == "no":
        INcompleted += 1

print()
print(f"You did a total of {numOfHabits} habits!\nYou completed: {completed} habits!\nYou did not complete: {INcompleted} habits!")

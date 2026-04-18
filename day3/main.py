numOfHabits = None
while True:
    try:
        numOfHabits = int(input("Please enter a number between 3 and 5 only!: "))
        while numOfHabits < 3 or numOfHabits > 5:
            numOfHabits = int(input("Only numbers between 3 and 5: "))
        break
    except ValueError:
            print("Invalid input. Please try again.")
print(numOfHabits)

habits = [[] for _ in range(numOfHabits)]
for i in range(numOfHabits):
    habits[i] = input(f"What is the {i + 1} habit: ")


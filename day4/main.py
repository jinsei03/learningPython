f1 = open("data.txt", "a")
f1.write("Writing to file\n")
f1.close()

f1 = open("data.txt", "r+")
print(f1.read())



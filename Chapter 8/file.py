# Read file
f = open("file.txt")
data = f.read()
print(data)
f.close()

# Write to file
f = open("filew.txt", "w")
f.write("This is a new line of text.\n")
f.write("This is another line of text.\n")
f.close()

# with statement
with open("file.txt") as f:
    data = f.read()
    print(data)
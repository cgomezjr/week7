fileName = input("Enter the file name: ")

lines = []
f = open(fileName, 'r')
for line in f:
    lines.append(line.strip())

while True:
    print("This file has", len(lines), "lines.")
    if len(lines) == 0:
        print("File must contain lines of text. Try again.")
        break
    chooseLine = int(input("Enter a line number or enter 0 to quit: "))
    if chooseLine == 0:
        break
    elif chooseLine > len(lines):
        print("Line number must be between 1 and", len(lines))
    else:
        print("Line", chooseLine, "contains the following: ", lines[chooseLine - 1])

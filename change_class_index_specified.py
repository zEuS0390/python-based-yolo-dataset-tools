import os, glob

path = input("Text Labels Directory: ")
files = glob.glob(os.path.join(path, "*"))
TXTs = []

for file in files:
    fileType = os.path.splitext(os.path.basename(file))[1]
    if fileType == ".txt":
        TXTs.append(file)


indexToChange = int(input("Index to change: "))
newIndex = int(input("New index: "))

def changeIndex(label:str):
    values = label.split()
    var = int(values[0])
    if var == indexToChange:
        values[0] = str(newIndex)
        return " ".join(values)
    return " ".join(values)

# Loop through all files
for txt in TXTs:

    # Read
    with open(txt, "r") as file:
        lines = [l.rstrip() for l in file.readlines()]
        for index in range(len(lines)):
            lines[index] = changeIndex(lines[index])

    # Write
    with open(txt, "w") as file:
        for line in lines:
            file.write(line+"\n")
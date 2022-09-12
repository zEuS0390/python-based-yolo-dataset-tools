import os, glob

path = input("Text Labels Directory: ")
files = glob.glob(os.path.join(path, "*"))
TXTs = []

for file in files:
    fileType = os.path.splitext(os.path.basename(file))[1]
    if fileType == ".txt":
        TXTs.append(file)

newIndex = int(input("New index: "))

def changeIndex(label:str):
    values = label.split()
    values[0] = str(newIndex)
    return " ".join(values)

for txt in TXTs:
    with open(txt, "r+") as file:
        lines = [line.rstrip() for line in file.readlines()]
        file.seek(0)
        for line in lines:
            newLine = changeIndex(line)+"\n"
            file.write(newLine)
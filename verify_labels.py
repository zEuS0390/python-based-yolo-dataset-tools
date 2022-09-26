import os, glob

# Verify YOLO format labels
directory = input("Input directory: ")
nvalues = 5 # Number of values of the standard YOLO format

files =  [os.path.normpath(file) for file in glob.glob(os.path.join(directory, "*.txt"))]
for file in files:
    filename = os.path.splitext(os.path.basename(file))[0]
    if filename == "classes":
        continue
    with open(file, "r") as txt:
        lines = txt.readlines()
        for line in lines:
            n = len(line.split())
            if n != nvalues:
                print(f"{file} has {n} values")
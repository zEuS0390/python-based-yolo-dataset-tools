import os, glob, sys

# Verify YOLO format labels
directory = input("Input directory: ")
nvalues = 5 # Number of values of the standard YOLO format
nfound = 0

if not os.path.exists(directory) or not os.path.isdir(directory):
    sys.stdout.write("Invalid input directory.\n")
    sys.exit()

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
                sys.stdout.write(f"{file} has {n} values.\n")
                n += 1

sys.stdout.write(f"Found {nfound} invalid files.\n")
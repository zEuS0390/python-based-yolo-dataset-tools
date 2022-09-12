import os, glob

root = input("Image directory: ")
files = glob.glob(os.path.join(root, "*"))

for file in files:
    fileType = os.path.basename(os.path.splitext(file)[1])
    if os.path.isfile(file):
        basename = os.path.basename(file)
        filename = os.path.splitext(basename)[0]
        redundant = filename.find('(1)')
        if redundant != -1:
            toRemove = os.path.join(root, basename)
            os.remove(toRemove)
            print(f"[REMOVED]: {toRemove}")
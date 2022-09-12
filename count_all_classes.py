import os, glob

path = input("Dataset Directory: ")
# classes_file = input("Classes Text File: ")
classes_file =input("Classes filepath: ")


with open(classes_file, "r") as file:
    classes = [line.rstrip() for line in file.readlines()]
    classes_count = {_class:0 for _class in classes}

# Explore all sub-directories in a directory
def explore(root):
    total_images = 0
    files = glob.glob(os.path.join(root, "*"))
    for file in files:
        fileType = os.path.splitext(os.path.basename(file))[1]
        if fileType == ".txt":
            with open(file, "r") as textFile:
                lines = [line.rstrip() for line in textFile.readlines()]
                for line in lines:
                    if len(line.split()) == 5:
                        class_id = int(line.split()[0])
                        if class_id <= 11 and class_id >= 0:
                            classes_count[classes[class_id]] += 1
                            total_images += 1
        if os.path.isdir(file):
            total_images += explore(file)
    return total_images

texts = explore(path)

print("\n\tClasses:\n")
for _class in classes_count:
    print("\t"+f"{_class:<20s}: {classes_count[_class]}")
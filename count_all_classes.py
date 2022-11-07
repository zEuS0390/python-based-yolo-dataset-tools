import os, glob

path = input("Labels directory: ")
classes_file =input("Classes filepath: ")

with open(classes_file, "r") as file:
    classes = [line.rstrip() for line in file.readlines()]
    nclasses = len(classes)
    classes_count = {_class:0 for _class in classes}

# Explore all sub-directories in a directory
def explore(root):
    files = glob.glob(os.path.join(root, "*"))
    total_images = 0
    for file in files:
        if os.path.splitext(os.path.basename(file))[0] == "classes":
            continue
        fileType = os.path.splitext(os.path.basename(file))[1]
        if fileType == ".txt":
            total_images += 1
            with open(file, "r") as textFile:
                lines = [line.rstrip() for line in textFile.readlines()]
                for line in lines:
                    if len(line.split()) == 5:
                        class_id = int(line.split()[0])
                        if class_id <= nclasses-1 and class_id >= 0:
                            classes_count[classes[class_id]] += 1
        if os.path.isdir(file):
            total_images += explore(file)
    return total_images

total_images = explore(path)

print("\n\tClasses: \n")
for _class in classes_count:
    print("\t"+f"{_class:<20s}: {classes_count[_class]}")
print(f"\n\tTotal Images: {total_images}", end="")
total_boxes = 0
for cls in classes_count:
    total_boxes += classes_count[cls]
print(f"\n\tTotal Boxes: {total_boxes}", end="")

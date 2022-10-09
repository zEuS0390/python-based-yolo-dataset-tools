import os, glob

image_type = "jpg"

def getLength(file):
    with open(file, "r") as file:
        length = len(file.readlines())
        return length

print("Remove Images with Empty Label")
images_directory = input("Image Directory: ")
labels_directory = input("Label Directory: ")
txt_files = glob.glob(os.path.join(labels_directory, "*.txt"))

empty_labels = []
total_n_boxes = 0

for txt_path in txt_files:
    txt_file = os.path.basename(txt_path)
    img_file = ".".join([os.path.splitext(txt_file)[0], image_type])
    img_path = os.path.normpath(os.path.join(images_directory, img_file))
    if os.path.exists(img_path):
        length = getLength(txt_path)
        total_n_boxes += length
        if length == 0:
            empty_labels.append((img_path, os.path.normpath(txt_path)))
        print(f"('{img_file}', '{txt_file}') has {length} labels.")
    else:
        print(f"'{img_path}' does not exist!")

length = len(empty_labels)
print(f"There are {length} empty labels found.")
if length > 0:
    response = input("Would like to remove them? (y/n): ").lower()
    if response == 'y':
        print(f"Removing {length*2} files.")
        for i in range(length):
            img_path = empty_labels[i][0]
            txt_path = empty_labels[i][1]
            print(f"Removing {img_path} and {txt_path}")
            os.remove(img_path)
            os.remove(txt_path)
        print(f"Removed {length*2} files.")
    elif response == 'n':
        print("Aborted.")
print(f"There are {total_n_boxes} total number of boxes in labels.")
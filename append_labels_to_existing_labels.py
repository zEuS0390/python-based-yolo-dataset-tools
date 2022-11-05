import glob, os, sys

source_directory = input("Labels directory (Source): ")
destination_directory = input("Labels directory (Destination): ")

if not os.path.exists(source_directory):
    print("Source directory does not exist.")
    sys.exit()

if not os.path.exists(destination_directory):
    print("Destination directory does not exist.")
    sys.exit()

source_labels = glob.glob(os.path.join(source_directory, "*.txt"))

for source_label in source_labels:
    filename = os.path.basename(source_label)
    destination_label = os.path.join(destination_directory, filename)
    if os.path.exists(destination_label):
        with open(source_label, "r") as file:
            lines = [line.strip() for line in file.readlines()]
        with open(destination_label, "a") as file:
            for line in lines:
                file.write(f"{line}\n")
        print(f"{source_label} OK")
    else:
        print(f"{destination_label} does not exist.")
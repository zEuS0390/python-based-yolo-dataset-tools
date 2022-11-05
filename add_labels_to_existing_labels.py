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
    # Check if the destination label exists
    if os.path.exists(destination_label):
        # Get the source label lines
        with open(source_label, "r") as file:
            source_label_lines = [line.strip() for line in file.readlines()]
        # Check if the current line already exist in the destination label
        with open(destination_label, "r") as file:
            destination_label_lines = [line.strip() for line in file.readlines()]
        # Verify existence before adding the new labels
        with open(destination_label, "a") as file:
            for source_label_line in source_label_lines:
                if source_label_line not in destination_label_lines:
                    file.write(f"{source_label_line}\n")
        print(f"{source_label} OK")
    else:
        print(f"{destination_label} does not exist.")
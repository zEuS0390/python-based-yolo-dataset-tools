import glob, os, sys, shutil

images_directory = input("Images directory: ")
labels_directory = input("Labels directory: ")
out_directory = input("Images with no label directory")
image_type = "jpg"
success = True

if not os.path.exists(images_directory) or os.path.isfile(images_directory):
    print("Invalid images directory. Aborted.")
    sys.exit()

if not os.path.exists(labels_directory) or os.path.isfile(labels_directory):
    print("Invalid labels directory. Aborted.")
    sys.exit()

if not os.path.exists(out_directory):
    os.mkdir(out_directory)

img_files = glob.glob(os.path.join(images_directory, f"*.{image_type}"))

for img_file in img_files:
    file = os.path.basename(img_file)
    filename = os.path.splitext(file)[0]
    label_file = os.path.normpath(os.path.join(labels_directory, ".".join([filename, "txt"])))
    if not os.path.exists(label_file):
        print(f"{label_file} does not exist. Moving to {out_directory}")
        shutil.move(img_file, os.path.join(out_directory, file))

if success:
    print("Done.")
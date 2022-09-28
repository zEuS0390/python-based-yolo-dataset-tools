import glob, os, sys, shutil

images_directory = input("Images directory: ")
labels_directory = input("Labels directory: ")
out_directory = input("Output directory: ")
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

out_images_directory = os.path.join(out_directory, "images")
out_labels_directory = os.path.join(out_directory, "labels")

if not os.path.exists(out_images_directory):
    os.mkdir(out_images_directory)
if not os.path.exists(out_labels_directory):
    os.mkdir(out_labels_directory)

txt_files = glob.glob(os.path.join(labels_directory, f"*.txt"))

for txt_path in txt_files:
    txt_file = os.path.basename(txt_path)
    img_file = ".".join([os.path.splitext(txt_file)[0], image_type])
    img_path = os.path.normpath(os.path.join(images_directory, img_file))
    if os.path.exists(img_path):
        print(f"Moving {img_file} to {out_images_directory} and {txt_file} to {out_labels_directory}")
        shutil.copy2(txt_path, os.path.join(out_labels_directory, txt_file))
        shutil.copy2(img_path, os.path.join(out_images_directory, img_file))

if success:
    print("Done.")
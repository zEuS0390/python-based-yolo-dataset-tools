import cv2, os, glob, sys

img_files_directory = input("Images directory: ")
out_directory = input("Output directory: ")
img_type = "jpg"
success = True

try:
    img_width = int(input("New image width: "))
    img_height = int(input("New image height: "))
except:
    print("Invalid image size input. Aborted.")
    sys.exit()

if not os.path.exists(img_files_directory) or os.path.isfile(img_files_directory):
    sys.stdout.write("Invalid images directory. Aborted.")
    sys.exit()

if not os.path.exists(out_directory):
    os.mkdir(out_directory)

img_files = glob.glob(os.path.join(img_files_directory, f"*.{img_type}"))

for img_file in img_files:
    img = cv2.imread(img_file)
    img = cv2.resize(img, (img_width, img_height), interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.join(out_directory, os.path.basename(img_file)), img)

if success:
    print("Done.")
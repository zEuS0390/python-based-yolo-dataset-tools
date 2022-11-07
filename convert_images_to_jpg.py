from PIL import Image
import os, glob

# Convert Any Image Type to JPG Type 
def convertImageToJPG(dirname, file):
    root = os.path.dirname(file)
    basename = os.path.basename(file)
    print(f"[CHECK]: {basename}")
    image = Image.open(file)
    rgb_image = image.convert("RGB")
    JPG = "".join([os.path.splitext(basename)[0], ".jpg"])
    rgb_image.save(os.path.join(root, dirname, JPG))
    os.remove(file)

# Declrations
imageTypes = [".png", ".PNG", ".gif", ".GIF", ".jfif", ".jpeg", ".JPEG", ".JPG", ".webp", ".WEBP"]
root = input("Image directory: ")
files = glob.glob(os.path.join(root, "*"))
converted_dir = "converted_to_jpg"

# Create unlabeled directory if it does not exist
if not os.path.exists(os.path.join(root, converted_dir)):
    os.makedirs(os.path.join(root, converted_dir))

# Check if the file is in imageTypes
for file in files:
    fileType = os.path.basename(os.path.splitext(file)[1])
    if fileType in imageTypes:
        convertImageToJPG(converted_dir, file)
    else:
        print(f"Invalid file format: {file}")

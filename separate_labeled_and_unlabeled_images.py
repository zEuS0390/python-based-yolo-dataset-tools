import glob, os, sys

imageFiles = []
txtFiles = []
LABELED = {}

# Types of images
imageTypes = [".jpg", ".JPG", ".jpeg", ".JPEG"]
path = input("Image directory: ")

# Create unlabeled directory if it does not exist
unlabeled_directory = os.path.join(path, "unlabeled")
if not os.path.exists(unlabeled_directory):
    os.makedirs(unlabeled_directory)

# Accept valid images and texts only
files = glob.glob(os.path.join(path, "*"))
for file in files:
    fileType = os.path.basename(os.path.splitext(file)[1])
    if fileType in imageTypes:
        imageFiles.append(file)
    elif fileType == ".txt":
        txtFiles.append(file)
    else:
        if os.path.isfile(file):
            print(f"[MOVED]: {os.path.basename(file)}")
            os.rename(file, os.path.join(unlabeled_directory, os.path.basename(file)))

if len(imageFiles) == 0 or len(txtFiles) == 0:
    print("No images are labeled!")
    sys.exit()

# Get labeled images
for txt in txtFiles:
    txtbasename = os.path.basename(os.path.splitext(txt)[0])
    for image in imageFiles:
        imgbasename = os.path.basename(os.path.splitext(image)[0])
        if txtbasename == imgbasename:
            LABELED[image] = txt
            print(f"[CHECK]: {imgbasename:<15}")
            break    

# Move unlabeled images to the other directory
for image in imageFiles:
    if image not in LABELED:
        source = image
        destination = unlabeled_directory
        print(f"[MOVED]: {os.path.basename(image):<15}")
        os.rename(source, os.path.join(destination, os.path.basename(image)))
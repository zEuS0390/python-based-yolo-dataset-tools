import os, glob

IMAGETYPES = [".jpg", ".JPG", ".jpeg", ".JPEG"]

def getLength(file):
    with open(file, "r") as file:
        length = len(file.readlines())
        return length

print("Remove Images with Empty Label")
path = input("Image Directory: ")
files = glob.glob(os.path.join(path, "*"))
LABELED = {}
IMAGES = []
TXTs = []

# Get the iamge and text files
for file in files:
    basename = os.path.basename(file)
    filetype = os.path.splitext(basename)[1]
    if filetype in IMAGETYPES:
        IMAGES.append(file)
    elif filetype == ".txt":
        TXTs.append(file)

# Match any image and txt files
for txt in TXTs:
    txtFileName = os.path.splitext(os.path.basename(txt))[0]
    for img in IMAGES:
        imgFileName = os.path.splitext(os.path.basename(img))[0]
        if imgFileName == txtFileName:
            LABELED[img] = txt
            break

# Remove images with empty labels
for image in LABELED:
    txt = LABELED[image]
    if getLength(txt) == 0:
        print("[REMOVE]: ", image, txt)
        os.remove(image)
        os.remove(txt)
import os, glob

# Declarations
path = input("Image directory: ")
name = input("Image name: ")
files = glob.glob(os.path.join(path, "*"))
renamed = "renamed"
IMAGETYPES = [".jpg", ".JPG", ".jpeg", ".JPEG"]
LABELED = {}
IMAGES = []
TXTs = []

# Create renamed folder if does not exist
if not os.path.exists(os.path.join(path, renamed)):
    os.makedirs(os.path.join(path, renamed))

# Get the iamge and text files
for file in files:
    fileType = os.path.splitext(os.path.basename(file))[1]
    if fileType in IMAGETYPES:
        IMAGES.append(file)
    elif fileType == ".txt":
        TXTs.append(file)

# Match any image and txt files
for txt in TXTs:
    txtFileName = os.path.splitext(os.path.basename(txt))[0]
    for img in IMAGES:
        imgFileName = os.path.splitext(os.path.basename(img))[0]
        if imgFileName == txtFileName:
            LABELED[img] = txt
            break

# Rename
n = 1
for image in LABELED:
    originalimg = image
    originaltxt = LABELED[image]
    imgType = os.path.splitext(os.path.basename(image))[1]
    if imgType == ".JPG":
        newimg = os.path.join(os.path.join(path, renamed), f"{name}{n}.JPG")
    elif imgType == ".jpg":
        newimg = os.path.join(os.path.join(path, renamed), f"{name}{n}.jpg")
    elif imgType == ".jpeg":
        newimg = os.path.join(os.path.join(path, renamed), f"{name}{n}.jpeg")
    elif imgType == ".JPEG":
        newimg = os.path.join(os.path.join(path, renamed), f"{name}{n}.JPEG")
    newtxt = os.path.join(os.path.join(path, renamed), f"{name}{n}.txt")
    print("[RENAME]: ", originalimg, originaltxt)
    os.rename(originalimg, newimg)
    os.rename(originaltxt, newtxt)
    n+=1
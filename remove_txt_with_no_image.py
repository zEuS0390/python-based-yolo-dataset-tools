import os, glob

path = input("Images directory: ")
files = glob.glob(os.path.join(path, "*"))
IMAGETYPES = [".jpg", ".JPG", ".jpeg", ".JPEG"]
LABELED = {}
IMAGES = []
TXTs = []

for file in files:
    fileType = os.path.splitext(os.path.basename(file))[1]
    if fileType in IMAGETYPES:
        IMAGES.append(file)
    elif fileType == ".txt":
        TXTs.append(file)

test = []

for txt in TXTs:
    txtFileName = os.path.splitext(os.path.basename(txt))[0]
    for image in IMAGES:
        imageFileName = os.path.splitext(os.path.basename(image))[0]
        if imageFileName == txtFileName:
            LABELED[image] = txt
            break
        
for image in IMAGES:
    try:
        for txt in TXTs:
            if LABELED[image] == txt:
                TXTs.remove(txt)
                print(f"[REMOVE]: {os.path.basename(txt)}")
    except:
        print("Failed!")

for txt in TXTs:
    txtFileName = os.path.splitext(os.path.basename(txt))[0]
    if txtFileName == "classes":
        TXTs.remove(txt)

for txt in TXTs:
    print(txt)
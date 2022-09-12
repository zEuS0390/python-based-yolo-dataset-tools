import os, glob

IMAGETYPES = [".jpg", ".JPG", ".jpeg", ".JPEG"]
path = input("Dataset Directory: ")
save = input("Save Directory: ")

# Get all images (JPG and JPEG FORMAT)
def getImages(path):
    images = []
    root = glob.glob(os.path.join(path, "*"))
    for file in root:
        fileType = os.path.splitext(os.path.basename(file))[1]
        if fileType in IMAGETYPES:
            print(f"[SAVE]: {file}")
            images.append(file)
    return images

# Explore all sub-directories in a directory
def explore(root):
    images = []
    files = glob.glob(os.path.join(root, "*"))
    for file in files:
        if os.path.isdir(file):
            explore(file)
            images += getImages(file)
    return images

images = explore(path)
print(len(images))

# with open(os.path.join(save, "all_images_path.txt"), "w") as file:
#     file.write("\n".join(images))

# print("DONE!")
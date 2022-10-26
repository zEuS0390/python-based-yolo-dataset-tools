import os, glob, shutil, sys
from concurrent.futures import ThreadPoolExecutor

images_directory = input("Images directory: ")
labels_directory = input("Labels directory: ")
output_directory = input("Output directory: ")
train_percentage = 0.7
test_percentage = 0.2
valid_percentage = 0.1

if not os.path.exists(images_directory):
    print("Images directory does not exist!")
    sys.exit()
if not os.path.exists(labels_directory):
    print("Labels directory does not exist!")
    sys.exit()
if not os.path.exists(os.path.join(output_directory)):
    os.mkdir(os.path.join(output_directory))

images = glob.glob(os.path.normpath(os.path.join(images_directory, "*.jpg")))
count = len(images)

def collect(iterList):
    labeled_images = []
    while len(iterList) > 0:
        image_file = iterList.pop(0)
        text_file = os.path.normpath(os.path.join(labels_directory, ".".join([os.path.splitext(os.path.basename(image_file))[0], "txt"])))
        if os.path.exists(text_file):
            labeled_images.append({
                "image": image_file,
                "text": text_file
            })
        else:
            print(f"'{text_file}' not found")
    return labeled_images

def split(iterList, *percentages):
    countList = []
    for percentage in percentages:
        count = round(len(iterList)*percentage)
        countList.append(count)
    split_result = []
    for index in range(len(countList)):
        piece = []
        while countList[index] > 0:
            piece.append(iterList.pop(0))
            countList[index] -= 1
        split_result.append(piece)
    return split_result

images = collect(images)
print("-"*30)
print(f"original total images: {len(images)}")
train, test, valid = split(images, train_percentage, test_percentage, valid_percentage)
print("-"*30)
print(f"train ({train_percentage*100}%): {len(train)}")
print(f"test ({test_percentage*100}%): {len(test)}")
print(f"valid ({valid_percentage*100}%): {len(valid)}")
print(f"total (100%): {len(train)+len(test)+len(valid)}")
print("-"*30)

def copyTo(iterList, dir_name):
    total = 0
    if not os.path.exists(os.path.join(output_directory, dir_name)):
        os.mkdir(os.path.join(output_directory, dir_name))
        os.mkdir(os.path.join(output_directory, dir_name, "images"))
        os.mkdir(os.path.join(output_directory, dir_name, "labels"))
    if not os.path.exists(os.path.join(output_directory, dir_name)):
        os.mkdir(os.path.join(output_directory, dir_name))
    if not os.path.exists(os.path.join(output_directory, dir_name, "images")):
        os.mkdir(os.path.join(output_directory, dir_name, "images"))
    if not os.path.exists(os.path.join(output_directory, dir_name, "labels")):
        os.mkdir(os.path.join(output_directory, dir_name, "labels"))
    while len(iterList) > 0:
        labeled_image = iterList.pop()
        basename_image = os.path.basename(labeled_image["image"])
        basename_text = os.path.basename(labeled_image["text"])
        dest_image = os.path.normpath(os.path.join(output_directory, dir_name, "images", basename_image))
        dest_text = os.path.normpath(os.path.join(output_directory, dir_name, "labels", basename_text))
        shutil.copy2(labeled_image["image"], dest_image)
        shutil.copy2(labeled_image["text"], dest_text)
        print(f"{labeled_image} done.")
        total += 1
    return total

executor = ThreadPoolExecutor(max_workers=3)
future1 = executor.submit(copyTo, train, "train")
future2 = executor.submit(copyTo, test, "test")
future3 = executor.submit(copyTo, valid, "valid")
total = future1.result()+future2.result()+future3.result()
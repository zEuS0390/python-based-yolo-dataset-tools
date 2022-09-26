import cv2, os, glob, sys

class BoxValues:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def getBoxValues(image_width: int, image_height: int, yolo_format_value: BoxValues) -> BoxValues:
    topleft_x = int((yolo_format_value.x-yolo_format_value.width/2)*image_width)
    topleft_y = int((yolo_format_value.y-yolo_format_value.height/2)*image_height)
    box_width = int(yolo_format_value.width * image_width)
    box_height = int(yolo_format_value.height * image_height)
    return BoxValues(topleft_x, topleft_y, box_width, box_height)

images_directory = input("Images directory: ")
img_width = int(input("Image width in pixels: "))
img_height = int(input("Image height in pixels: "))
labels_directory = input("Labels directory: ")
classes_file = input("Classes text file: ")
output_directory = input("Output directory: ")
ncls = {}
success = True

if not os.path.exists(images_directory) or not os.path.isdir(images_directory):
    print("Invalid image directory.")
    sys.exit()

if not os.path.exists(labels_directory) or not os.path.isdir(labels_directory):
    print("Invalid labels directory.")
    sys.exit()

if not os.path.exists(classes_file) or not os.path.isfile(classes_file):
    print("Invalid classes text file.")
    sys.exit()

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

with open(classes_file, "r") as file:
    class_names = [line.strip() for line in file.readlines()]

img_labels = glob.glob(os.path.join(labels_directory, "*.txt"))
for img_label in img_labels:
    if os.path.splitext(os.path.basename(img_label))[0] == "classes":
        continue
    filename = os.path.splitext(os.path.basename(img_label))[0]
    img_file = os.path.normpath(os.path.join(images_directory, ".".join([filename, "jpg"])))
    if not os.path.exists(img_file):
        print(f"{img_file} does not exist. Fix the problem first and start again. Aborted.")
        success = False
        break
    img = cv2.imread(img_file)
    if img.shape[0] != img_height and img.shape[1] != img_width:
        print(f"{img_file}: Image size is not matched to {img_width}x{img_height}. Fix the problem first and start again. Aborted.")
        success = False
        break
    for cls in class_names:
        if not os.path.exists(os.path.join(output_directory, cls)):
            os.mkdir(os.path.join(output_directory, cls))
        ncls[cls] = 1
    with open(img_label, "r") as txt:
        lines = [line.strip() for line in txt.readlines()]
        for line in lines:
            values = line.split()
            class_name = class_names[int(values[0])]
            center_x = float(values[1])
            center_y = float(values[2])
            width = float(values[3])
            height = float(values[4])
            box_values = getBoxValues(img_width, img_height, BoxValues(center_x, center_y, width, height))
            cropped_image = img[box_values.y: box_values.y+box_values.height, box_values.x: box_values.x+box_values.width]
            cv2.imwrite(os.path.join(output_directory, class_name, f"{filename}_{class_name}_{ncls[class_name]}.jpg"), cropped_image)
            ncls[class_name] += 1
        
if success:
    print("Done.")
import os, cv2, datetime, threading

# Functions
# - list
# - move <box_id> 
# - manual-move <box_id> <pos_x> <pos_y>
# - create <size_width> <size_height>
# - manual-create <pos_x> <pos_y> <size_width> <size_height>
# - resize <box_index>
# - manual-resize <box_index> <size_width> <size_height>
# - delete <box_index>
# - save

outdir = "./output"
pos_clicked = [0, 0]
state_clicked = False
cam_status = True
frame = None

# Box Class
class Box:
    def __init__(self, x, y, w, h):
        self.pos = [self.x, self.y] = [x, y]
        self.size = [self.w, self.h] = [w, h]
    def __str__(self):
        return f"Box(x={self.pos[0]}, y={self.pos[1]}, w={self.size[0]}, h={self.size[1]})"

def onMouseCallback(event, x, y, flags, params, pos_clicked):
    global state_clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        pos_clicked[0] = x
        pos_clicked[1] = y
        state_clicked = True

# Camera function
def camera(source, boxes):
    global frame
    cap = cv2.VideoCapture(source)
    while cap.isOpened() and cam_status:
        _, frame = cap.read()
        viewFrame = frame.copy()
        for index, box in enumerate(boxes):
            topleft = box.pos
            bottomright = [sum(value) for value in zip(box.pos, box.size)]
            viewFrame = cv2.rectangle(viewFrame, topleft, bottomright, (0, 255, 0), 2)
            viewFrame =  cv2.putText(viewFrame, str(index), (topleft[0], topleft[1]), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        cv2.imshow("frame", viewFrame)
        cv2.setMouseCallback(
            'frame', 
            lambda event, x, y, flags, params: 
            onMouseCallback(event, x, y, flags, params, pos_clicked)
        )
        key = cv2.waitKey(100)
        # Terminate video capturing
        if key & 0xFF == ord('q'):
            break
        # Capture video frame
        elif key & 0xFF == ord('c'):
            filename = datetime.datetime.now().strftime(("%y%m%d_%H%M%S"))
            output_img = os.path.normpath(os.path.join(outdir, "images", ".".join([filename, "jpg"])))
            output_label = os.path.normpath(os.path.join(outdir, "labels", ".".join([filename, "txt"])))
            with open(output_label, "w") as file:
                for index, box in enumerate(boxes):
                    topleft = box.pos
                    box = topleft[0], topleft[1], box.size[0], box.size[1]
                    file.write(f"{box[0]} {box[1]} {box[2]} {box[3]}\n")    
            cv2.imwrite(output_img , frame)
    cap.release()
    cv2.destroyAllWindows()

# Control camera function
def cameraControl(boxes: list):
    global cam_status, state_clicked
    while cam_status:
        msg = input(">> ")
        # move <box_index>
        if msg.startswith("move"):
            try:
                args = msg.strip().split(" ")
                assert len(args) == 2
                index = int(args[1])
                print("Select a coordinate in the frame window.")
                while not state_clicked: pass
                boxes[index].pos[0] = pos_clicked[0]
                boxes[index].pos[1] = pos_clicked[1]
                state_clicked = False
            except Exception as e:
                print(e)
        # create <size_width> <size_height>
        elif msg.startswith("create"):
            try:
                args = msg.strip().split(" ")
                assert len(args) == 3
                size_width = int(args[1])
                size_height = int(args[2])
                print("Select a coordinate in the frame window.")
                while not state_clicked: pass
                box = Box(pos_clicked[0], pos_clicked[1], size_width, size_height)
                boxes.append(box)
                state_clicked = False
            except Exception as e:
                print(e)
        # resize <box_index>
        elif msg.startswith("resize"):
            try:
                args = msg.strip().split(" ")
                assert len(args) == 2
                index = int(args[1])
                print("Select a coordinate in the frame window.")
                while not state_clicked: pass
                boxes[index].size[0] = pos_clicked[0]-boxes[index].pos[0]
                boxes[index].size[1] = pos_clicked[1]-boxes[index].pos[1]
                state_clicked = False
            except Exception as e:
                print(e)
        # manual-resize <box_index> <size_width> <size_height>
        elif msg.startswith("manual-resize"):
            try:
                args = msg.strip().split(" ")
                assert len(args) == 4
                index = int(args[1])
                size_width = int(args[2])
                size_height = int(args[3])
                boxes[index].size[0] = size_width
                boxes[index].size[1] = size_height
            except Exception as e:
                print(e)
        # manual-move <box_index> <topleft_x> <topleft_y>
        elif msg.startswith("manual-move"):
            try:
                args = msg.strip().split(" ")
                assert len(args) == 4
                index = int(args[1])
                try:
                    x = int(args[2])
                    y = int(args[3])
                    boxes[index].pos[0] = x
                    boxes[index].pos[1] = y
                except Exception as e:
                    print(e)
            except:
                print("Invalid arguments.")
        # manual-create <topleft_x> <topleft_y> <size_width> <size_height>
        elif msg.startswith("manual-create"):
            try:
                args = msg.strip().split(" ")
                assert len(args) == 5
                topleft_x = int(args[1])
                topleft_y = int(args[2])
                size_width = int(args[3])
                size_height = int(args[4])
                box = Box(topleft_x, topleft_y, size_width, size_height)
                boxes.append(box)
                index = len(boxes)-1
            except:
                print("Invalid arguments.")
        # delete <box_index>
        elif msg.startswith("delete"):
            try:
                args = msg.strip().split(" ")
                assert len(args) == 2
                index = int(args[1])
                boxes.pop(index)
            except Exception as e:
                print(e)
        elif msg == "list":
            for index, box in enumerate(boxes):
                print(f"{index} - {box}")
        elif msg == "save":
            try:
                filename = datetime.datetime.now().strftime(("%y%m%d_%H%M%S"))
                output_img = os.path.normpath(os.path.join(outdir, "images", ".".join([filename, "jpg"])))
                output_label = os.path.normpath(os.path.join(outdir, "labels", ".".join([filename, "txt"])))
                with open(output_label, "w") as file:
                    for index, box in enumerate(boxes):
                        topleft = box.pos
                        box = topleft[0], topleft[1], box.size[0], box.size[1]
                        file.write(f"{box[0]} {box[1]} {box[2]} {box[3]}\n")    
                cv2.imwrite(output_img , frame)
                print(f"Saved {output_img} and {output_label}.")
            except Exception as e:
                print(e)
        elif msg == "exit":
            cam_status = False
        else:
            print(f"{msg} command not found.")

if __name__=="__main__":
    if not os.path.exists(outdir):
        os.mkdir(outdir)
        os.mkdir(os.path.normpath(os.path.join(outdir, "images")))
        os.mkdir(os.path.normpath(os.path.join(outdir, "labels")))
    if not os.path.exists(os.path.normpath(os.path.join(outdir, "images"))):
        os.mkdir(os.path.normpath(os.path.join(outdir, "images")))
    if not os.path.exists(os.path.normpath(os.path.join(outdir, "labels"))):
        os.mkdir(os.path.normpath(os.path.join(outdir, "labels")))
    boxes = [Box(0, 0, 50, 50)]
    controlThread = threading.Thread(target=cameraControl, args=(boxes,), daemon=True)
    controlThread.start()
    camera(0, boxes)
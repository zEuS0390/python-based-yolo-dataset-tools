import cv2, os, sys

video_filepath = input("Input video (mp4): ")
if not os.path.exists(video_filepath):
    print(f"{video_filepath} does not exist. Abort.")
    sys.exit()
output_dir = input("Output directory: ")
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
video_filename = os.path.splitext(os.path.basename(video_filepath))[0]
cap = cv2.VideoCapture(video_filepath)
assert cap.isOpened()
n = 1

while True:
    ret, frame = cap.read()
    if ret:
        if n % 10 == 0:
            frame = cv2.resize(frame, (640, 640), interpolation=cv2.INTER_AREA)
            img_filename = os.path.normpath(os.path.join(output_dir, '.'.join([video_filename + " (" + str(n//10) + ")", 'jpg'])))
            print(f"Frame {n}: Saving to {img_filename}. ", end="")
            cv2.imwrite(img_filename, frame)
            print("Done.")
        n += 1
    else:
        break
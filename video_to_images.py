from concurrent.futures import ThreadPoolExecutor
import cv2, os, glob, time

MAX_WORKERS = 2

videos_directory = input("Videos directory (mp4): ")
output_directory = input("Output directory: ")
frame_interval = int(input("Frame Interval: "))
width, height = 640, 640

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

video_files = glob.glob(os.path.join(videos_directory, "*.mp4"))
count = len(video_files)

def videoToImages(vid_file):
    total_frames = 0
    filename = os.path.splitext(os.path.basename(vid_file))[0]
    cur_dir = os.path.join(output_directory,filename)
    if not os.path.exists(cur_dir):
        os.mkdir(cur_dir)
    cap = cv2.VideoCapture(vid_file)
    assert cap.isOpened()
    n = 1
    while True:
        ret, frame = cap.read()
        if ret:
            if n % frame_interval == 0:
                frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
                # frame = cv2.rotate(frame, cv2.ROTATE_180)
                img_filename = os.path.normpath(os.path.join(cur_dir, ".".join([filename + f"({n//frame_interval})", "jpg"])))
                # print(f"Frame {n}: {filename}", end=" ")
                cv2.imwrite(img_filename, frame)
                # print("OK.")
                total_frames += 1
            n += 1
        else: 
            break
        time.sleep(0.01)
    cap.release()
    return total_frames

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = []
    total_frames = []
    for video_file in video_files: futures.append(executor.submit(videoToImages, video_file))
    print("Please wait...")
    for future in futures: total_frames.append(future.result())
    print("-"*30)
    print("Total Frames:")
    for index, result in enumerate(total_frames):
        print(f"\t- {os.path.splitext(os.path.basename(video_files[index]))[0]}: {result}")
    print("-"*30)
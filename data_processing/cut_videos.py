import cv2
import sys
import os
from tqdm import tqdm

#video_path = sys.argv[1]
#output = sys.argv[2]
#print("video path : " + str(video_path))
#print("output path : " + str(output))

#if not os.path.exists(output):
#    os.makedirs(output)
#    print(str(output) + " created")


def cut_by_frame(video_path):
    capture = cv2.VideoCapture(video_path)
    short_path = video_path.replace("./videos/", "")
    short_path = short_path.replace(".mp4", "")
    frame_id = 0
    while True:
        success, frame = capture.read()
        if success:
            cv2.imwrite("./output_1/" + short_path + "_" + f'{frame_id}.jpg', frame)
        else:
            break
        frame_id = frame_id + 1

    capture.release()


list_videos = os.listdir("./videos")
print(list_videos)

for i in tqdm(range(len(list_videos))):
    video_path = list_videos[i]
    cut_by_frame("./videos/" + video_path)

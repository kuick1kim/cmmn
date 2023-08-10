
import cv2
import numpy as np


def read_video(path):
    cap = cv2.VideoCapture(path)
    return cap


def play_video(path):
    Vid = cv2.VideoCapture(path)

    if Vid.isOpened():
        fps = Vid.get(cv2.CAP_PROP_FPS)
        f_count = Vid.get(cv2.CAP_PROP_FRAME_COUNT)
        f_width = Vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        f_height = Vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
        print('Frames per second : ', fps,'FPS')
        print('Frame count : ', f_count)
        print('Frame width : ', f_width)
        print('Frame height : ', f_height)
    
    while Vid.isOpened():
        ret, frame = Vid.read()
        if ret:
            re_frame = cv2.resize(frame, (round(f_width), round(f_height)))
            cv2.imshow('Car_Video',re_frame)
            key = cv2.waitKey(int(fps))            
            if key == ord('q'):
                break
        else:
            break

    Vid.release()
    cv2.destroyAllWindows()



#### 저장 베이직 세팅 VideoWriter
def save_video1(video_path, cap, output_size):
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter('%s_output.mp4' % (video_path.split('.')[0]), fourcc, cap.get(cv2.CAP_PROP_FPS), output_size)
    return out



##### 트래커 만들기
def create_tracker():
    tracker = cv2.TrackerCSRT_create()
    return tracker

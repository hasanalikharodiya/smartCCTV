import datetime
import cv2


def Video_Start(cap):
    # timer setting
    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=59)
    nowDatetime = start.strftime('%Y-%m-%d_%H:%M')
    print(nowDatetime)
    # video save setting
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(nowDatetime+'.avi', fourcc, 20.0, (640,480))
    
    while cap.isOpened():
        ret, frame = cap.read()
        out.write(frame)
        if(datetime.datetime.now() >= end):
            out.release()
            return 0
    


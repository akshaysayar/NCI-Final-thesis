
import cv2
import numpy as np
import os
import time
def process(input_dir, output_dirl, output_dirr, file):
    print(input_dir + str(file))
    cap = cv2.VideoCapture(input_dir + str(file))
    fps  = cap.get(cv2.CAP_PROP_POS_FRAMES)
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

    out_l = cv2.VideoWriter(output_dirl +  str(file)[:-4]+ "_left.avi"  ,fourcc, 31,(581,436))
    out_r = cv2.VideoWriter(output_dirr +  str(file)[:-4]+ "_right.avi" ,fourcc, 24, (581,436))
    start_time = time.time()
    c=0
    while cap.isOpened():
        c+=1
        ret, frame = cap.read()
        if ret:
            # roi = frame[232:668, 58:-60]
            roi1 = frame[232:668, 58:639]
            roi2 = frame[232:668, 639:-60]
            # cv2.imshow("roi1", roi1)
            # cv2.imshow("roi2", roi2)
            out_l.write(roi1)
            out_r.write(roi2)
        else:   
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break
            # if (0xFF & cv2.waitKey(5) == 27) or frame.size == 0:
            #     break
        if cv2.waitKey(15) & 0xFF == ord('q'): # Press 'Q' on the keyboard to exit the playback
            break
    
    cap.release()
    out_l.release()
    f_time = time.time()
    print(c/(f_time-start_time))
    cv2.destroyAllWindows()

input_dir = "C:\\Users\\aksha\\Documents\\Thesis\\Pupil_processed_3\\"
output_dirl = "C:\\Users\\aksha\\Documents\\Thesis\\Pupil_left_3\\"
output_dirr = "C:\\Users\\aksha\\Documents\\Thesis\\Pupil_right_3\\"
# input_dir =  "C:\\Users\\aksha\\Downloads\\trail\\"
# output_dir = "C:\\Users\\aksha\\Downloads\\trail\\"
files = [file for file in os.listdir(input_dir) if file.endswith(".mp4")]
# files = ['Aditya_pupil.mp4']
for file in files:
    print("\n\n\n\nstarted with  -  ",str(file))
    process(input_dir, output_dirl,output_dirr, file)
    print("finished with  -  ",str(file))
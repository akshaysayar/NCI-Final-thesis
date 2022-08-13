import time
import cv2
def process(input_dir, output_dirl):

    cap = cv2.VideoCapture(input_dir)

    fps  = cap.get(cv2.CAP_PROP_POS_FRAMES)
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    
    H  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    W  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    
    out_l = cv2.VideoWriter(output_dirl ,fourcc, 25,(W,H))

    start_time = time.time()
    c=0
    
    while cap.isOpened():
        c+=1
        ret, frame = cap.read()
        if ret:
            out_l.write(frame)
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break
           
        if cv2.waitKey(15) & 0xFF == ord('q'): # Press 'Q' on the keyboard to exit the playback
            break
    
    cap.release()
    out_l.release()
    f_time = time.time()
    print(f_time-start_time)
    cv2.destroyAllWindows()
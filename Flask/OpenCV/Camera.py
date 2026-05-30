from multiprocessing import Process, Queue, Event
import cv2
import numpy

import MultiProcess.EventBus as EventBus

def startCameraProcess(win_vec):
    print("Log: Camera has opened.")
    
    is_stop = False
    windows_name = "PWVrmVtuberStudio Camera (%d*%d)" %(win_vec[0], win_vec[1])

    cap = cv2.VideoCapture(0)
    # cap.set(3, frameWidth)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, win_vec[0])
    # cap.set(4, frameHeight)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, win_vec[1])
    # cap.set(10, 50)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 50)

    while True:
        key = cv2.waitKey(1) & 0xFF
        # Press ESC to exit camera.
        if key == 27:
            break
        
        success, img = cap.read()
        cv2.imshow(windows_name , img)
        
    # Exit
    cap.release()
    cv2.destroyAllWindows()

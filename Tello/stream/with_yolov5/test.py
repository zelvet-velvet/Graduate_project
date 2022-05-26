from threading import Thread
from djitellopy import Tello
import cv2, math, time
import os


tello = Tello()
tello.connect(False)
tello.streamon()
print(tello.get_udp_video_address())
print(type(tello.get_udp_video_address()))

bruh = tello.get_frame_read()


try:
    print("while ing")
    while True:
        img = bruh.frame
        #img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
except KeyboardInterrupt:
    exit(1)
finally:
    print("fin")




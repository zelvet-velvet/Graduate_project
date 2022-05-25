from threading import Thread
from djitellopy import Tello
import cv2, math, time
import torch
import os


tello = Tello()
tello.connect(False)
tello.streamon()
frame_read = tello.get_frame_read()


    
class VideoStreamWidget(object):
    def __init__(self, src=0):

        self.thread = Thread(target=self.update, args=())######
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        global frame
        while True:


            self.frame = cv2.cvtColor(frame_read.frame,cv2.COLOR_RGB2BGR)


            time.sleep(.01)

    def show_frame(self):

        cv2.imshow('frame', self.frame)
        

if __name__ == '__main__':
    video_stream_widget = VideoStreamWidget()
    time.sleep(1)
    while True:
        try:
            video_stream_widget.show_frame()
        except AttributeError:
            pass


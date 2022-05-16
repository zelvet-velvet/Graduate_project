
import cv2
import time
from djitellopy import Tello

tello = Tello()
tello.connect(False)



tello.streamon()
while True:
	img = tello.get_frame_read().frame
	cv2.imshow("Image",img)
	cv2.waitKey(1)


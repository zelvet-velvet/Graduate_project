                                                           
import threading
import asyncio
from djitellopy import Tello
import cv2, math, time
from threading import Thread
import numpy as np


img = cv2.imread('030..jpg')
WINDOW_NAME = '030'
cv2.imshow(WINDOW_NAME , img)


print("while process")
while True:
    key = cv2.waitKey(1) & 0xff
    if key == ord('x'):
        exit(1)

    


from threading import Thread
from djitellopy import Tello
import cv2, math, time
import torch
import os
import numpy as np
import asyncio
import imutils
from PIL import Image
from matplotlib import pyplot as plt


path = r'C:\yolov5-master'
model = torch.hub.load(path, 'yolov5s',source='local', pretrained=True)
"""
tello = Tello()
tello.connect()



tello.streamon()
frame_read = tello.get_frame_read()
"""
    



global frame
frame = cv2.imread('smol_Ina.jpg')
           
result = model(frame)
print(type(result))
cv2.imshow(  frame.permute(1, 2, 0)  )










#result = np.array(result)
#vale = torch.from_numpy(result)
#frame_resized = cv2.resize(vale, (960, 720),interpolation=cv2.INTER_LINEAR)
#print(type(frame_resized))
#print("weeew")
#cv2.imshow('frame', frame_resized)
key = cv2.waitKey(1)





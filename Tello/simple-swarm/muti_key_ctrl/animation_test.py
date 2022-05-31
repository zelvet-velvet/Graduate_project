from djitellopy import TelloSwarm
from djitellopy import Tello
import cv2, math, time , os
from threading import Thread
import threading
import asyncio
import numpy as np
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key, Controller





def cls():
    	os.system('cls')

a=""

ww="d "
nn="g "
ss=" h"
dd=" s"
ii=" w"
jj=" a"
mm=" t"
ll=" b"
A = "     a   "
B = "     q   "

def animate_frame():
    print("")               
    print("")               
    print("tello1            tello2")               
    print("")
    print("       "+ww+"                 "+ii+"         ") 
    print("                                    " )
    print("   "+nn+"  "+ss+"  "+dd+A+jj+"  "+mm+"  "+ll+B)


while True:
    cls()
    animate_frame()
    a=a+" "
    time.sleep(0.2)
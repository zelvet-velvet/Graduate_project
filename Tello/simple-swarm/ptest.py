from djitellopy import TelloSwarm
from djitellopy import Tello
import cv2, math, time
from threading import Thread
import threading
import asyncio
import numpy as np
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key, Controller





class movement(object):
    global press_list 
    press_list = []
    def __init__(self):   
        global y,t,k,r
        print("thread 1 begin")   
        t=""
        y=""
        try:
            keyboard.release('q')
            r=""
            while True:
                print("list:", end=" ")
                print (press_list)
                
                y=r
                print("r:"+r+" y:"+y+"      k:"+k+" t:"+t)
                if y != "" and y.replace("'","") in press_list:
                    print("wakuwaku")
                    press_list.remove(y.replace("'",""))
                    evt = y + "evt"
                    globals()[evt].clear()
                    k = ""
                
                if t is not "" and t.replace("'","") not in press_list:
                    print("wee")
                    press_list.extend(t.replace("'",""))
                    moving_Thread = t
                    evt = moving_Thread+"evt"
                    globals()[evt] = threading.Event()
                    globals()[evt].set()
                    print(globals()[evt].isSet())
                    globals()[moving_Thread] = Thread(target = self.move,daemon = True)
                    globals()[moving_Thread].start()
                    time.sleep(0.5)
                time.sleep(1)
                t = k
 

        except KeyboardInterrupt:
            exit(1)

    def move(self):
        z=k
        evt = z+"evt"
        while globals()[evt].isSet():
            print("tello move"+z)
            time.sleep(1)

a=0
b=0

def on_press(key):
    print(f"press{key}")
    global k,a
    if a is 0:
        k=""
        a=1
    elif a is 1:
        k = f"{key}"


def on_release(key):
    print(f"release{key}")
    global r,b
    if b == 0:
        r=""
        b=1
    elif b == 1:
        r = f"{key}"

# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()


if __name__ == '__main__':
    keyboard = Controller()
    time.sleep(1)
    keyboard.press('q')
    keyboard.release('q')
    time.sleep(1)
    print("start")
    moving = movement()
    keyboard_listener.join()
    pass


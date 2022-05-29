from djitellopy import TelloSwarm
from djitellopy import Tello
import cv2, math, time
from threading import Thread
import threading
import asyncio
import numpy as np
from pynput.keyboard import Listener as KeyboardListener


global p_or_r
global bruh
bruh = ""
a= ""
p_or_r = 0
press_list = []


class movement():
    def __init__(self):         
        print("thread 1 begin")   

        try:
            while True:
                print("wee")
                 f on_press.k != "" and on_press.k not in press_list:
                    press_list.extend(listen.on_press.k)
                    moving_Thread = listen.on_press.k
                    evt = moving_Thread+"evt"
                    self.locals()[evt] = threading.Event()
                    self.locals()[evt].set()
                    print(locals()[evt])
                    locals()[moving_Thread] = Thread(target = move,daemon = True)
                    locals()[moving_Thread].start()
                    on_press.k = ""
                    print("on_press is"+listen.on_press.k)

                if on_release.r != "" and on_release.r in press_list:
                    print("wakuwaku")
                    press_list.remove(listen.on_release.k)
                    locals()[evt] = listen.on_release.r + "evt"
                    evt.clear()
                time.sleep(1)


        except KeyboardInterrupt:
            exit(1)

    def move(self):
        z=on_press.k
        evt = z+"evt"
        while self.locals()[evt].isSet():
            print(z)
            time.sleep(1)

def on_press(key):
    print(f"press{key}")
    global k = f"{key}"

def on_release(key):
    print(f"release{key}"+f"{key}")
    global r = f"{key}"

# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()


if __name__ == '__main__':
    listening = listen()
    moving = listening .movement()
    keyboard_listener.join()
    pass

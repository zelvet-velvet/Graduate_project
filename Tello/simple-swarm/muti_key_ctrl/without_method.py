from djitellopy import TelloSwarm
from djitellopy import Tello
import cv2, math, time , os
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
        global y,t,k,r,press_repeat,press_list
        print("thread 1 begin")   
        t=""
        y=""
        try:
            keyboard.release('q')
            r = ""
            time.sleep(0.1)
            r_list.remove('q')
            press_repeat=[]
            while True:
                length = len(press_list)
                while length != 0:
                    if k.replace("'","") in press_repeat:
                        for x in press_list:
                            if x not in press_repeat:
                                k=x
                                break

                    if k is not "" and k.replace("'","") not in press_repeat:
                        press_repeat.extend(k.replace("'",""))
                        evt = k.replace("'","")+"evt"
                        globals()[evt] = threading.Event()
                        globals()[evt].set()
                        globals()[k.replace("'","")] = Thread(target = self.move,daemon = True)
                        globals()[k.replace("'","")].start()
                        time.sleep(0.5)
                        k = ""
                    length=length-1

                if len(r_list) and r_list[0] in press_list:
                    if r.replace("'","") is "" or len(press_list)==0 < len(r_list)!=0:
                        r = r_list[0]

                    try:
                        press_list.remove(r.replace("'",""))
                    except:
                        pass

                    try:
                        press_repeat.remove(r.replace("'",""))
                    except:
                        pass

                    try:
                        r_list.remove(r.replace("'",""))
                    except:
                        pass

                    evt = r.replace("'","") + "evt"
                    globals()[evt].clear()
                    r = ""
                    k = ""
                #print(press_list)
                #print(press_repeat)
                #print(r_list)
                time.sleep(0.2)

        except KeyboardInterrupt:
            exit(1)

    def move(self):
        z = k.replace("'","")
        evt = z + "evt"
        try:
            while globals()[evt].isSet():
                #print("move to "+z)
                time.sleep(0.35)
        except KeyboardInterrupt:
            exit(1)

a=0
b=0

def on_press(key):
    #print(f"press{key}")
    global k,a
    if a is 0:
        k=""
        a=1
    elif a is 1:
        k = f"{key}"
        if k.replace("'","") not in press_list:
            press_list.extend(k.replace("'",""))

def on_release(key):
    global r_list
    #print(f"release{key}")
    global r,b
    if b == 0:
        r=""
        b=1
        r_list = []
    elif b == 1:
        r = f"{key}"
        if r.replace("'","") not in r_list:
            r_list.extend(r.replace("'",""))

def cls():
    	os.system('cls')

def animation():
    global A , B , ww , nn , ss , dd , ii , jj , mm , ll
    A = "         "
    B = "         "
    while True:
        ww="  "
        nn="  "
        ss="  "
        dd="  "
        ii="  "
        jj="  "
        mm="  "
        ll="  "
        A = "         "
        B = "         "
        for x in press_list:
            action_name(x)
        cls()
        print("")               
        print("")               
        print("tello1            tello2")               
        print("")
        print("       "+ww+"                 "+ii+"         ") 
        print("                                    " )
        print("   "+nn+"  "+ss+"  "+dd+A+jj+"  "+mm+"  "+ll+B)
        print(press_list)
        print(r_list)
        print("k:"+k+"r:"+r)
        A = "         "
        B = "         "
        time.sleep(0.65)


def action_name(p):
    global A , B , ww , nn , ss , dd , ii , jj , mm , ll
    if p== 'q':
        A = "   CCW   "
    if p== 'e':
        A = "   CW    "
    if p== 'r':
        A = "   Up    "
    if p== 'f':
        A = "  Down   "
    if p== 't':
        A = " Takeoff "
    if p== 'g':
        A = "  Land   "

    if p=='u':
        B = "   CCW   "
    if p== 'o':
        B = "   CW    "
    if p== 'p':
        B = "   Up    "
    if p== ';':
        B = "  Down   "
    if p== '[':
        B = " Takeoff "
    if p== '"':
        B = "  Land   "

    if p== 'w':
        ww = "↑"
    if p== 'a':
        nn = "←"
    if p== 's':
        ss = "↓"
    if p== 'd':
        dd = "→"

    if p== 'i':
        ii = "↑"
    if p== 'j':
        jj = "←"
    if p== 'k':
        mm = "↓"
    if p== 'l':
        ll = "→"

                


# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()

animation_thread = Thread(target=animation,daemon = True)


if __name__ == '__main__':
    keyboard = Controller()
    time.sleep(0.5)
    keyboard.press('q')
    keyboard.release('q')
    time.sleep(0.5)

    print("start")
    animation_thread.start()
    moving = movement()
    time.sleep(1)
    keyboard_listener.join()


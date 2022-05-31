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

    def __init__(self):   
        global k,r,press_repeat,press_list
        press_list = []
        press_repeat = []
        print("class movement init")   
        press_response_thread = Thread(target=self.press_response,daemon = True)
        release_response_thread = Thread(target=self.release_response,daemon = True)
        press_response_thread.start()
        release_response_thread.start()
        #animation_thread.start()
        
        try:
            while True:
                print(press_list)
                print(press_repeat)
                print(r_list)
                print("pressing_key:"+pressing_key+"release_key:"+release_key+"        aa:"+str(aa)+"bb:"+str(bb))
            time.sleep(0.5)
        except KeyboardInterrupt:
            exit(1)
        


    def press_response(self):  
        global pressing_key,release_key,press_repeat,press_list
        pressing_key=""
        try:
            while True:
                if len(press_list)>len(press_repeat):
                    for x in press_list:
                        if x not in press_repeat:
                            pressing_key=x
                            break
                if pressing_key is not "" and pressing_key.replace("'","") not in press_repeat:
                    press_repeat.extend(pressing_key.replace("'",""))
                    evt = pressing_key.replace("'","")+"evt"
                    globals()[evt] = threading.Event()
                    globals()[evt].set()
                    globals()[pressing_key.replace("'","")] = Thread(target = self.move,daemon = True)
                    globals()[pressing_key.replace("'","")].start()
                    pressing_key = ""
                time.sleep(0.1)
        except KeyboardInterrupt:
            exit(1)

    def release_response(self): 
        global pressing_key,release_key,press_repeat,press_list
        while True:
            if len(r_list):
                if release_key.replace("'","") is "" or len(press_list) <= len(r_list):
                    release_key = r_list[0]

                evt = release_key.replace("'","") + "evt"
                try:
                    globals()[evt].clear()
                    press_list.remove(release_key.replace("'",""))
                    press_repeat.remove(release_key.replace("'",""))
                    r_list.remove(release_key.replace("'",""))
                except:
                    pass

            release_key = ""

            if len(press_list)==0 and len(press_repeat)!=0:
                for x in press_repeat:
                    evt = x.replace("'","") + "evt"
                    globals()[evt].clear()
                    press_repeat.remove(x.replace("'",""))

    def move(self):
        zz = pressing_key.replace("'","")
        evt = zz + "evt"
        try:
            while globals()[evt].isSet():
                #print("move to "+zz)
                time.sleep(0.5)
        except:
            pass



aa=0
bb=0

def on_press(key):
    global pressing_key,aa
    #print(f"press{key}")
    if aa is 0:
        pressing_key=""
        aa=1
    elif aa is 1:
        pressing_key = f"{key}"
        if pressing_key == '"\'"':
            pressing_key = "@"
        if pressing_key.replace("'","") not in press_list:
            press_list.extend(pressing_key.replace("'",""))



def on_release(key):
    global r_list,release_key,bb
    #print(f"release{key}")
    if bb == 0:
        release_key=""
        bb=1
        r_list = []
    elif bb == 1:
        release_key = f"{key}"
        if release_key == '"\'"':
            release_key = "@"
        if release_key.replace("'","") not in r_list:
            r_list.extend(release_key.replace("'",""))


def cls():
    	os.system('cls')

def animation():
    global A , B , ww , nn , ss , dd , ii , jj , mm , ll
    A = "         "
    B = "         "
    try:
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
            animate_frame()
            time.sleep(0.2)
    except KeyboardInterrupt:
        exit(1)

def animate_frame():              
    print("\n                       \n                       \ntello1              tello2")               
    print("\n       "+ww+"                 "+ii+"         \n") 
    print("   "+nn+"  "+ss+"  "+dd+A+jj+"  "+mm+"  "+ll+B)
    #print(press_list)
    #print(press_repeat)
    #print(r_list)
    #print("pressing_key:"+pressing_key+"release_key:"+release_key+"        aa:"+str(aa)+"bb:"+str(bb))

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
    if p== '@':
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
    pressing_keyboard = Controller()
    time.sleep(0.5)
    pressing_keyboard.press('q')
    pressing_keyboard.release('q')
    time.sleep(0.5)

    moving = movement()
    keyboard_listener.join()


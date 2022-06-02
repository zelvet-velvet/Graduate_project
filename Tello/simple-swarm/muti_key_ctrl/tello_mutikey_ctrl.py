from djitellopy import TelloSwarm
from djitellopy import Tello
import cv2, math, time , os
from threading import Thread
import threading
import asyncio
import numpy as np
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key, Controller


"""
swarm = TelloSwarm.fromIps([
    "192.168.137.205",
    "192.168.137.183"
])

#___ right side
swarm1 = TelloSwarm.fromIps([
    "192.168.137.205"
])

"""
#___ left side

swarm2 = TelloSwarm.fromIps([
    "192.168.137.82"
])


swarm2.connect(False)
time.sleep(2)
swarm2.query_battery()
print("ewe")

class movement(object):

    press_event = threading.Event()
    release_event = threading.Event()

    def __init__(self):   
        global k,r,press_repeat,press_list
        press_list = []
        press_repeat = []
        print("class movement init")   
        press_response_thread = Thread(target=self.press_response,daemon = True)
        release_response_thread = Thread(target=self.release_response,daemon = True)

        self.press_event.set()
        self.release_event.set()
        animation_event.set()

        press_response_thread.start()
        release_response_thread.start()
        #animation_thread.start()


        
        try:
            while True:
                print(press_list)
                print(press_repeat)
                #print("pressing_key:"+pressing_key+"release_key:"+release_key+"        aa:"+str(aa)+"bb:"+str(bb))
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.press_event.clear()
            self.release_event.clear()
            animation_event.clear()
            print("Fin")
            exit(1)
        


    def press_response(self):  
        global pressing_key,release_key,press_repeat,press_list
        pressing_key=""
        while self.press_event:
            pressing_key=""
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


    def release_response(self): 
        global pressing_key,release_key,press_repeat,press_list

        while self.release_event:
            if len(press_repeat)>len(press_list):
                for x in press_repeat:
                    if x not in press_list:
                        evt = x.replace("'","") + "evt"
                        globals()[evt].clear()
                        press_repeat.remove(x.replace("'",""))
                        if x in r_list:
                            r_list.remove(x.replace("'",""))
                        Thread(target=stop, args=()).start()


    def move(self):
        zz = pressing_key.replace("'","")
        print(zz+" move start")
        evt = zz + "evt"
        try:
            while globals()[evt].isSet() and self.press_event:
                moving(zz.replace("'",""))
                #print(evt+"move  "+zz)
                time.sleep(0.8)
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
        if pressing_key == "'t'":
            takeoff()
            pressing_key=""
        if pressing_key == "'['":
            takeoff2()
            pressing_key=""
        if pressing_key == "'g'":
            land()
            pressing_key=""
        if pressing_key == '"\'"':
            land2()
            pressing_key=""

        if pressing_key.replace("'","") not in press_list:
            press_list.extend(pressing_key.replace("'",""))



def on_release(key):
    global r_list,release_key,bb
    print(f"release{key}")
    if bb == 0:
        release_key=""
        bb=1
        r_list = []
    elif bb == 1:
        release_key = f"{key}"
        if release_key.replace("'","") in press_list:
            press_list.remove(release_key.replace("'",""))


def takeoff():
    swarm1.takeoff()
    pass

def land():
    swarm1.land()
    pass

def takeoff2():
    swarm2.takeoff()
    pass

def land2():
    swarm2.land()
    pass


def cls():
    	os.system('cls')


global animation_event
animation_event = threading.Event()
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


def moving(zz):
    if zz== 'q':
        Thread(target=rotate_clockwise, args=()).start()
    if zz== 'e':
        Thread(target=rotate_counter_clockwise, args=()).start()
    if zz== 'r':
        Thread(target=move_up, args=()).start()
    if zz== 'f':
        Thread(target=move_down, args=()).start()

    if zz=='u':
        Thread(target=rotate_clockwise2, args=()).start()
    if zz== 'o':
        Thread(target=rotate_counter_clockwise2, args=()).start()
    if zz== 'p':
        Thread(target=move_up2, args=()).start()
    if zz== ';':
        Thread(target=move_down2, args=()).start()


    if zz== 'w':
        print("move w")
        Thread(target=move_forward, args=()).start()
    if zz== 'a':
        print("move a")
        Thread(target=move_left, args=()).start()
    if zz== 's':
        print("move s")
        Thread(target=move_back, args=()).start()
    if zz== 'd':
        print("move d")
        Thread(target=move_right, args=()).start() 

    if zz== 'i':
        print("ewe")
        Thread(target=move_forward2, args=()).start()
    if zz== 'j':
        Thread(target=move_left2, args=()).start()
    if zz== 'k':
        Thread(target=move_back2, args=()).start()
    if zz== 'l':
        Thread(target=move_right2, args=()).start() 



axis_spd = 70
yaw_spd = 80
hieght_spd = 70
def move_forward():
    swarm1.send_rc_control(0,axis_spd,0,0)
    pass
def move_back():
    swarm1.send_rc_control(0,-axis_spd,0,0)
    pass
def move_left():
    swarm1.send_rc_control(axis_spd*-1,0,0,0)
    pass
def move_right():
    swarm1.send_rc_control(axis_spd,0,0,0)
    pass
def rotate_clockwise():
    swarm1.send_rc_control(0,0,0,-yaw_spd)
    pass
def rotate_counter_clockwise():
    swarm1.send_rc_control(0,0,0,yaw_spd)
    pass
def move_up():
    swarm1.send_rc_control(0,0,hieght_spd,0)
    pass
def move_down():
    swarm1.send_rc_control(0,0,hieght_spd*-1,0)
    pass


def move_forward2():
    swarm2.send_rc_control(0,axis_spd,0,0)
    pass
def move_back2():
    swarm2.send_rc_control(0,-axis_spd,0,0)
    pass
def move_left2():
    swarm2.send_rc_control(axis_spd*-1,0,0,0)
    pass
def move_right2():
    swarm2.send_rc_control(axis_spd,0,0,0)
    pass
def rotate_clockwise2():
    swarm2.send_rc_control(0,0,0,-yaw_spd)
    pass
def rotate_counter_clockwise2():
    swarm2.send_rc_control(0,0,0,yaw_spd)
    pass
def move_up2():
    swarm1.send_rc_control(0,0,hieght_spd,0)
    pass
def move_down2():
    swarm2.send_rc_control(0,0,hieght_spd*-1,0)
    pass

def stop():
    time.sleep(0.2)
    #swarm.send_rc_control(0,0,0,0)
    #swarm1.send_rc_control(0,0,0,0)
    swarm2.send_rc_control(0,0,0,0)
    pass

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


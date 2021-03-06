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


#___ left side

swarm2 = TelloSwarm.fromIps([
    "192.168.137.82"
])


swarm2.connect(False)
time.sleep(2)
swarm2.query_battery()
print("ewe")
"""
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
        swarm1_moving_thread = Thread(target=swarm1_moving,daemon = True)
        swarm2_moving_thread = Thread(target=swarm2_moving,daemon = True)

        self.press_event.set()
        self.release_event.set()
        animation_event.set()


        press_response_thread.start()
        release_response_thread.start()
        swarm1_moving_thread.start()
        swarm2_moving_thread.start()
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
            swarm1_moving_event.clear()
            swarm2_moving_event.clear()
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
        global pressing_key,release_key,press_repeat,press_list,stop

        while self.release_event:
            if len(press_repeat)>len(press_list):
                for x in press_repeat:
                    if x not in press_list:
                        evt = x.replace("'","") + "evt"
                        globals()[evt].clear()
                        moving(x,1)
                        press_repeat.remove(x.replace("'",""))
                        if x in r_list:
                            r_list.remove(x.replace("'",""))



    def move(self):
        zz = pressing_key.replace("'","")
        print(" "+zz+" move start")
        evt = zz + "evt"
        try:
            while globals()[evt].isSet() and self.press_event:
                moving(zz.replace("'",""),0)
                #print(evt+"move  "+zz)
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
        ww = "???"
    if p== 'a':
        nn = "???"
    if p== 's':
        ss = "???"
    if p== 'd':
        dd = "???"

    if p== 'i':
        ii = "???"
    if p== 'j':
        jj = "???"
    if p== 'k':
        mm = "???"
    if p== 'l':
        ll = "???"


def moving(zz,stop):
    global xxx,yyy,sss,ttt,xxx2,yyy2,sss2,ttt2
    axis_spd = 70
    yaw_spd = 80
    hieght_spd = 70
#-------------------swarm1-------------------#
    if stop == 0:
        if zz== 'q':
            yyy=-yaw_spd
        if zz== 'e':
            yyy=yaw_spd
    else:
        yyy=0
    if stop == 0:
        if zz== 'r':
            xxx=hieght_spd
        if zz== 'f':
            xxx=-hieght_spd
    else:
        xxx=0

    if stop == 0:
        if zz== 'w':
            ttt=axis_spd
        if zz== 's':
            ttt=-axis_spd
    else:
        ttt=0
    if stop == 0:
        if zz== 'a':
            sss=-axis_spd
        if zz== 'd':
            sss=axis_spd
    else:
        sss=0
#-------------------swarm2-------------------#
    if stop == 0:
        if zz=='u':
            yyy2=-yaw_spd
        if zz== 'o':
            yyy2=yaw_spd
    else:
        yyy2=0
    if stop == 0:
        if zz== 'p':
            xxx2=hieght_spd
        if zz== ';':
            xxx2=-hieght_spd
    else:
        xxx2=0


    if stop == 0:
        if zz== 'i':
            ttt2=axis_spd
        if zz== 'k':
            ttt2=-axis_spd
    else:
        ttt2=0
    if stop == 0:
        if zz== 'j':
            sss2=-axis_spd
        if zz== 'l':
            sss2=axis_spd
    else:
        sss2=0


swarm1_moving_event = threading.Event()
swarm2_moving_event = threading.Event()
swarm1_moving_event.set()
swarm2_moving_event.set()

def swarm1_moving():
    global sss,ttt,xxx,yyy
    sss=0
    ttt=0
    xxx=0
    yyy=0
    while swarm1_moving_event.isSet():
        #swarm1.send_rc_control(sss,ttt,xxx,yyy)
        print("swarm1: "+str(sss)+" , "+str(ttt)+" , "+str(xxx)+" , "+str(yyy))
        time.sleep(0.5)
    pass
def swarm2_moving():
    global sss2,ttt2,xxx2,yyy2
    sss2=0
    ttt2=0
    xxx2=0
    yyy2=0
    while swarm2_moving_event.isSet():
        #swarm2.send_rc_control(sss2,ttt2,xxx2,yyy2)
        print("swarm2: "+str(sss2)+" , "+str(ttt2)+" , "+str(xxx2)+" , "+str(yyy2))
        time.sleep(0.5)
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


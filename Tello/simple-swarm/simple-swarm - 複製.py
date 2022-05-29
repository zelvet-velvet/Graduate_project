from djitellopy import TelloSwarm
from djitellopy import Tello
import cv2, math, time
from threading import Thread
import threading
import asyncio
import numpy as np
from pynput.keyboard import Listener as KeyboardListener


swarm = TelloSwarm.fromIps([
    "192.168.137.218",
    "192.168.137.77"
])

#___ right side
swarm1 = TelloSwarm.fromIps([
    "192.168.137.218"
])


#___ left side

swarm2 = TelloSwarm.fromIps([
    "192.168.137.77"
])



def main():
    swarm.connect(False)
    time.sleep(2)
    swarm.query_battery()
    print("ewe")
    swarm_thread = Thread(target=swarm_key_ctrl, args=())
    swarm_thread.start()

global p_or_r
global bruh
bruh = ""
a= ""
p_or_r = 0
press_list = []

def swarm_key_ctrl():         
    print("thread 1 begin")   

    try:
        while True:
            if on_press.k != "" and on_press.k not in press_list:
                press_list.extend(on_press.k)
                moving_Thread = on_press.k
                global evt
                evt = moving_Thread+"evt"
                evt = threading.Event()
                moving_Thread+"evt".isSet()
                moving_Thread = Thread(target = move,daemon = True)
                moving_Thread.start()
            if on_release.k != "" and on_release.k in press_list:
                press_list.remove(on_release.k)
                evt = on_release.r + "evt"
                evt.clear()
    except KeyboardInterrupt:
        swarm1.land()
        swarm2.land()
        swarm1_thread.sleep(10)
        swarm2_thread.sleep(10)
        cv2.destroyAllWindows()
        exit(1)

def move():
    z=on_press.k
    while evt:
        acting(on_press.k)

def acting(x):

    second = 0.001
    bruh = int(second*1000)

    axis_spd = 100
    yaw_spd = 80
    hieght_spd = 100

    match x:
        case ord('x'):
            #self.capture.release()
            swarm1.land()
            swarm2.land()
            cv2.destroyAllWindows()
            exit(1)

#------------swarm1------------------------#

        case 'w':
            swarm1.send_rc_control(0,axis_spd,0,0)
            
        case 's':
            swarm1.send_rc_control(0,-axis_spd,0,0)
            
        case ord('a'):
            swarm1.send_rc_control(axis_spd*-1,0,0,0)
            
        case ord('d'):
            swarm1.send_rc_control(axis_spd,0,0,0)   
    
        case ord('r'):
            swarm1.send_rc_control(0,0,hieght_spd,0)
            
        case ord('f'):
            swarm1.send_rc_control(0,0,-hieght_spd,0)

        case ord('q'):
            swarm1.send_rc_control(0,0,0,-yaw_spd)
            bruh = int(60)

        case ord('e'):
            swarm1.send_rc_control(0,0,0,yaw_spd)
            bruh = int(60)   

        case ord('t'):
            swarm1.takeoff()
            time.sleep(3)
            
        case ord('g'):
            swarm1.land()
            time.sleep(3)   


#------------swarm1------------------------#

#------------swarm2------------------------#

        case ord('i'):
            swarm2.send_rc_control(0,axis_spd,0,0)
            
        case ord('k'):
            swarm2.send_rc_control(0,-axis_spd,0,0)
            
        case ord('j'):
            swarm2.send_rc_control(axis_spd*-1,0,0,0)
            
        case ord('l'):
            swarm2.send_rc_control(axis_spd,0,0,0)   
    
        case ord('p'):
            swarm2.send_rc_control(0,0,hieght_spd,0)
            
        case ord(';'):
            swarm2.send_rc_control(0,0,-hieght_spd,0)

        case ord('u'):
            swarm2.send_rc_control(0,0,0,-yaw_spd)
            bruh = int(60)

        case ord('o'):
            swarm2.send_rc_control(0,0,0,yaw_spd)
            bruh = int(60)   

        case ord('['):
            swarm2.takeoff()
            time.sleep(3)
            
        case ord("'"):
            swarm2.land()
            time.sleep(3)   

#------------swarm2------------------------#


        case ord('z'):
            cv2.destroyAllWindows()
   

        case 255:
            swarm.send_rc_control(0,0,0,0)

def on_press(key):
    print(f"press{key}")
    on_press.k = f"{key}"

def on_release(key):
    print(f"release{key}")
    on_release.r = f"{key}"





# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
keyboard_listener.join()
if __name__ == '__main__':
    main()
    pass

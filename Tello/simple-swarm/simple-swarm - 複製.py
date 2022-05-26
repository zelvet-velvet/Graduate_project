from djitellopy import TelloSwarm
from djitellopy import Tello
import cv2, math, time
from threading import Thread
import threading
import asyncio
import numpy as np


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



def swarm_key_ctrl():         
    global bruh
    global key
    print("thread 1 begin")   
    second = 0.001
    bruh = int(second*1000)
    img = cv2.imread('030..jpg')
    WINDOW_NAME = '030'
    cv2.imshow(WINDOW_NAME,img)

    axis_spd = 100
    yaw_spd = 80
    hieght_spd = 100
    try:
        print("while ing")
        while True:
            key = cv2.waitKey(bruh) & 0xff
            bruh = int(second*1000)
            acting(x)

    except KeyboardInterrupt:
        swarm1.land()
        swarm2.land()
        swarm1_thread.sleep(10)
        swarm2_thread.sleep(10)
        cv2.destroyAllWindows()
        exit(1)

def acting(x):
    match x:
        case ord('x'):
            #self.capture.release()
            swarm1.land()
            swarm2.land()
            cv2.destroyAllWindows()
            exit(1)

#------------swarm1------------------------#

        case ord('w'):
            swarm1.send_rc_control(0,axis_spd,0,0)
            if key-ord(
            
        case ord('s'):
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

               
if __name__ == '__main__':
    main()
    pass

from djitellopy import TelloSwarm
from djitellopy import Tello
import cv2, math, time
from threading import Thread
import threading
import asyncio
import numpy as np


img = cv2.imread('030..jpg')
WINDOW_NAME = '030'
cv2.imshow(WINDOW_NAME,img)
key = cv2.waitKey(1)

swarm = TelloSwarm.fromIps([
    "192.168.137.220",
    "192.168.137.7"
])
#right_side
swarm1 = TelloSwarm.fromIps([
    "192.168.137.220"
])
#left_side
swarm2 = TelloSwarm.fromIps([
    "192.168.137.7"
])

swarm.connect(False)
swarm.query_battery()
#swarm.takeoff()


#----------------------swarm1-------------------------------------#


def land1():
    swarm1.land()
    pass

def move_forward1():
    swarm1.send_rc_control(0,axis_spd,0,0)
    pass

def move_back1():
    swarm1.send_rc_control(0,-axis_spd,0,0)
    pass

def move_left1():
    swarm1.send_rc_control(axis_spd*-1,0,0,0)
    pass

def move_right1():
    swarm1.send_rc_control(axis_spd,0,0,0)
    pass
    
def rotate_clockwise1():
    swarm1.send_rc_control(0,0,0,-yaw_spd)
    pass

def rotate_counter_clockwise1():
    swarm1.send_rc_control(0,0,0,yaw_spd)
    pass

def move_up1():
    swarm1.send_rc_control(0,0,hieght_spd,0)
    pass

def move_down1():
    swarm1.send_rc_control(0,0,hieght_spd*-1,0)
    pass


def swarm1_key_ctrl1():            
    second = 0.001
    bruh = int(second*1000)

    while True:
        try:
            key = cv2.waitKey(bruh) & 0xff
            bruh = int(second*1000)
            if key == ord('x'):
                #self.capture.release()
                Thread(target=land1, args=()).start()
                cv2.destroyAllWindows()
                exit(1)
            
            elif key == ord('w'):
                Thread(target=move_forward1, args=()).start()
            
            elif key == ord('s'):
                Thread(target=move_back1, args=()).start()
            
            elif key == ord('a'):
                Thread(target=move_left1, args=()).start()
            
            elif key == ord('d'):
                Thread(target=move_right1, args=()).start()     
    
            elif key == ord('r'):
                Thread(target=move_up1, args=()).start()
            
            elif key == ord('f'):
                Thread(target=move_down1, args=()).start()

            elif key == ord('q'):
                Thread(target=rotate_clockwise1, args=()).start()
                bruh = int(60)

            elif key == ord('e'):
                Thread(target=rotate_counter_clockwise1, args=()).start()
                bruh = int(60)           

            if key == 255 :
               swarm1.send_rc_control(0,0,0,0)
        except KeyboardInterrupt:
            break
    exit(1)
#----------------------swarm1-------------------------------------#


#----------------------swarm2-------------------------------------#


def land2():
    swarm2.land()
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
    swarm2.send_rc_control(0,0,hieght_spd,0)
    pass

def move_down2():
    swarm2.send_rc_control(0,0,hieght_spd*-1,0)
    pass


def swarm2_key_ctrl():            
    second = 0.001
    bruh = int(second*1000)

    while True:
        try:
            key = cv2.waitKey(bruh) & 0xff
            bruh = int(second*1000)
            if key == ord('x'):
                Thread(target=land2, args=()).start()
                Thread(target=land1, args=()).start()
                swarm1_thread.sleep(True)
                swarm2_thread.sleep(True)
                cv2.destroyAllWindows()
                exit(1)
            
            elif key == ord('i'):
                Thread(target=move_forward2, args=()).start()
            
            elif key == ord('k'):
                Thread(target=move_back2, args=()).start()
            
            elif key == ord('j'):
                Thread(target=move_left2, args=()).start()
            
            elif key == ord('l'):
                Thread(target=move_right2, args=()).start()     
    
            elif key == ord('p'):
                Thread(target=move_up2, args=()).start()
            
            elif key == ord(';'):
                Thread(target=move_down2, args=()).start()

            elif key == ord('u'):
                Thread(target=rotate_clockwise2, args=()).start()
                bruh = int(60)

            elif key == ord('o'):
                Thread(target=rotate_counter_clockwise2, args=()).start()
                bruh = int(60)           

            if key == 255 :
               swarm2.send_rc_control(0,0,0,0)
        except KeyboardInterrupt:
            Thread(target=land2, args=()).start()
            Thread(target=land1, args=()).start()
            swarm1_thread.sleep(True)
            swarm2_thread.sleep(True)
            cv2.destroyAllWindows()
            exit(1)

#----------------------swarm2-------------------------------------#

if __name__ == '__main__':
    swarm2_thread = Thread(target=swarm2_key_ctrl, args=(),daemon = True)
    swarm1_thread = Thread(target=swarm1_key_ctrl, args=(),daemon = True)
    print("Two thread start")
    swarm2_thread.start()
    swarm1_thread.start()


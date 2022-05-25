
import threading
import asyncio
from djitellopy import Tello
import cv2, math, time
from threading import Thread
import numpy as np


tello = Tello()
tello.connect(False)
#send_rc_control(self, left_right_velocity: int, forward_backward_velocity: int, up_down_velocity: int,yaw_velocity: int):

img = cv2.imread('030..jpg')
WINDOW_NAME = '030'
cv2.imshow(WINDOW_NAME,img)

global axis_spd 
global yaw_spd

axis_spd = 100
yaw_spd = 80
hieght_spd = 100

def takeoff():
    tello.takeoff()
    pass

def land():
    tello.land()
    pass

def move_forward():
    tello.send_rc_control(0,axis_spd,0,0)
    pass

def move_back():
    tello.send_rc_control(0,-axis_spd,0,0)
    pass

def move_left():
    tello.send_rc_control(axis_spd*-1,0,0,0)
    pass

def move_right():
    tello.send_rc_control(axis_spd,0,0,0)
    pass
    
def rotate_clockwise():
    tello.send_rc_control(0,0,0,-yaw_spd)
    pass

def rotate_counter_clockwise():
    tello.send_rc_control(0,0,0,yaw_spd)
    pass

def move_up():
    tello.send_rc_control(0,0,hieght_spd,0)
    pass

def move_down():
    tello.send_rc_control(0,0,hieght_spd*-1,0)
    pass


def main():            
    second = 0.001
    bruh = int(second*1000)

    while True:
        try:
            key = cv2.waitKey(bruh) & 0xff
            bruh = int(second*1000)
            if key == ord('x'):
                #self.capture.release()
                Thread(target=land, args=()).start()
                cv2.destroyAllWindows()
                exit(1)
            
            elif key == ord('w'):
                Thread(target=move_forward, args=()).start()
            
            elif key == ord('s'):
                Thread(target=move_back, args=()).start()
            
            elif key == ord('a'):
                Thread(target=move_left, args=()).start()
            
            elif key == ord('d'):
                Thread(target=move_right, args=()).start()     
    
            elif key == ord('r'):
                Thread(target=move_up, args=()).start()
            
            elif key == ord('f'):
                Thread(target=move_down, args=()).start()

            elif key == ord('q'):
                Thread(target=rotate_clockwise, args=()).start()
                bruh = int(60)

            elif key == ord('e'):
                Thread(target=rotate_counter_clockwise, args=()).start()
                bruh = int(60)           

            elif key == ord('t'):
                Thread(target=takeoff, args=()).start()
                time.sleep(3)
            
            elif key == ord('l'):
                Thread(target=land, args=()).start()
                time.sleep(3)

            if key == 255 :
               tello.send_rc_control(0,0,0,0)
        except KeyboardInterrupt:
            break
    exit(1)
        


if __name__ == '__main__':
    main()
    time.sleep(1)


 

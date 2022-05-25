from djitellopy import TelloSwarm
from djitellopy import Tello
import cv2, math, time
from threading import Thread

img = cv2.imread('030..jpg')
WINDOW_NAME = '030'
cv2.imshow(WINDOW_NAME,img)


swarm = TelloSwarm.fromIps([
    "192.168.137.159",
    "192.168.137.220"
])
#right_side
swarm1 = TelloSwarm.fromIps([
    "192.168.137.220"
])
#left_side
swarm2 = TelloSwarm.fromIps([
    "192.168.137.159"
])

swarm.connect(False)
swarm.query_battery()
swarm.takeoff()

# run in parallel on all tellos
def scheduling():

    axis_spd = 100
    axis_spd = 100
    yaw_spd = 80
    hieght_spd = 100

    swarm1.send_rc_control(0,0,0,-yaw_spd)
    swarm2.send_rc_control(0,0,0,yaw_spd)
    time.sleep(1)
    tello.send_rc_control(0,0,0,0)

    
    
    
    
    
    
    
    
    """
    swarm.move_up(20)
    swarm1.rotate_clockwise(90)
    swarm2.rotate_counter_clockwise(90)
    swarm.curve_xyz_speed(70, 70, 0, 100, 0, 0, 20)
    swarm.rotate_counter_clockwise(90)
    swarm1.go_xyz_speed(0,50,-50,20)
    swarm2.go_xyz_speed(0,50,50,20)
    swarm1.go_xyz_speed(-50,0,50,20)
    swarm2.go_xyz_speed(-50,0,-50,20)
    swarm.flip_left()
    swarm.go_xyz_speed(50,50,0,20)
    swarm2.rotate_clockwise(180)
    swarm.flip_back()
    """

def key():
    key = cv2.waitKey(1) & 0xff
    while True:
        try:
            if key == ord('x'):
                #self.capture.release()
                scheduling_thread.sleep(True)
                swarm.land()
                swarm.end()
                exit(1)
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    key_thread = Thread(target=key, args=())
    key_thread.start()
    scheduling_thread = Thread(target=scheduling, args=())
    scheduling_thread.start()
    time.sleep(1)


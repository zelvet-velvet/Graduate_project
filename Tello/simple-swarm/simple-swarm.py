from djitellopy import TelloSwarm
from djitellopy import Tello

import cv2, math, time


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
# 同时在所有Tello上执行
swarm.move_up(20)
swarm1.rotate_clockwise(90)
swarm2.rotate_counter_clockwise(90)
swarm.curve_xyz_speed(70, 70, 0, 100, 0, 0, 20)
swarm.rotate_counter_clockwise(90)
swarm1.go_xyz_speed(0,50,-50,20)
swarm2.go_xyz_speed(0,50,50,20)
# swarm2.rotate_clockwise(180)
swarm1.go_xyz_speed(-50,0,50,20)
swarm2.go_xyz_speed(-50,0,-50,20)
swarm.flip_left()
swarm.go_xyz_speed(50,50,0,20)
swarm2.rotate_clockwise(180)
swarm.flip_back()



key = cv2.waitKey(1) & 0xff
if key == ord('o'):
    swarm.emergency()

# swarm.sequential(lambda i, tello: tello.move_back(20))

swarm.land()
swarm.end()

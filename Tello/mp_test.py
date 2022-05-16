from djitellopy import Tello
import threading 

tello = Tello()

tello.connect(False)

print("Press enter to takeoff")
a=input()
tello.takeoff()

def r():
	tello.rotate_clockwise(360)
def Revolution():
	tello.curve_xyz_speed(25, -25, 0, 25, -75, 0, 20 )
	
tello.curve_xyz_speed(25, -25, 0, 25, -75, 0, 20 )
"""
print("Press enter to begin.")
a=input()
tello.go_xyz_speed(30,30,20,40)


print("Press enter to fly in revolution")
a=input()
rotate = threading.Thread(target = r)
ravolution = threading.Thread(target = Revolution)


ravolution.start()
rotate.start()

ravolution.join()
rotate.join()
"""

print("Press enter to land.")
a=input()
tello.land()

from djitellopy import Tello

tello = Tello()

tello.connect(False)


print("Press enter to takeoff")
a=input()
tello.takeoff()

print("Press enter to flip left")
a=input()
tello.flip_left()

print("Press enter to land")
a=input()
tello.land()





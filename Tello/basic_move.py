

from djitellopy import Tello

tello = Tello()

tello.connect(False)

print("Press enter to takeoff.")
a=input()
tello.takeoff()
tello.move_up(20)

print("Press enter to move forward and get back.")
a=input()
tello.move_forward(35)
tello.move_back(35)


print("Press enter to move right and get back.")
a=input()
tello.move_right(35)
tello.move_left(35)


print("Press enter to land.")
a=input()
tello.land()


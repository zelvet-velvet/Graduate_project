from djitellopy import Tello

tello = Tello()

tello.connect(False)

print("Press enter to continue")
a=input()

print("Press enter to takeoff")
a=input()
tello.takeoff()


print("Press enter to flip forward")
a=input()
tello.flip(f)			# direction: l (left), r (right), f (forward) or b (back)


print("Press enter to move forward")
a=input()
tello.move_forward(180) 	# (cm)

print("Press enter to move up")
a=input()
tello.move(up, 50)
"""direction: up, down, left, right, forward or back
   x: 20-500				"""

print("Press enter to rotate counter clockwise")
a=input()
tello.rotate_counter_clockwise(360)	#degree

print("Press enter to flip backward")
a=input()
tello.flip(b)

print("Press enter to land")
a=input()
tello.land()





from djitellopy import Tello

tello = Tello()

tello.connect(False)

print("Press enter to continue")
a=input( end = '')

print("Press enter to takeoff")
a=input()
tello.takeoff(end = '')


print("Press enter to flip forward")
a=input(end = '')
tello.flip(self,f)			# direction: l (left), r (right), f (forward) or b (back)


print("Press enter to move forward")
a=input(end = '')
tello.move_forward(180) 	# (cm)

print("Press enter to move up")
a=input(end = '')
tello.move(self,up, 50)
"""direction: up, down, left, right, forward or back
   x: 20-500				"""

print("Press enter to rotate counter clockwise")
a=input(end = '')
tello.rotate_counter_clockwise(360)	#degree

print("Press enter to flip backward")
a=input(end = '')
tello.flip(self,b)

print("Press enter to land")
a=input(end = '')
tello.land()





from djitellopy import Tello

tello = Tello()

tello.connect()

print("Press enter to continue")
a=input()

print("Press enter to takeoff")
a=input()
tello.takeoff()


print("Press enter to flip forward")
a=input()
flip(self,f)			# direction: l (left), r (right), f (forward) or b (back)


print("Press enter to move forward")
a=input()
tello.move_forward(100) 	# (cm)

print("Press enter to move up")
a=input
move(self,up, 100)
"""direction: up, down, left, right, forward or back
   x: 20-500				"""

print("Press enter to rotate counter clockwise")
a=input()
tello.rotate_counter_clockwise(180)	#degree

print("Press enter to flip backward")
a=input()
flip(self,b)

print("Press enter to land")
a=input()
tello.land()





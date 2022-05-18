from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
	"192.168.0.166"
	"192.168.0.101"
])
print("Press enter to takeoff")
a=input()
swarm.connect(False)

print("Press enter to takeoff")
a=input()
swarm.takeoff()
print("Press enter to land")
a=input()
swarm.land()
swarm.end()
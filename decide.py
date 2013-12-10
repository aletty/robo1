from predict import *
from models import *
import time

def decide(my_boat,enemy_boat,buoy_list):

	dangers = []
	actions = zip(2*range(15),15*[5,9])
	for rud, thrust in actions:
		head, pos = look_ahead(my_boat, my_boat.angleMap[rud], thrust)
		dangers.append(danger(pos, enemy_boat.position, buoy_list)) 
	
	# print dangers
	minIndex = min(xrange(len(dangers)),key=dangers.__getitem__)
	rudder, thrust = actions[minIndex]
	print "rudder: %s thrust: %s" % (rudder, thrust)
	return rudder, thrust

if __name__ == "__main__":
	boatB = Boat("Beth","G")
	boatD = Boat("Deborah","G")
	time.sleep(7)
	boatB.update((41,1173),1)
	boatD.update((500,500),1.1)
	# print boatB.speed
	# print boatD.speed

	buoys = []
	for i,pos in enumerate([(825, 415), (637, 850), (230,774), (232, 293)]):
		b = Buoy("%s" % i)
		b.position = pos
		buoys.append(b)

	print decide(boatB, boatD, buoys)
	# boat = Boat()

	# b = Boat('beth','L')
	# for i in xrange(2):
	# 	time.sleep(1)
	# 	b.update((0,i+1),0)
	# print b
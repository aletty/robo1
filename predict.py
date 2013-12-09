from models import *
import math

# predicts the boat's future state given it's current state
#   boat:   a boat object
#   rudder: the rudder position in radians
#   thrust: the thrust of the propellers on a scale of 0 to 15 (7 is neutral)
#   dt:     time to simulate in milliseconds
def look_ahead(boat, rudder, thrust, dt = 100):
  # calculate the circle
  arc_len = boat.speed*dt
  
  # catch the case that the rudder angle is really small
  if abs(rudder < .1):
    #calculate change in heading
    theta = 0
    #calculate change in position
    dl = arc_len

  else:
    #calculate change in heading
    rad = 1/(rudder*.1)#TODO figure out what this number really is
    theta = arc_len/rad
    #calculate change in position
    dl = 2*rad*math.sin(theta/2)

  dx = dl*math.sin(boat.heading + theta)
  dy = dl*math.cos(boat.heading + theta)

  # calculate the new state
  new_heading = theta + boat.heading
  new_position = boat.position[0] + dx, boat.position[1] + dy

def danger(my_boat, enemy_boat, buoy_list):
  pass


  return new_heading, new_position

if __name__ == "__main__":
  myBoat = Boat('beth', 'L')
  myBoat.speed = .4
  myBoat.position = (0,0)
  myBoat.heading = 0
  print look_ahead(myBoat,.1
  myBoat.heading,1)

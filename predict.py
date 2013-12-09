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
    rad = 1/(abs(rudder)*-6.91e-4)#TODO figure out what this number really is
    theta = arc_len/rad
    #calculate change in position
    dl = 2*rad*math.sin(theta/2)

  dx = dl*math.sin(boat.heading + theta)
  dy = dl*math.cos(boat.heading + theta)

  # calculate the new state
  new_heading = theta + boat.heading
  new_position = boat.position[0] + dx, boat.position[1] + dy

  return new_heading, new_position

def danger(my_boat, enemy_boat, buoy_list):
  x = my_boat.position[0] - enemy_boat.position[0]
  y = my_boat.position[1] - enemy_boat.position[1]
  
  r = math.sqrt(x**2 + y**2)
  theta = math.atan(y/x) - math.pi/2
  if x < 0
    theta += math.pi

  dist = r*theta/math.sin(theta)

  danger = math.exp(-dist**2/100000) + \
           math.exp(-R/20000)

  for b in buoy_list:
    danger += math.tanh(math.exp((-(my_boat.position[0]-b.position[0])**2 - (my_boat.position[1]-b.position[1])**2)/2000))

  

if __name__ == "__main__":
  myBoat = Boat('beth', 'L')
  myBoat.speed = .4
  myBoat.position = (0,0)
  myBoat.heading = 0
  print look_ahead(myBoat,.1
  myBoat.heading,1)

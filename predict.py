from models import *
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

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

def danger(my_boat_pos, enemy_boat_pos, buoy_list):
  x = my_boat_pos[0] - enemy_boat_pos[0]
  y = my_boat_pos[1] - enemy_boat_pos[1]
  
  print x
  print type(x)
  
  r = np.sqrt(x**2 + y**2)
  theta = np.arctan(y/x) - np.pi/2 + (x < 0)*np.pi
  #if (x < 0):
  #  theta += np.pi

  dist = r*theta/np.sin(theta)

  # danger near enemy boat
  danger = np.exp(-dist**2/100000) + \
           np.exp(-np.sqrt(x**2+y**2)/20000)

  # danger near buoy
  for b in buoy_list:
    danger += np.tanh(np.exp((-(my_boat_pos[0]-b.position[0])**2 - (my_boat_pos[1]-b.position[1])**2)/800))

  # danger near pool edge
  pc = (680, 516)
  danger += np.exp(-(np.sqrt((my_boat_pos[0]-pc[0])**2 + (my_boat_pos[1]-pc[1])**2) - 600)**2/1000)
  return danger
  

if __name__ == "__main__":
  myBoat = Boat('beth', 'L')
  myBoat.speed = .4
  myBoat.position = (300.5,300.5)
  myBoat.heading = 0
  print look_ahead(myBoat,.1,1)

  fig = plt.figure()
  ax = fig.gca(projection='3d')
  X = np.arange(0, 1500, 10)
  Y = np.arange(0, 1500, 10)
  X, Y = np.meshgrid(X, Y)
  R = danger((X, Y), (300.5, 300.5),[])
  surf = ax.plot_surface(X, Y, R, rstride=1, cstride=1, cmap=cm.coolwarm,
          linewidth=0, antialiased=False)
  ax.set_zlim(-1.01, 1.01)
  plt.show()




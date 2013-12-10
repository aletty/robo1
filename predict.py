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
def look_ahead(boat, rudder, thrust, dt = .1):
  # calculate the circle
  arc_len = boat.speed*dt*math.copysign(1, thrust-7)
  
  # catch the case that the rudder angle is really small
  if abs(rudder) < .1:
    #calculate change in heading
    theta = 0
    #calculate change in position
    dl = arc_len

  else:
    #calculate change in heading
    rad = 1/(abs(rudder)*6.91e-4)
    theta = arc_len/rad
    #calculate change in position
    dl = 2*rad*math.sin(theta/2)


  dx = -dl*math.cos(boat.heading - math.copysign(1,rudder)*theta/2)
  dy = dl*math.sin(boat.heading - math.copysign(1,rudder)*theta/2)
  # dy = math.cos(boat.heading - theta/2)
  # dx_temp = dl*math.sin(math.pi/2 - theta)
  # dy_temp = -dl*math.cos(math.pi/2 - theta)
  # dx = math.cos(theta)*dx_temp - math.sin(theta)*dy_temp
  # dy = math.sin(theta)*dx_temp + math.cos(theta)*dy_temp

  # calculate the new state
  new_heading = theta - boat.heading
  new_position = boat.position[0] + dx, boat.position[1] + dy

  return new_heading, new_position

def np_danger(my_boat_pos, enemy_boat_pos, buoy_list):
  # position relative to enemy boat
  x = my_boat_pos[0] - enemy_boat_pos[0]
  y = my_boat_pos[1] - enemy_boat_pos[1]
  r = np.sqrt(x**2 + y**2)
  theta = np.arctan(y/x) - np.pi/2 + (x < 0)*np.pi
  dist = r*theta/np.sin(theta)

  # danger near enemy boat
  enemy_danger = 0
  print np.exp(-dist**2/100000)
  enemy_danger = .5*np.exp(-dist**2/100000) + \
           .5*np.exp(-(x**2 + y**2)/20000)

  # danger near buoy
  buoy_danger = 0
  for b in buoy_list:
    x, y = my_boat_pos[0]-b.position[0], my_boat_pos[1]-b.position[1]
    buoy_danger += np.tanh(10*np.exp(-(x**2 + y**2)/1500))

  # danger near pool edge
  pc = (492, 525)
  x, y = my_boat_pos[0]-pc[0], my_boat_pos[1]-pc[1]
  distToEdge = np.sqrt(x**2 + y**2) - 530
  pool_danger = (distToEdge)/30 # np.exp(-distToEdge**2/1000)
  pool_danger = (np.tanh(pool_danger)+1)/2
  
  # danger near the cloud
  cloud_danger = (1-np.tanh((my_boat_pos[0]-200)/50))/2

  # find the real danger
  return np.maximum(np.maximum(1.3*enemy_danger, .8*buoy_danger), np.maximum(pool_danger, cloud_danger))

def danger(my_boat_pos, enemy_boat_pos, buoy_list):
# position relative to enemy boat
  x = my_boat_pos[0] - enemy_boat_pos[0]
  y = my_boat_pos[1] - enemy_boat_pos[1]
  r = math.sqrt(x**2 + y**2)
  theta = math.atan(y/x) - math.pi/2 + (x < 0)*math.pi
  dist = r*theta/math.sin(theta)

  # danger near enemy boat
  enemy_danger = 0
  print math.exp(-dist**2/100000)
  enemy_danger = .5*math.exp(-dist**2/100000) + \
           .5*math.exp(-(x**2 + y**2)/20000)

  # danger near buoy
  buoy_danger = 0
  for b in buoy_list:
    x, y = my_boat_pos[0]-b.position[0], my_boat_pos[1]-b.position[1]
    buoy_danger += math.tanh(10*math.exp(-(x**2 + y**2)/1500))

  # danger near pool edge
  pc = (492, 525)
  x, y = my_boat_pos[0]-pc[0], my_boat_pos[1]-pc[1]
  distToEdge = math.sqrt(x**2 + y**2) - 530
  pool_danger = (distToEdge)/30 # math.exp(-distToEdge**2/1000)
  pool_danger = (math.tanh(pool_danger)+1)/2

  # danger near the cloud
  cloud_danger = (1-np.tanh((my_boat_pos[0]-200)/50))/2

  # find the real danger
  return max(1.3*enemy_danger, .8*buoy_danger, pool_danger, cloud_danger) 


if __name__ == "__main__":
  myBoat = Boat('beth', 'L')
  myBoat.speed = 15
  myBoat.position = (300.5,300.5)
  myBoat.heading = 3*math.pi/2
  print look_ahead(myBoat,.1,1)

  # buoys = []
  # for i,pos in enumerate([(229, 295), (220, 778), (629, 860), (827, 405)]):
  #   b = Buoy("%s" % i)
  #   b.position = pos
  #   buoys.append(b)

  # print danger((100,100),(300,300),buoys)
  # fig = plt.figure()
  # ax = fig.gca(projection='3d')
  # # X = np.arange(0, 1032, 10)
  # # Y = np.arange(0, 1032, 10)
  # X = np.arange(-100, 1132, 10)
  # Y = np.arange(-100, 1132, 10)
  # X, Y = np.meshgrid(X, Y)
  # R = np_danger((X, Y), (680+.1, 516+.1),buoys)
  # surf = ax.plot_surface(X, Y, R, rstride=1, cstride=1, cmap=cm.coolwarm,
  #         linewidth=0, antialiased=False)
  # # ax.set_zlim(-1.01, 1.01)
  # plt.show()




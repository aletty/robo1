from models import *
import baseStation
import predict
import decide
import nxt
import time

def init_vars():
  # initialize boats and buoys
  my_boat = Boat('christine', 'T')
  enemy_boat = Boat('beth', 'P')
  buoy_list = [Buoy(name) for name in ['A', 'B', 'C', 'D']]
  socket = baseStation.setup_udp_socket(0xFFFFFFFF, 61557)
  xbee = nxt.setup_xbee()

  return (my_boat, enemy_boat, buoy_list, socket, xbee)  

def main(my_boat, enemy_boat, buoy_list, socket, xbee):
  # get data from base station
  baseStation.read_base_station(my_boat, enemy_boat,buoy_list, socket)
  print my_boat
  
  # get optimal rudder or thrust
  my_boat.action = decide.decide(my_boat,enemy_boat,buoy_list)
  
  # send commands to nxt
  nxt.send_nxt(xbee, *my_boat.action)


if __name__ == '__main__':
  my_boat, enemy_boat, buoy_list, socket, xbee = init_vars()

  try:
    while True:
      main(my_boat, enemy_boat, buoy_list, socket, xbee)
      time.sleep(0.2) #wait 500ms
  
  except KeyboardInterrupt:
    nxt.send_nxt(xbee, 7, 7)
    print 'Exiting program...'
    socket.close()
    xbee.close()

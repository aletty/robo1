from models import *
import baseStation
import predict
import decide
import nxt
import time

def init_vars():
  # initialize boats and buoys
  my_boat = Boat('beth', 'P')
  enemy_boat = Boat('deborah', 'L')
  buoy_list = [Buoy(name) for name in ['A', 'B', 'C', 'D']]
  socket = baseStation.setup_udp_socket(0xFFFFFFFF, 61557)
  xbee = nxt.setup_xbee()

  return (my_boat, enemy_boat, buoy_list, socket, xbee)  

def main(my_boat, enemy_boat, buoy_list, socket, xbee):
  # get data from base station
  baseStation.read_base_station(my_boat, enemy_boat,buoy_list, socket)
  
  # get optimal rudder or thrust
  rudder, thrust = decide.decide(my_boat,enemy_boat,buoy_list)
  
  # send commands to nxt
  nxt.send_nxt(xbee, thrust, rudder)


if __name__ == '__main__':
  my_boat, enemy_boat, buoy_list, socket, xbee = init_vars()

  try:
    while True:
      main(my_boat, enemy_boat, buoy_list, socket, xbee)
      time.sleep(0.5) #wait 500ms
  
  except KeyboardInterrupt:
    print 'Exiting program...'
    socket.close()
    xbee.close()

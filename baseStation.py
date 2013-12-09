import socket
from models import * 
import math

def setup_udp_socket(base_ip, base_port):
  UDP_IP = base_ip
  UDP_PORT = base_port

  sock = socket.socket(socke.AF_INET, socket.SOCK_DGRAM)
  sock.bind((UDP_IP, UDP_PORT))
  return sock

def read_base_station(boat_1, boat_2, buoy_list, socket):
  data, addr = socket.recvfrom(1024)
  data_list = data.split(',')
  
  # boat 1
  boat_1_index = data_list.index(boat_1.greek)
  pos_1 = (int(data_list[boat_1_index+1]), int(data_list[boat_1_index+2]))
  heading_1 = math.radians(int(data_list[boat_1_index+3])-90)
  boat_1.update(pos_1, heading_1)

  # boat 2
  boat_2_index = data_list.index(boat_2.greek)
  pos_2 = (int(data_list[boat_2_index+1]), int(data_list[boat_2_index+2]))
  heading_2 = math.radians(int(data_list[boat_2_index+3])-90)
  boat_2.update(pos_2, heading_2)

  # buoy
  for buoy in buoy_list:
    buoy_index = data_list.index(buoy.name)
    buoy.position = (int(data_list[buoy_index+1]), int(data_list[buoy_index+2]))

if __name__ == '__main__':
  boat1 = Boat('deborah', 'G')
  boat2 = Boat('beth', 'L')

  buoy_list = [Buoy(name) for name in ['A', 'B', 'C', 'D']]

  read_base_station(boat1, boat2, buoy_list, None)
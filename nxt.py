import serial

def setup_xbee(port = '/dev/ttyUSB0'):
  ser = serial.Serial(port)
  return ser

def send_nxt(ser, thrust, rudder, left_wall_follow = False, right_wall_follow = False, gtfo_wall = False):
  # set behavior weights
  forebrain_weight = 1
  right_wall_follow_weight = 0
  left_wall_follow_weight = 0
  gtfo_wall_weight = 0
  
  if left_wall_follow:
    left_wall_follow_weight = 1
    right_wall_follow_weight = 0
    gtfo_wall_weight = 0
    forebrain_weight = 0

  elif right_wall_follow:
    left_wall_follow_weight = 0
    right_wall_follow_weight = 1
    gtfo_wall_weight = 0
    forebrain_weight = 0

  elif gtfo_wall:
    left_wall_follow_weight = 0
    right_wall_follow_weight = 0
    gtfo_wall_weight = 1
    forebrain_weight = 0

  # convert numbers to string
  thrust_command = chr(thrust + 65)
  rudder_command = chr(rudder + 65)
  left_wall_follow_command = chr(left_wall_follow_weight + 65)
  right_wall_follow_command = chr(right_wall_follow_weight + 65)
  gtf_wall_command = chr(gtfo_wall_weight + 65)
  forebrain_command = chr(forebrain_weight + 65)

  # create command string
  command_string = '[H%s%s%s%s%sAA%s]' % (rudder_command, thrust_command, forebrain_command, left_wall_follow_command, right_wall_follow_command, gtf_wall_command)
  
  # write to xbee
  ser.write(command_string)
  ser.flush()

  return command_string

if __name__ == '__main__':
  ser = setup_xbee()
  print send_nxt(ser, 3, 7)
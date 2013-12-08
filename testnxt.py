import serial
import time
import io

ser = serial.Serial('/dev/ttyUSB0')
# sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), newline = '\n', line_buffering = True)

ser.write("AAHCAAAAA")
ser.write("OOHCAAAAA")
# ser.flush()

try:
  sio.close()
except:
  print "no close"
  pass

# while True:
#   try:
#     x = ser_io.readline()
#     print x
#     time.sleep(0.1)
#   except KeyboardInterrupt:
#     print "Shutting port down"
#     ser.close()
      # break
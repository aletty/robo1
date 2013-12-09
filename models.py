from datetime import datetime
import time
import math

class Boat(object):
  def __init__(self, name, greek):
    self.name = name
    self.greek = greek
    self.position = (0,0)
    self.heading = 0
    self.speed = 0
    self.last_updated = datetime.now()

  def update(self, pos, heading):
    #calculate dt
    now = datetime.now()
    dt = (now - self.last_updated).total_seconds()
    
    # update variables
    self.last_updated = now
    self.speed = .3*self.speed + .7*math.sqrt((self.position[0] - pos[0])**2 + (self.position[1] - pos[1])**2)/dt
    self.position = pos
    self.heading = heading

  def __str__(self):
    return '{"name": "%s", "position": "%s", "heading": "%s", "speed": "%s"}' % (self.name, self.position, self.heading, self.speed)

  def __repr__(self):
    return self.__str__()

class Buoy(object):
  def __init__(self, name):
    self.name = name
    self.position = (0,0)

  def __str__(self):
    return '{"name": "%s", "position": "%s"}' % (self.name, self.position)

  def __repr__(self):
    return self.__str__()

if __name__ == "__main__":
  b = Boat('beth','L')
  for i in xrange(2):
    time.sleep(1)
    b.update((0,i+1),0)
  print b
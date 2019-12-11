from operator import itemgetter, attrgetter
import math
FILE = 'input.txt'

class Station(list):
    # initialize with current origin and desired resulting format
    def __init__(self, x, y):
        self.value = y + x * 100
        self.x = x
        self.y = y
    # define subtraction - differences from origin   
    def __sub__(self, pt):
        return (pt.x - self.x, pt.y - self.y)
    # laser method    
    def laser(self, lastShot = 200):
        shot = {k: v for k,_,v in self}
        return shot[sorted(shot)[lastShot-1]]
    def refresh(self):
        for pt in Station.Map:
            if pt is not self:  # check if point not current origin
                offset = self - pt
                theta = math.atan2(*offset)
                yield (math.pi - theta, math.hypot(*offset), pt.value) # hypot calculates length
    def analyze(asteroids):
        Station.Map = (*asteroids,)
        for pt in Station.Map:
            pt += sorted(pt.refresh(), reverse = True)
            pt.targets = len({*map(itemgetter(0), pt)})
        return max(Station.Map, key = attrgetter('targets'))


station = Station.analyze(Station(x, y) for y, line
    in enumerate(open(FILE))
for x, char in enumerate(line) if char == '#')


print("Part I:", station.targets)
print("Part II:", station.laser())

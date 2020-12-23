class Heading:
    direction : str
    distance : int

    def __init__(self, data):
        self.direction = data[0]
        self.distance = int(data[1:])

class Ship:
    #units away from starting point
    north : int
    east : int
    heading : int

    def __init__(self):
        #ship starts heading east
        self.north = 0
        self.east = 0
        #ship starts facing east
        self.heading = 90

    def adjust_heading(self,degrees):
        self.heading += degrees
        if self.heading >= 360:
            self.heading -= 360
        elif self.heading < 0:
            self.heading += 360

    def forward(self,units):
        direction = self.heading / 90
        if direction == 0:
            self.north += units
        elif direction == 1:
            self.east += units
        elif direction == 2:
            self.north -= units
        elif direction == 3:
            self.east -= units

    def move_direction(self,heading:Heading):
        if heading.direction == 'N':
            self.north += heading.distance
        elif heading.direction == 'E':
            self.east += heading.distance
        elif heading.direction == 'S':
            self.north -= heading.distance
        elif heading.direction == 'W':
            self.east -= heading.distance
    
    def calc_manhattan(self):
        return abs(self.north) + abs(self.east)

def read_input():
    headings = []
    with open('input.txt','r') as f:
        for line in f:
            headings.append(Heading(line))
    return headings

def process_headings(headings, ship):
    for heading in headings:
        direction = heading.direction
        if direction == 'F':
            ship.forward(heading.distance)
        elif direction == 'L':
            ship.adjust_heading(0-heading.distance)
        elif direction == 'R':
            ship.adjust_heading(heading.distance)
        else:
            ship.move_direction(heading)

def process_waypoint_headings(headings, ship, waypoint):
    for heading in headings:
        direction = heading.direction
        if direction == 'F':
            #move ship to waypoint, waypoint keeps same distance from ship
            east = waypoint.east - ship.east
            north = waypoint.north - ship.north
            ship.east += east * heading.distance
            ship.north += north * heading.distance
            waypoint.east = ship.east + east
            waypoint.north = ship.north + north
        elif direction == 'L':
            if heading.distance == 90:
                east = waypoint.east - ship.east
                north = waypoint.north - ship.north
                waypoint.north = ship.north + east
                waypoint.east = ship.east - north
            elif heading.distance == 180:
                north = ship.north - waypoint.north
                east = ship.east - waypoint.east
                waypoint.north = ship.north + north
                waypoint.east = ship.east + east
            elif heading.distance == 270:
                east = waypoint.east - ship.east
                north = waypoint.north - ship.north
                waypoint.north = ship.north - east
                waypoint.east = ship.east + north
        elif direction == 'R':
            if heading.distance == 90:
                east = waypoint.east - ship.east
                north = waypoint.north - ship.north
                waypoint.north = ship.north - east
                waypoint.east = ship.east + north
            elif heading.distance == 180:
                north = ship.north - waypoint.north
                east = ship.east - waypoint.east
                waypoint.north = ship.north + north
                waypoint.east = ship.east + east
            elif heading.distance == 270:
                east = waypoint.east - ship.east
                north = waypoint.north - ship.north
                waypoint.north = ship.north + east
                waypoint.east = ship.east - north
        else:
            waypoint.move_direction(heading)

headings = read_input()
ship = Ship()
process_headings(headings, ship)
print('Part 1:',ship.calc_manhattan())
ship = Ship()
waypoint = Ship()
waypoint.east += 10
waypoint.north += 1
process_waypoint_headings(headings,ship,waypoint)
print('Part 2:', ship.calc_manhattan())
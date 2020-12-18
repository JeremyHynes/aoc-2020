from enum import Enum

from files import import_input


class Direction(Enum):
    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270


class Position:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.direction = Direction.EAST

    def next(self, command: str):
        letter = command[0]
        value = int(command[1:])

        def move(v, force_direction=None):
            if force_direction:
                if force_direction == 'N':
                    self.y += v
                elif force_direction == 'E':
                    self.x += v
                elif force_direction == 'S':
                    self.y -= v
                elif force_direction == 'W':
                    self.x -= v
            else:
                if self.direction == Direction.NORTH:
                    self.y += v
                elif self.direction == Direction.EAST:
                    self.x += v
                elif self.direction == Direction.SOUTH:
                    self.y -= v
                elif self.direction == Direction.WEST:
                    self.x -= v

        if letter == 'F':
            move(value)
        elif letter in ['N', 'E', 'S', 'W']:
            move(value, letter)
        elif letter == 'L':
            new_dir = self.direction.value - value
            if new_dir < 0:
                new_dir += 360
            self.direction = Direction(value=new_dir)
        elif letter == 'R':
            new_dir = self.direction.value + value
            if new_dir >= 360:
                new_dir -= 360
            self.direction = Direction(value=new_dir)

        print(command, self.x, self.y, self.direction)

    def next_2(self, command: str):
        letter = command[0]
        value = int(command[1:])

        def move(x, y):
            self.x += x
            self.y += y

        def move_waypoint(v, force_direction):
            if force_direction == 'N':
                self.waypoint_y += v
            elif force_direction == 'E':
                self.waypoint_x += v
            elif force_direction == 'S':
                self.waypoint_y -= v
            elif force_direction == 'W':
                self.waypoint_x -= v

        if letter == 'F':
            for _ in range(value):
                move(self.waypoint_x, self.waypoint_y)
        elif letter in ['N', 'E', 'S', 'W']:
            move_waypoint(value, letter)
        elif (letter == 'L' and value == 90) or (letter == 'R' and value == 270):
            new_y = self.waypoint_x
            new_x = -self.waypoint_y
            self.waypoint_x = new_x
            self.waypoint_y = new_y
        elif letter in ['R', 'L'] and value == 180:
            new_x = -self.waypoint_x
            new_y = -self.waypoint_y
            self.waypoint_x = new_x
            self.waypoint_y = new_y
        elif (letter == 'R' and value == 90) or (letter == 'L' and value == 270):
            new_y = -self.waypoint_x
            new_x = self.waypoint_y
            self.waypoint_x = new_x
            self.waypoint_y = new_y

        print(command, self.x, self.y, self.waypoint_x, self.waypoint_y)

    def get_current_position(self):
        return abs(self.x) + abs(self.y)


if __name__ == '__main__':
    i_file = import_input('files/12.txt')

    p = Position()
    for i in i_file:
        p.next_2(i)
    print(p.get_current_position())

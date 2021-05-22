

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            self.x = self.x + other.x
            self.y = self.y + other.y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if isinstance(other, Point):
            return self.x != other.x or self.y != other.y

"""
vec.py
"""


class Vec:
    """A simple 2d vector class to use"""
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """Adds two vectors"""
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        """Subtracts two vectors"""
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Multiplication : Inner Product & Scalar Multiplcation Both implemented"""
        if isinstance(other, Vec):
            return self.x*other.x + self.y*other.y
        return Vec(self.x * other, self.y * other)

    def __rmul__(self, other):
        """Multiplication But for multiplication from the right"""
        if isinstance(other, Vec):
            return self.x*other.x + self.y*other.y
        return Vec(self.x * other, self.y * other)

########################################

if __name__ == "__main__":
    v1 = vec(2, 3)
    v2 = vec(-3, 2)

    print(v1 * 2)
    print(3 * v2)
    print(v1 * v2)
import math
from fractions import Fraction

class vectorPx:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def magnitude(self):

        return round(math.sqrt(self.x**2 + self.y**2))

    def normalize(self):

        gcd_value = math.gcd(self.x, self.y)

        if gcd_value != 0:

            self.x = self.x // gcd_value
            self.y = self.y // gcd_value

        return self
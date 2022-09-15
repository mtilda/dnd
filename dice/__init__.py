import random
from typing import Optional, Union

from mixins.logging import LoggingMixin


class D(LoggingMixin):
    def __init__(self, n: Union[int, str], count: Optional[int] = None):
        if isinstance(n, int):  # Dice(3) or Dice(3, 4)
            self.sides = n
            self.count = count or 1
        if isinstance(n, str):  # Dice("3d4")
            if count is not None:
                raise TypeError(
                    "Unexpected use of argument 'count' while using shorthand notation for argument 'n'"
                )
            (c, s) = n.split("d")
            self.count = int(c or 1)
            self.sides = int(s)

    def __repr__(self):
        return "%sd%s" % (self.count or "", self.sides)

    def __call__(self):
        sum = 0
        roll_list = []
        for _ in range(self.count):
            current_roll = random.randint(0, self.sides)
            roll_list.append(str(current_roll))
            sum += current_roll
        self.log.debug("Rolling %s" % repr(self))
        self.log.debug("%s = %s" % (sum, " + ".join(roll_list)))
        self.log.info("Rolled %s and got %s" % (repr(self), sum))
        return sum

    def __add__(self, other: "D"):
        if not isinstance(other, D):
            raise TypeError(
                "Unexpected type '%s' canot be added to type 'D'" % type(other).__name__
            )
        if not self.sides == other.sides:
            raise ValueError(
                "Unable to add dice (%s and %s) with different numbers of sides (%s and %s)"
                % (self, other, self.sides, other.sides)
            )
        new = D("%sd%s" % (self.count + other.count, self.sides))
        self.log.debug("%s = %s + %s" % (new, self, other))
        return new


d4 = D("d4")
d6 = D("d6")
d8 = D("d8")
d10 = D("d10")
d12 = D("d12")
d20 = D("d20")
d100 = D("d100")

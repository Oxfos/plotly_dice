from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Generates a random value between 1 and num_sides."""
        return randint(1, self.num_sides)

    def roll_x_times(self, times=1000):
        """Return results of rolling the die x times."""
        results = []
        for time in range(times):
            results.append(self.roll())
        return results
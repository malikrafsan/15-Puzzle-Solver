from numpy import random
import numpy as np
from constant import SIZE


class PuzzleGenerator:
    """A class for generating new puzzle board
    """

    def generate(self):
        """Generate new puzzle board randomly

        Returns:
            1D list of int: random puzzle board
        """

        arr = np.array(range(1, SIZE*SIZE+1))
        random.shuffle(arr)
        return list(arr)

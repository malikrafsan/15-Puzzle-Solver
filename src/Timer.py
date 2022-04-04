from time import time


class Timer:
    """A class for measuring time lapse
    
    Attributes:
    ----------------
    _timer: int
        time of current Timer instantiated
    """

    def __init__(self):
        """Constructor for Timer class
        """
        self._timer = int(time() * 1000)

    def stop(self):
        """Return time lapse of current Timer instantiated

        Returns:
            int: time lapse of current Timer instantiated
        """
        
        return int(time() * 1000) - self._timer

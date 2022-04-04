class VisitedPuzzle:
    """A class for storing puzzles that have been visited 
    
    Attributes:
    ----------------
    _map: set of tuple of int
        set data structure to store the puzzle that has been visited
    """
  
    def __init__(self):
        """Constructor for VisitedPuzzle class
        """
        
        self._map = set()

    def contain(self, item):
        """Check whether given Node's puzzle board is in visited set

        Args:
            item (Node): Node that being checked

        Returns:
            boolean: flag whether puzzle of Node is in visited set
        """
      
        return tuple(item.puzzle().board()) in self._map

    def insert(self, item):
        """Insert puzzle board of Node into visited set

        Args:
            item (Node): Node that being inserted into visited set
        """
      
        self._map.add(tuple(item.puzzle().board()))

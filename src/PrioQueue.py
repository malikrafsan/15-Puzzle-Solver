import heapq


class PrioQueue:
    """A class for store Nodes that will be checked as priority queue
    
    Attributes:
    ----------------
    _queue: heap of Node
        Heap data structure for storing Nodes to fasten 
        insert and delete first operation
    """
    
    def __init__(self):
        """Constructor for PrioQueue class
        """
        
        self._queue = []
        heapq.heapify(self._queue)
        self._size = 0

    def empty(self):
        """Check if current PrioQueue is empty

        Returns:
            boolean: flag whether current PrioQueue is empty
        """
        
        return self._size == 0

    def push(self, item):
        """Insert new item into heap

        Args:
            item (Node): new item that will be inserted 
                into priority queue
        """
        heapq.heappush(self._queue, item)
        self._size += 1

    def pop(self):
        """Remove first item from priority queue and return it

        Returns:
            Node: first item in priority queue
        """
      
        self._size -= 1
        return heapq.heappop(self._queue)

    def size(self):
        """Getter for size attribute

        Returns:
            int: size of current PrioQueue
        """
        
        return self._size

    def describe(self):
        """Descibe all Nodes that being stored in 
        current PrioQueue (unordered)
        """
      
        for node in self._queue:
            node.describe()
            print("================")

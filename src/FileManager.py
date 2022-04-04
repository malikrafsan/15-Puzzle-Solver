from constant import SIZE, LENGTH


class FileManager:
    """A class for reading input puzzle from file

    Attributes:
    ----------------
    _matrix: list of list of int
        A 2D matrix to store the puzzle that being read from file
    """

    def __init__(self, path):
        """Constructor for FileManager class

        Args:
            path (string): path of file that will be read from
        """
        
        self._matrix = [[-1 for _ in range(SIZE)] for _ in range(SIZE)]

        f = open(path, 'r')
        for i, line in enumerate(f):
            arr = line.split()
            for j in range(SIZE):
                self._matrix[i][j] = int(arr[j])

    def _flatten(self, matrix):
        """Convert 2D matrix to 1D list

        Args:
            matrix (list of list of int): matrix that will be converted to 1D list

        Returns:
            list of int: flattened matrix
        """
        
        arr = [-1 for _ in range(LENGTH)]

        for i in range(SIZE):
            for j in range(SIZE):
                arr[i*SIZE + j] = matrix[i][j]

        return arr

    def arr(self):
        """Getter for puzzle that being read by FileManager as 1D list

        Returns:
            list of int: puzzle file reading result
        """

        return self._flatten(self._matrix)

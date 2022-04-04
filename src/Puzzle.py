from constant import HOLE, SIZE, LENGTH


class Puzzle:
    """A class to store puzzle state

    Attributes:
    ----------------
    _board: list of int
        1D list of puzzle state
    _weight: int
        number of misplaced tiles
    _idx_empty: int
        index of empty tile
    """

    def __init__(self, arr, weight=-1, idx_empty=-1):
        """Constructor for Puzzle class

        Args:
            arr (list of int): 1D list of puzzle state
            weight (int, optional): number of misplaced tiles.
                Defaults to -1.
            idx_empty (int, optional): index of empty tile. 
                Defaults to -1.
        """

        self._board = arr
        self._weight = weight
        self._idx_empty = idx_empty

    def find_empty(self):
        """Find the index of empty tile and store it in class attribute
        """

        for i in range(len(self._board)):
            if self._board[i] == HOLE:
                self._idx_empty = i

    def _get_row_col(self, idx):
        """Get row and column of a tile based on given index 

        Args:
            idx (int): given index to calculate row and column

        Returns:
            (int, int): tuple of row and column
        """

        return (idx // SIZE, idx % SIZE)

    def solvable_status(self):
        """Calculate `kurang` per tiles and return status solvability of the puzzle

        Returns:
            (boolean, list of int, int, int, int): status of solvability of the puzzle
        """

        (row, col) = self._get_row_col(self._idx_empty)
        x = (row+col) % 2
        
        arr = [-1 for _ in range(LENGTH)]

        sum = 0
        for i in range(len(self._board)):
            arr[self._board[i] - 1] = self._kurang(i)
            sum += arr[self._board[i] - 1]
        
        return ((sum + x) % 2 == 0, arr, sum, x, self._weight)

    def _kurang(self, i):
        """Helper method to calculate inversion of given index

        Args:
            i (int): given index to calculate inversion

        Returns:
            int: inversion of given index
        """

        count = 0
        for idx in range(i, len(self._board)):
            if (self._board[idx] < self._board[i]):
                count += 1

        return count

    def move(self, d_row, d_col):
        """Generate new puzzle by moving empty tile if possible

        Args:
            d_row (int): change of row
            d_col (int): change of col

        Returns:
            (Puzzle | None, boolean): tuple of new Puzzle 
                and boolean flag whether move is success
        """

        (row, col) = self._get_row_col(self._idx_empty)

        if (row+d_row < 0 or row+d_row >= SIZE or col+d_col < 0 or col+d_col >= SIZE):
            return None, False

        idx1 = row*SIZE + col
        idx2 = (row+d_row)*SIZE + (col+d_col)

        new_weight = self._weight
        if (self._board[idx2] == idx1 + 1):
            new_weight -= 1
        elif (self._board[idx2] == idx2 + 1):
            new_weight += 1

        new_puzzle = Puzzle(self._copy_board(), new_weight, idx2)
        new_puzzle._board[idx1], new_puzzle._board[idx2] = new_puzzle._board[idx2], new_puzzle._board[idx1]

        return new_puzzle, True

    def describe(self):
        """Describe current puzzle state
        """

        for i in range(SIZE):
            for j in range(SIZE):
                cur = self._board[i*SIZE + j]
                print("#" if cur == HOLE else cur, end=" ")
            print()

    def _copy_board(self):
        """Copy current board and return it

        Returns:
            1D list of int: copy of current board
        """
        return [x for x in self._board]

    def count_misplaced_tiles(self):
        """Count misplaced tiles in current puzzle. 
        To be called on first Puzzle that being instantiated
        """

        count = 0
        for i in range(LENGTH):
            if (self._board[i] != HOLE and self._board[i] != i+1):
                count += 1

        self._weight = count

    def weight(self):
        """Getter for weight attribute

        Returns:
            int: weight of current puzzle
        """

        return self._weight

    def board(self):
        """Getter for board attribute

        Returns:
            1D list of int: board of current puzzle
        """

        return self._board

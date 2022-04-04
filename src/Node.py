class Node:
    """A wrapper class for store information about 
    state of puzzle, depth, parent, and move that is used

    Attributes
    ----------
    _moves_units (static) : list of tuple
        list of operator move that will be used to generated new Puzzle
    _moves_names (static) : list of string
        label for _moves_units
    _puzzle : Puzzle
        Puzzle object that store state of puzzle
    _parent : Node
        Node object that store parent of current Node
    _depth : int
        depth of current Node
    _move : string
        label for operator move that is used to generate current Node
    """

    _moves_units = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    _moves_names = ["Right", "Down", "Left", "Up"]

    def __init__(self, puzzle, parent=None, depth=0, move=None):
        """Constructor for Node class

        Args:
            puzzle (Puzzle): Puzzle object that store state of puzzle
            parent (Node, optional): Node object that store parent of 
                current Node. Defaults to None.
            depth (int, optional): depth of current Node. Defaults to 0.
            move (string, optional): label for operator move that is 
                used to generate current Node. Defaults to None.
        """

        self._puzzle = puzzle
        self._parent = parent
        self._depth = depth
        self._move = move

    def path_solving(self):
        """Generate path from current Node to root Node

        Returns:
            list of Node: path from current Node to root Node
        """
        
        temp = self
        arr = []

        while (True):
            if (temp._move == None):
                return arr

            arr.append(temp)
            temp = temp._parent

    def depth(self):
        """Getter for depth attribute

        Returns:
            int: depth of current Node
        """
        return self._depth

    def puzzle(self):
        """Getter for puzzle attribute

        Returns:
            Puzzle: state puzzle of current Node
        """
        return self._puzzle

    def is_solution(self):
        """Check if current Node is solution

        Returns:
            boolean: flag whether current Node is solution
        """

        return self._puzzle.weight() == 0

    def weight(self):
        """Getter for weight attribute

        Returns:
            int: weight of current Node
        """
        return self._depth + self._puzzle.weight()

    def generate_children(self):
        """Generate children Node of current Node. 
        This method generate if move is possible 
        and not opposite move to parent

        Returns:
            list of Node: children of current Node
        """

        arr = []

        for i in range(len(Node._moves_units)):
            opp_move = Node._moves_names[(i+2) % 4]
            if (opp_move != self._move):
                (d_row, d_col) = Node._moves_units[i]
                new_puzzle, success = self._puzzle.move(d_row, d_col)
                if (success):
                    arr.append(
                        Node(new_puzzle, self, self._depth+1, Node._moves_names[i]))

        return arr

    def describe(self):
        """Describe the current Node as weight, depth, move, 
        and puzzle state
        """
      
        print("weight:", self.weight())
        print("depth:", self._depth)
        print("move:", self._move)
        print("puzzle:")
        self._puzzle.describe()

    def __lt__(self, next):
        """Operator overloading for less than operator based on 
        weight of Node. If weight is same, compare depth

        Args:
            next (Node): Right hand side of less than operation

        Returns:
            boolean: flag whether current Node is less than next Node
        """
        
        if self.weight() == next.weight():
            return self.depth() >= next.depth()

        return self.weight() < next.weight()

    def move(self):
        return self._move
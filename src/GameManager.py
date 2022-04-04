from FileManager import FileManager
from Puzzle import Puzzle
from PrioQueue import PrioQueue
from Node import Node
from Timer import Timer
from PuzzleGenerator import PuzzleGenerator
from VisitedPuzzle import VisitedPuzzle


class GameManager():
    """A class that control behaviour of program execution

    Attributes
    ----------
    _pz : Puzzle
        Puzzle input, either from file or PuzzleGenerator
    """

    def __init__(self, is_from_file, path=None):
        """Constructor for GameManager class

        Args:
            is_from_file (bool): flag whether puzzle input is from file
            path (string | None, optional): Path of puzzle input file. Defaults to None.
        """

        if (is_from_file):
            self._pz = Puzzle(FileManager(path).arr())
        else:
            self._pz = Puzzle(PuzzleGenerator().generate())

        self._pz.count_misplaced_tiles()
        self._pz.find_empty()

    def puzzle(self):
        """Getter for Puzzle attribute

        Returns:
            Puzzle: puzzle input that will be solved
        """

        return self._pz

    def solvable_status(self):
        """Method that return status of solvability of the puzzle

        Returns:
            (boolean, list of int, int, int, int): status of solvability of the puzzle
        """

        return self._pz.solvable_status()

    def solve(self):
        """Main control program to solve the puzzle

        Returns:
            (list of Node, int, int): Snapshot of Node path to solve the puzzle, 
                how many Nodes are generated, time lapse taken to solve the puzzle
        """

        t = Timer()
        sol_node = None
        pq = PrioQueue()
        vp = VisitedPuzzle()

        n = Node(self._pz)
        pq.push(n)
        vp.insert(n)
        count = 1

        while (not pq.empty()):
            cur_node = pq.pop()

            if (cur_node.is_solution()):
                sol_node = cur_node
                break

            children = cur_node.generate_children()
            for child in children:
                if (not vp.contain(child)):
                    vp.insert(child)
                    pq.push(child)
                    count += 1

        time_lapse = t.stop()

        arr = sol_node.path_solving()

        return (arr, count, time_lapse)

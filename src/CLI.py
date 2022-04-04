from GameManager import GameManager
from constant import LENGTH

class CLI:
    """A class for running CLI App

    Attributes
    ----------
    _gm : GameManager
        object that controlls the game 
    """

    def __init__(self):
        """Constructor for CLI class that also run the program at once
        """

        print("PUZZLE SOLVER")
        print("Please select input mode for puzzle")
        print("1. From file")
        print("2. Random generator")

        inp = int(input("Input: "))
        while (True):
            if (inp >= 1 and inp <= 2):
                break
            else:
                print("Wrong format, please enter 1 or 2")

        is_from_file = inp == 1
        if (is_from_file):
            print("Please enter file name:")
            file_name = input("File name: ")
            self._gm = GameManager(is_from_file, file_name)
        else:
            self._gm = GameManager(is_from_file)

        (solvable, arr_kurang, sum, x, misplaced) = self._gm.solvable_status()

        self._gm.puzzle().describe()
        print("Misplaced tiles:", misplaced)
        for i in range(LENGTH):
            print(f"Kurang ke-{i+1}: {arr_kurang[i]}")

        print(f"Sum kurang + x: {sum} + {x} = {sum + x}")

        if (not solvable):
            print("Puzzle is unsolvable")
            return

        print("Puzzle is solvable")

        (arr, count, time_lapse) = self._gm.solve()

        n = len(arr)
        for i in range(n):
            arr[n-i-1].describe()
            print("<><><><><><><><><>")

        print("GENERATED:", count)
        print("TIME LAPSE:", time_lapse, "ms")

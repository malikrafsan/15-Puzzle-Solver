from GameManager import GameManager
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import enum
from constant import *

class GUI(tk.Tk):
    """A class for running GUI App. Interited from tkinter.Tk

    Attributes
    ----------
    truncated
    """
    
    class _Status_Enum(enum.Enum):
        """Enum class for Program execution status
        Inherited from enum.Enum
        """
        
        SOLVED = "Solved"
        UNSOLVABLE = "Unsolvable"
        LOADING = "Loading"
        WAITING_INPUT = "Waiting Input"
        FINISHED = "Finished"

    def __init__(self):
        """Constructor for GUI class
        """
        
        super().__init__()
        self.title('Puzzle Solver')

        self._arr_btn = [Button(self, text=i+1, padx=40, pady=40,
                                state=DISABLED, width=10, bg="#ffffff")
                         for i in range(LENGTH)]

        self._from_file_btn = Button(
            self, text="Load from File", padx=40, pady=10, width=10, command=self._load_file)
        self._random_generated_btn = Button(
            self, text="Random Generated", padx=40, pady=10, width=10, command=self._random_generated)

        self._from_file_btn.grid(row=0, column=0)
        self._random_generated_btn.grid(row=0, column=3)

        self._label_status = Label(
            self, text=f"Status: {self._Status_Enum.WAITING_INPUT.value}")
        self._label_status.grid(row=1, column=0, columnspan=4)

        self._label_generated = Label(self, text=f"Generated Node: ")
        self._label_generated.grid(row=2, column=0, columnspan=4)
        self._label_time = Label(self, text=f"Time Lapse: ms")
        self._label_time.grid(row=3, column=0, columnspan=4)
        self._label_total_move = Label(self, text=f"Total Move: ")
        self._label_total_move.grid(row=4, column=0, columnspan=4)

        for i in range(LENGTH):
            self._arr_btn[i].grid(row=(i//4 + 5), column=(i % 4))

            num = int(self._arr_btn[i]["text"])
            if (num == HOLE):
                self._arr_btn[i].grid_remove()

        self._label_steps = Label(self, text=f"Step Taken: ")
        self._label_steps.grid(row=9, column=0, columnspan=4)
        self._label_misplaced = Label(self, text=f"Total misplaced puzzle: ")
        self._label_misplaced.grid(row=10, column=0, columnspan=4)
        self._label_kurang = Label(self, text=f"Total kurang puzzle: ")

        self._arr_label_kurang = [
            Label(self, text=f"Kurang ke-{i+1}: ") for i in range(LENGTH)]
        
        for i in range(LENGTH):
            self._arr_label_kurang[i].grid(
                row=(11 + i // 2), column=(0 if i % 2 == 0 else 2), columnspan=2)

        self._label_sum_add_x = Label(self, text=f"Sum of kurang + x: ")
        self._label_sum_add_x.grid(row=20, column=0, columnspan=4)

        self._set_label(0, 0, 0)
        self._set_label_below(0, [0 for _ in range(LENGTH)], 0)

    def _set_label_below(self, misplaced, arr, sum_x):
        """Method to set label below the tiles

        Args:
            misplaced (int): how many misplaced tiles
            arr (list of int): list of `kurang` calculation per tiles
            sum_x (int): sum of kurang calculation + x (parity)
        """
        
        self._label_misplaced["text"] = f"Total misplaced puzzle: {misplaced}"

        for i in range(LENGTH):
            self._arr_label_kurang[i]["text"] = f"Kurang ke-{i+1}: {arr[i]}"

        self._label_sum_add_x["text"] = f"Sum of kurang + x: {sum_x}"

    def _load_file(self):
        """Method to get file puzzle and run program
        """
        
        self._label_status["text"] = f"Status: {self._Status_Enum.LOADING.value}"
        self._random_generated_btn["state"] = DISABLED
        self._from_file_btn["state"] = DISABLED

        self._is_from_file = True
        filetypes = (("Text Files", "*.txt"),)
        self._filename = fd.askopenfilename(
            title='Select puzzle file',
            initialdir='test/',
            filetypes=filetypes)

        self.solve()

    def _random_generated(self):
        """Method to generate random puzzle and run program
        """
        
        self._label_status["text"] = f"Status: {self._Status_Enum.LOADING.value}"
        self._is_from_file = False
        self._random_generated_btn["state"] = DISABLED
        self._from_file_btn["state"] = DISABLED
        self._filename = None
        showinfo(
            title='Warning Random Generated Puzzle',
            message="Random Generated Puzzle tends to be computational intensive if solveable. This program will most likely be unresponsive for a long time until puzzle is solved"
        )

        self.solve()

    def solve(self):
        """Main program control to solve the puzzle
        """
        
        self._gm = GameManager(self._is_from_file, self._filename)
        self.redisplay(self._gm.puzzle().board())

        (solvable, arr_kurang, sum, x, misplaced) = self._gm.solvable_status()
        self._set_label_below(misplaced, arr_kurang, sum + x)

        if (not solvable):
            self._label_status["text"] = f"Status: {self._Status_Enum.UNSOLVABLE.value}"
            showinfo(
                title='Unsolvable Puzzle',
                message="Your input puzzle is unsolvable"
            )
            self._label_steps["text"] = "Step Taken: "

            self._enable_btn()
            return

        (arr, count, time_lapse) = self._gm.solve()

        self._set_label(count, time_lapse, 0 if arr == None else len(arr))

        self._label_status["text"] = f"Status: {self._Status_Enum.SOLVED.value}"

        n = len(arr)
        steps = ""
        for i in range(n):
            steps += " " + str(arr[n-i-1].move())
            (lambda x=i: self.loop(n,
                                   x, arr[n-x-1].puzzle().board()))()
        
        self._label_steps["text"] = f"Step Taken: {steps}"

    def redisplay(self, arr):
        """Method to change tiles position based on current state of Puzzle

        Args:
            arr (list of int): board of current Puzzle
        """
        
        for i in range(LENGTH):
            self._arr_btn[i].grid()
            self._arr_btn[i]['text'] = arr[i]

            num = int(arr[i])
            if (num == HOLE):
                self._arr_btn[i].grid_remove()

    def loop(self, n, x, arr):
        """Method to display change tiles based on Node path to solve the puzzle

        Args:
            n (int): how many step to solve the puzzle
            x (int): index of current path
            arr (list of int): state of current puzzle board
        """
        
        self.after(SLEEP_TIME * x, lambda: self.redisplay(arr))

        if (x+1 == n):
            self.after(SLEEP_TIME * x, lambda: self._finish())

    def _enable_btn(self):
        """Method to enable button random generate and load file
        """
        
        self._random_generated_btn["state"] = "active"
        self._from_file_btn["state"] = "active"

    def _finish(self):
        """Method that to be called when program is finish displaying the changing tiles
        """
        
        self._enable_btn()
        self._label_status["text"] = f"Status: {self._Status_Enum.FINISHED.value}"

    def _set_label(self, node, time_lapse, move):
        """Method to set upper labels text

        Args:
            node (int): How many nodes are generated
            time_lapse (int): How long the program took to solve the puzzle
            move (int): total move to solve the puzzle
        """
        
        self._label_generated["text"] = f"Generated Node: {node}"
        self._label_time["text"] = f"Time Lapse: {time_lapse}ms"
        self._label_total_move["text"] = f"Total Move: {move}"

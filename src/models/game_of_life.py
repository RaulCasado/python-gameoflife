import numpy as np


class GameOfLife:
    def __init__(self, rows, cols, initial_grid=None):
        self.rows = rows
        self.cols = cols
        if initial_grid is None:
            self.set_random_start()
        else:
            self.grid = initial_grid

    def toggle_state(self, row, col):
        # Toggle the state of the cell at (row, col)
        # Ensure the indices are within bounds
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row, col] = 1 - self.grid[row, col]

    def get_cell(self, row, col):
        # Get the state of the cell at (row, col)
        # Ensure the indices are within bounds
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row, col]
        return None

    def count_neighbors(self, row, col):
        neighbors = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                # if we are visiting the own cell we skip
                if i == row and j == col:
                    continue
                # make sure we dont get a out of bonds error
                if 0 <= i < self.rows and 0 <= j < self.cols:
                    neighbors += self.grid[i, j]
        return neighbors

    def update_grid(self):
        # Update the grid kill cells or bring them to life based on the rules of the game

        """Any live cell with fewer than two live neighbors dies (underpopulation).
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies (overpopulation).
        Any dead cell with exactly three live neighbors becomes a live cell (reproduction).
        """

        np_copy = np.copy(self.grid)
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.count_neighbors(i, j)
                if self.grid[i, j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        np_copy[i, j] = 0
                else:
                    if neighbors == 3:
                        np_copy[i, j] = 1
        self.grid = np_copy

    def set_random_start(self):
        # we use np method instead of making my own for loop
        # just to make it more efficient
        # and to make it more readable and just for using numpy since we
        # are using it in the rest of the code
        self.grid = np.random.randint(2, size=(self.rows, self.cols))

    def set_pattern(self,pattern):
        self.grid = np.zeros((self.rows, self.cols), dtype=int)
        patterns = {
            'glider': [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
            'blinker': [(1, 0), (1, 1), (1, 2)],
            'block': [(0, 0), (0, 1), (1, 0), (1, 1)],
            'toad': [(1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2)],
            'beacon': [(0, 0), (0, 1), (1, 0), (2, 3), (3, 2), (3, 3)],
        }
        if pattern not in patterns:
            raise ValueError(f"Pattern '{pattern}' not recognized.")
        for cell in patterns.get(pattern, []):
            self.grid[cell] = 1
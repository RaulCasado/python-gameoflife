import numpy as np


# we have made this class static so we can use it without instantiating it
# since we dont have any state to maintain
# and we just want to use the methods to save and load files
class FileManager:
    @staticmethod
    def save(grid, filename):
        # fmt is used to specify the format of the saved data
        # if we dont put it it will save it as a float
        # so something like 1.00000000e+00 and we dont want that
        try:
            np.savetxt(filename, grid, fmt='%d')
        except IOError as e:
            raise ValueError(f"Error saving file {filename}: {e}")

    @staticmethod
    def load(filename):
        try:
            # we use np.loadtxt to load the file
            # and we specify the dtype as int to ensure we get integers
            loaded_grid = np.loadtxt(filename, dtype=int)
            if loaded_grid.size == 0:
                raise ValueError("Loaded grid is empty.")
            return loaded_grid
        except (IOError, ValueError) as e:
            raise ValueError(f"Error loading file {filename}: {e}")

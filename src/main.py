import argparse
from views.view_tkinter import GameView
from controllers.game_controller import GameController
from controllers.file_controller import FileController
from models.game_of_life import GameOfLife
from models.file_manager import FileManager
import tkinter as tk


def main():
    # We define the command line arguments for the game of life
    # All of them are optional, except for --random or --pattern
    # which must be specified to run the game.
    # --load for loading a game from a file
    # --size is the size of the grid, --speed is the speed of the game
    # --iterations is the number of iterations to run, --name is the name of the game
    # --pattern is the pattern to use in the game, and --random is a flag to use a random pattern.
    parser = argparse.ArgumentParser(description="The game of life")
    parser.add_argument("--load", type=str, help="Load a game from a file")
    parser.add_argument(
        "--cols", type=int, default=20, help="Number of columns in the grid"
    )
    parser.add_argument(
        "--rows", type=int, default=20, help="Number of rows in the grid"
    )
    parser.add_argument("--speed", type=int, default=1000, help="Speed of the game")
    parser.add_argument(
        "--iterations", type=int, default=200, help="Number of iterations to run"
    )
    parser.add_argument("--name", type=str, default="World", help="Name of the game")
    parser.add_argument("--pattern", type=str, help="Pattern to use in the game")
    parser.add_argument("--random", action="store_true", help="Use a random pattern")
    args = parser.parse_args()

    try:
        validate_args(args)
    except ValueError as e:
        print(f"Error: {e}")
        parser.print_help()
        return

    # Create the game model
    if args.load:
        # If loading from a file, we create the model with the file manager
        try:
            initial_grid = FileManager.load(args.load)
        except ValueError as e:
            print(e)
            return
        model = GameOfLife(initial_grid.shape[0], initial_grid.shape[1], initial_grid)
    elif args.random:
        # If not loading from a file, we create the model with the specified parameters
        model = GameOfLife(args.rows, args.cols)
    else:
        model = GameOfLife(args.rows, args.cols)
        try:
            model.set_pattern(args.pattern)
        except ValueError as e:
            print(f"Error setting pattern: {e}")
            return
    
    root = tk.Tk()
    root.title(args.name)
    view = GameView(root, model.rows, model.cols)
    # Create controllers
    controller = GameController(model, view, args.speed, args.iterations)
    file_controller = FileController(model, view)
    view.pack()
    # If loading from file, load grid; otherwise start simulation
    controller.start_simulation()
    root.mainloop()


def validate_args(args):
    # We validate the command line arguments to ensure they are correct
    # And raise ValueError if they are not with the appropriate message
    if args.speed <= 0:
        raise ValueError("Speed needs to be a positive number")
    if args.iterations < 0:
        raise ValueError("Iterations needs to be a non-negative integer")
    if args.rows <= 0 or args.cols <= 0:
        raise ValueError("Rows and columns must be positive integers")
    if args.speed < 100:
        raise ValueError("Speed must be at least 100 milliseconds")
    if args.speed > 2000:
        raise ValueError("Speed must not exceed 2000 milliseconds")
    count = 0
    if args.pattern:
        count += 1
    if args.random:
        count += 1
    if args.load:
        count += 1
    if count == 0:
        raise ValueError("You must specify either --pattern, --random, or --load")
    if count > 1:
        raise ValueError("You can only specify one of --pattern, --random, or --load at a time")


if __name__ == "__main__":
    main()

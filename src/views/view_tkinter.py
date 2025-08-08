import tkinter as tk
from tkinter import messagebox
class GameView(tk.Frame):
    def __init__(self, root, count_rows, count_cols, cell_size=30):
        super().__init__(root)
        self.count_rows = count_rows
        self.count_cols = count_cols
        self.cell_size = cell_size
        self.rects = []
        self.canvas = tk.Canvas(
            self, width=cell_size * count_cols, height=cell_size * count_rows
        )
        self.pause_button = tk.Button(self, text="Pause", command=self.pause)
        self.pause_button.pack()
        self.export_button = tk.Button(self, text="Export")
        self.export_button.pack()
        self.reduce_speed = tk.Button(
            self, text="Reduce Speed"
        )
        self.reduce_speed.pack()
        self.increase_speed = tk.Button(
            self, text="Increase Speed"
        )
        self.increase_speed.pack()
        self.label_speed = tk.Label(self)
        self.label_speed.pack()
        self.is_paused = False
        self.canvas.pack()
        self.render_grid()

    def render_grid(self):
        for i in range(self.count_rows):
            row_rects = []
            for j in range(self.count_cols):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                rect = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="white", outline="black"
                )
                row_rects.append(rect)
            self.rects.append(row_rects)

    def update_board(self, grid):
        for i in range(self.count_rows):
            for j in range(self.count_cols):
                if grid[i, j] == 1:
                    color = "black"
                else:
                    color = "white"
                self.canvas.itemconfig(self.rects[i][j], fill=color)

    def pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")

    def show_speed(self, speed):
        self.label_speed.config(text=f"Speed: {speed}")

    def show_message(self, message):
        messagebox.showinfo("Game of Life", message)
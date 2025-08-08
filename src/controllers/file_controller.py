from tkinter import filedialog
from models.file_manager import FileManager


class FileController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # connect view button to export functionality
        self.view.export_button.config(command=self.export_game)

    def export_game(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if filename:
            try:
                FileManager.save(self.model.grid, filename)
            except ValueError as e:
                self.view.show_message(f"Error saving file: {e}")

class GameController:
    def __init__(self, model, view, speed, iterations):
        self.model = model
        self.view = view
        self.speed = speed
        self.iterations = iterations
        self.current_iteration = 0
        self.is_running = False
        # Connect view buttons to controller methods
        self.view.pause_button.config(command=self.toggle_pause)
        self.view.reduce_speed.config(command=self.reduce_speed)
        self.view.increase_speed.config(command=self.increase_speed)
        self.after_id = None
        self.view.show_speed(self.speed)

    def start_simulation(self):
        self.is_running = True
        self.current_iteration = 0
        self.run_iteration()

    def run_iteration(self):
        if self.is_running and self.current_iteration < self.iterations:
            self.model.update_grid()
            self.view.update_board(self.model.grid)
            self.current_iteration += 1
            self.after_id = self.view.after(self.speed, self.run_iteration)
        elif self.current_iteration >= self.iterations:
            self.is_running = False
            self.view.show_message("Simulation completed")

    def toggle_pause(self):
        self.view.pause()
        self.is_running = not self.is_running
        if self.is_running:
            self.run_iteration()

    def reduce_speed(self):
        self.speed = min(self.speed + 100, 2000)
        self.view.show_speed(self.speed)
        if self.is_running and self.after_id:
            self.view.after_cancel(self.after_id)
            self.after_id = self.view.after(self.speed, self.run_iteration)

    def increase_speed(self):
        self.speed = max(self.speed - 100, 100)
        self.view.show_speed(self.speed)
        if self.is_running and self.after_id:
            self.view.after_cancel(self.after_id)
            self.after_id = self.view.after(self.speed, self.run_iteration)


class TrainingProgram:
    def __init__(self, name, duration, level):
        self.name = name
        self.duration = duration  # in weeks
        self.level = level  # e.g., Beginner, Intermediate, Advanced

    def name (self) -> str:
        return self.name
    def duration (self) -> int:
        return self.duration
    def level (self) -> str:
        return self.level
    def __repr__(self) -> str:
        return f"TrainingProgram(name={self.name}, duration={self.duration} weeks, level={self.level})"

    def organizePractice(self):
        print(f"Organizing a {self.duration}-week {self.level} training program: {self.name}.")
    def add_program(self, program):
        print(f"Adding program '{program}' to the training program '{self.name}'.")

class TrainingProgram:
    def __init__(self, name, duration, level):
        self._name = name
        self._duration = duration  # in weeks
        self._level = level  # e.g., Beginner, Intermediate, Advanced

    @property
    def name (self):
        return self._name

    @property
    def duration (self):
        return self._duration

    @property
    def level (self):
        return self._level

    def __str__(self):
        return f"TrainingProgram: {self.name} | Duration: {self.duration} | Level: {self.level}"

    def __repr__(self):
        return f"TrainingProgram(name={self.name}, duration={self.duration} weeks, level={self.level})"

    def organize_practice(self):
        print(f"Organizing a {self.duration}-week {self.level} training program: {self.name}.")
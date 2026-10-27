from .team_member import TeamMember

class Coach(TeamMember):
    def __init__(self, name, age, country, style):
        super().__init__(name, age, country)
        self._style = style

    @property
    def style(self):
        return self._style

    def __str__(self):
        return f"{super().__str__()} | Стиль: {self.style}"

    def __repr__(self):
        return f"Coach('{self.name}', {self.age}, '{self.country}', [{self.style}])"
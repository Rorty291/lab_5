from .team_member import TeamMember

class Staff(TeamMember):
    def __init__(self, name, age, country, profession):
        super().__init__(name, age, country)
        self._profession = profession

    @property
    def profession(self):
        return self._profession

    def __str__(self):
        return f"{super().__str__()} | Професія: {self.profession}"

    def __repr__(self):
        return f"Staff('{self.name}', {self.age}, '{self.country}', [{self.profession}])"
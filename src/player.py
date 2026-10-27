from .team_member import TeamMember

class Player(TeamMember):
    def __init__(self, name, age, country, abilities):
        super().__init__(name, age, country)
        self._abilities = abilities

    @property
    def abilities(self):
        return self._abilities

    def __str__(self):
        return f"{super().__str__()} | Навички: {self.abilities}"

    def __repr__(self):
        return f"Player('{self.name}', {self.age}, '{self.country}', [{self.abilities}])"
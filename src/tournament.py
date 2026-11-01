from src.team import Team

class Tournament:
    def __init__(self, name: str, date: str, prize: int):
            self._name = name
            self._date = date
            self._prize = prize
            self._teams = []

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    @property
    def prize(self):
        return self._prize

    @property
    def teams(self):
        # Повертаємо копію списку для захисту від прямої зміни ззовні
        return self._teams.copy()

    def participate_tournament(self, team: Team):
        self._teams.append(team)

    def leave_tournament(self, team: Team):
        self._teams.remove(team)

    def __str__(self):
        return f"Tournament: {self.name}, Date: {self.date}, Prize pool: ${self.prize}"

    def __repr__(self):
        return f"Tournament(name={self.name}, date={self.date}, prize_pool={self.prize}, teams={self.teams})"



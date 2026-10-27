from src.coach import TeamMember
from typing import List


class Tournament:
    def __init__(self, name: str, date: str, prize: str): 
            self.name = name
            self.date = date
            self.prize = prize
            self.teams = []


    @property
    def name(self) -> str:
        return self._name

    @property
    def date(self) -> str:
        return self._date

    @property
    def date(self) -> str:
        return self._date

    @property
    def prize_pool(self) -> float:
        return self._prize_pool

    @property
    def teams(self) -> [TeamMember]:
        # Повертаємо копію списку для захисту від прямої зміни ззовні
        return list(self._teams)

    def participateTournament(self, team: TeamMember) -> None:
        self._teams.append(team)

    def __repr__(self) -> str:
        return f"Tournament(name={self.name}, date={self.date}, prize_pool={self.prize_pool}, teams={self.teams})"



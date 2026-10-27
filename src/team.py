from src.team_member import TeamMember
from src.player import Player
from src.coach import Coach

class Team:
    def __init__(self, game):
        self._members = []
        self. _game = game

    @property
    def game(self):
        return self._game

    @property
    def members(self):
        return self._members

    def add_member(self, item):
        if isinstance(item, TeamMember):
            self._members.append(item)
        else:
            raise TypeError("Can only add TeamMember objects")

    def remove_member(self, member):
        self._members.remove(member)

    def get_all_players(self):
        return [item for item in self._members if isinstance(item, Player)]

    def get_all_coaches(self):
        return [item for item in self._members if isinstance(item, Coach)]

    def search(self, keyword):
        return [item for item in self._members if
                keyword.lower() in item.name.lower() or keyword.lower() in item.country.lower()]

    def search_by_age(self, age):
        return [item for item in self._members if item.age == age]

    def __str__(self):
        return f"Team with {len(self._members)} members | Game: {self._game}"

    def __repr__(self):
        return f"Team({self._members}, {self._game})"
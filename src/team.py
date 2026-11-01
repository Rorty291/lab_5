from src.team_member import TeamMember
from src.player import Player
from src.coach import Coach
from src.staff import Staff
import random

class Team:
    def __init__(self, name, game):
        self._members = []
        self._name = name
        self._game = game
        self._sponsor = None

    @property
    def name(self):
        return self._name

    @property
    def game(self):
        return self._game

    @property
    def members(self):
        return self._members

    @property
    def sponsor(self):
        return self._sponsor

    def remove_sponsor(self):
        self._sponsor = None

    def negotiate_sponsor(self, sponsor):
        result = sponsor.negotiate_sponsorship()
        if result:
            self._sponsor = sponsor

        return result

    def recruit_member(self, item):
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

    def get_all_staff_members(self):
        return [item for item in self._members if isinstance(item, Staff)]

    def search(self, keyword):
        return [item for item in self._members if
                keyword.lower() in item.name.lower() or
                keyword.lower() in item.country.lower() or
                (isinstance(item, Player) and keyword.lower() in item.abilities.lower()) or
                (isinstance(item, Coach) and keyword.lower() in item.style.lower())
                ]

    def search_by_age(self, age):
        return [item for item in self._members if item.age == age]

    def __str__(self):
        return f"Team {self.name} with {len(self.members)} members | Game: {self.game} | Sponsor: {self.sponsor}"

    def __repr__(self):
        return f"Team({self.name}, {self.members}, {self.game}, {self.sponsor})"
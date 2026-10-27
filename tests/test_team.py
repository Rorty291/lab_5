import unittest
from src.team import Team
from src.coach import Coach
from src.player import Player
from src.team_member import TeamMember

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.team = Team()
        self.player1 = Player("Olly Gordon", 18, "Greece", "987-654321")
        self.player2 = Player("Boris Jonson", 44, "Japan", "123-456789")
        self.coach = Coach("Alex Goren", 20, "Ukraine", "110-348573")

    def test_add_member(self):
        self.team.add_member(self.player1)
        self.assertEqual(len(self.team._members), 1)

    def test_add_invalid_member(self):
        with self.assertRaises(TypeError):
            self.team.add_member("Not a TeamMember object")

    def test_remove_member(self):
        self.team.add_member(self.player1)
        self.team.remove_member(self.player1)
        self.assertEqual(len(self.team.members), 0)

    def test_get_all_players(self):
        self.team.add_member(self.player1)
        self.team.add_member(self.player2)
        self.team.add_member(self.coach)
        players = self.team.get_all_players()
        self.assertEqual(len(players), 2)
        self.assertIsInstance(players[0], Player)
        self.assertIsInstance(players[1], Player)

    def test_get_all_coaches(self):
        self.team.add_member(self.player1)
        self.team.add_member(self.coach)
        coaches = self.team.get_all_coaches()
        self.assertEqual(len(coaches), 1)
        self.assertIsInstance(coaches[0], Coach)

    def test_search(self):
        self.team.add_member(self.player1)
        self.team.add_member(self.player2)
        self.team.add_member(self.coach)

        results = self.team.search("Counter-Strike 2")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "1984")

    def test_search_by_year(self):
        self.team.add_item(self.book1)
        self.team.add_item(self.book2)
        self.team.add_item(self.magazine)

        results = self.team.search_by_year(1949)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "1984")

    def test_str_representation(self):
        self.team.add_item(self.book1)
        expected = "Library with 1 items"
        self.assertEqual(str(self.team), expected)
import unittest
from src.team import Team
from src.coach import Coach
from src.player import Player
from src.sponsor import Sponsor

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.team = Team("TEST", "CS2")
        self.player1 = Player("Olly Gordon", 18, "Greece", "Rifler")
        self.player2 = Player("Boris Jonson", 44, "Japan", "Sniper")
        self.coach = Coach("Alex Goren", 20, "Ukraine", "Fast")
        self.sponsor = Sponsor("KNUCA_E-Sports")

    def test_negotiate_sponsor(self):
        res = self.team.negotiate_sponsor(self.sponsor)
        self.assertEqual(not res is None, True)

    def test_recruit_member(self):
        self.team.recruit_member(self.player1)
        self.assertEqual(len(self.team._members), 1)

    def test_add_invalid_member(self):
        with self.assertRaises(TypeError):
            self.team.recruit_member("Not a TeamMember object")

    def test_remove_member(self):
        self.team.recruit_member(self.player1)
        self.team.remove_member(self.player1)
        self.assertEqual(len(self.team.members), 0)

    def test_get_all_players(self):
        self.team.recruit_member(self.player1)
        self.team.recruit_member(self.player2)
        self.team.recruit_member(self.coach)

        players = self.team.get_all_players()

        self.assertEqual(len(players), 2)
        self.assertIsInstance(players[0], Player)
        self.assertIsInstance(players[1], Player)

    def test_get_all_coaches(self):
        self.team.recruit_member(self.player1)
        self.team.recruit_member(self.coach)
        coaches = self.team.get_all_coaches()
        self.assertEqual(len(coaches), 1)
        self.assertIsInstance(coaches[0], Coach)

    def test_search(self):
        self.team.recruit_member(self.player1)
        self.team.recruit_member(self.player2)
        self.team.recruit_member(self.coach)

        results = self.team.search("Rifler")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Olly Gordon")

    def test_search_by_age(self):
        self.team.recruit_member(self.player1)
        self.team.recruit_member(self.player2)
        self.team.recruit_member(self.coach)

        results = self.team.search_by_age(20)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].age, 20)

    def test_str_representation(self):
        self.team.recruit_member(self.player1)
        expected = "Team TEST with 1 members | Game: CS2 | Sponsor: None"
        self.assertEqual(str(self.team), expected)

    def test_repr_representation(self):
        self.team.recruit_member(self.player1)
        expected = "Team(TEST, [Player('Olly Gordon', 18, 'Greece', [Rifler])], CS2, None)"
        self.assertEqual(repr(self.team), expected)
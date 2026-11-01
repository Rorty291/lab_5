import unittest
from src.tournament import Tournament
from src.team import Team

class TestTournament(unittest.TestCase):
    def setUp(self):
        self.tournament = Tournament("Test Championship 2026", "2026-11-27", 10000)
        self.team1 = Team("TEST1", "CS2")
        self.team2 = Team("TEST2", "CS2")

    def test_attributes(self):
        self.assertEqual(self.tournament.name, "Test Championship 2026")
        self.assertEqual(self.tournament.date, "2026-11-27")
        self.assertEqual(self.tournament.prize, 10000)
        self.assertEqual(self.tournament.teams, [])

    def test_participate_tournament(self):
        self.tournament.participate_tournament(self.team1)
        self.assertEqual(len(self.tournament.teams), 1)
        self.assertEqual(self.tournament.teams[0], self.team1)

    def test_leave_tournament(self):
        self.tournament.participate_tournament(self.team1)
        self.tournament.leave_tournament(self.team1)
        self.assertEqual(len(self.tournament.teams), 0)

    def test_str_representation(self):
        expected = "Tournament: Test Championship 2026, Date: 2026-11-27, Prize pool: $10000"
        self.assertEqual(str(self.tournament), expected)

    def test_repr_representation(self):
        self.tournament.participate_tournament(self.team1)
        expected = "Tournament(name=Test Championship 2026, date=2026-11-27, prize_pool=10000, teams=[Team(TEST1, [], CS2, None)])"
        self.assertEqual(repr(self.tournament), expected)
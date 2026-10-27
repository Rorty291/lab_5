import unittest
from src.team_member import TeamMember

class TestTeamMember(unittest.TestCase):
    def setUp(self):
        self.member = TeamMember("Alex Goren", 20, "Ukraine")

    def test_attributes(self):
        self.assertEqual(self.member.name, "Alex Goren")
        self.assertEqual(self.member.age, 20)
        self.assertEqual(self.member.country, "Ukraine")

    def test_str_representation(self):
        expected = "Alex Goren (20 y.o.) from Ukraine"
        self.assertEqual(str(self.member), expected)

    def test_repr_representation(self):
        expected = "TeamMember('Alex Goren', 20, 'Ukraine')"
        self.assertEqual(repr(self.member), expected)
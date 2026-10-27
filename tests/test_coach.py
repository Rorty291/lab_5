import unittest
from src.coach import Coach

class TestCoach(unittest.TestCase):
    def setUp(self):
        self.coach = Coach("Alex Goren", 20, "Ukraine", "Slow")

    def test_attributes(self):
        self.assertEqual(self.coach.name, "Alex Goren")
        self.assertEqual(self.coach.age, 20)
        self.assertEqual(self.coach.country, "Ukraine")
        self.assertEqual(self.coach.style, "Slow")

    def test_str_representation(self):
        expected = "Alex Goren (20 y.o.) from Ukraine | Стиль: Slow"
        self.assertEqual(str(self.coach), expected)

    def test_repr_representation(self):
        expected = "Coach('Alex Goren', 20, 'Ukraine', [Slow])"
        self.assertEqual(repr(self.coach), expected)
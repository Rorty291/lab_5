import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Alex Goren", 20, "Ukraine", "Rifler")

    def test_attributes(self):
        self.assertEqual(self.player.name, "Alex Goren")
        self.assertEqual(self.player.age, 20)
        self.assertEqual(self.player.country, "Ukraine")
        self.assertEqual(self.player.abilities, "Rifler")

    def test_str_representation(self):
        expected = "Alex Goren (20 y.o.) from Ukraine | Навички: 780-846352"
        self.assertEqual(str(self.player), expected)

    def test_repr_representation(self):
        expected = "Player('Alex Goren', 20, 'Ukraine', [Rifler])"
        self.assertEqual(repr(self.player), expected)
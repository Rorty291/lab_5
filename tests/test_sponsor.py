import unittest
from src.sponsor import Sponsor

class TestSponsor(unittest.TestCase):
    def setUp(self):
        self.sponsor = Sponsor("KNUCA_E-Sports")

    def test_attributes(self):
        self.assertEqual(self.sponsor.name, "KNUCA_E-Sports")

    def test_negotiate_sponsorship(self):
        result = self.sponsor.negotiate_sponsorship()
        self.assertEqual(not result is None, True)

    def test_str_representation(self):
        expected = "Sponsorship with KNUCA_E-Sports"
        self.assertEqual(str(self.sponsor), expected)

    def test_repr_representation(self):
        expected = "Sponsor(name=KNUCA_E-Sports)"
        self.assertEqual(repr(self.sponsor), expected)
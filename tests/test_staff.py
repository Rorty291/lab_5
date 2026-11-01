import unittest
from src.staff import Staff

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.staff = Staff("Alex Goren", 20, "Ukraine", "Аналітик")

    def test_attributes(self):
        self.assertEqual(self.staff.name, "Alex Goren")
        self.assertEqual(self.staff.age, 20)
        self.assertEqual(self.staff.country, "Ukraine")
        self.assertEqual(self.staff.profession, "Аналітик")

    def test_str_representation(self):
        expected = "Alex Goren (20 y.o.) from Ukraine | Професія: Аналітик"
        self.assertEqual(str(self.staff), expected)

    def test_repr_representation(self):
        expected = "Staff('Alex Goren', 20, 'Ukraine', [Аналітик])"
        self.assertEqual(repr(self.staff), expected)
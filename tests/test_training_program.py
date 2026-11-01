import unittest
from src.trainingprogram import TrainingProgram

class TestTrainingProgram(unittest.TestCase):
    def setUp(self):
        self.program = TrainingProgram("Main", 5, "Beginner")

    def test_attributes(self):
        self.assertEqual(self.program.name, "Main")
        self.assertEqual(self.program.duration, 5)
        self.assertEqual(self.program.level, "Beginner")

    def test_str_representation(self):
        expected = "TrainingProgram: Main | Duration: 5 | Level: Beginner"
        self.assertEqual(str(self.program), expected)

    def test_repr_representation(self):
        expected = "TrainingProgram(name=Main, duration=5 weeks, level=Beginner)"
        self.assertEqual(repr(self.program), expected)
import unittest
from models.gym_class import Gym_class

class TestGymClass(unittest.TestCase):

    def setUp(self):
        self.gym_class = Gym_class('Cycling', 'David', 45, 10, 'off-Peak hours', 'Activate')

    def test_gym_class_has_name(self):
        self.assertEqual('Cycling', self.gym_class.name)

    def test_gym_class_has_teachere(self):
        self.assertEqual('David', self.gym_class.teacher)

    def test_gym_class_has_duration(self):
        self.assertEqual(45, self.gym_class.duration)

    def test_gym_class_has_capacity(self):
        self.assertEqual(10, self.gym_class.capacity)

    def test_gym_class_has_peak_hour(self):
        self.assertEqual('off-Peak hours', self.gym_class.peak_hour)

    def test_gym_class_has_state(self):
        self.assertEqual('Activate', self.gym_class.state)
        
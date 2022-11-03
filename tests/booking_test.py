import unittest
from models.booking import Booking
from models.gym_class import Gym_class
from models.member import Member

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member_1 = Member('Anna', 'Mackenzie', 'Standard', 'Activate')
        self.member_2 = Member('David', 'Brown', 'Premium', 'Activate')
        self.member_3 = Member('Mary', 'Thomson', 'Premium', 'Activate')

        self.gym_class_1 = Gym_class('Cycling', 'David', 45, 10, 'off-Peak hours', 'Activate')
        self.gym_class_2 = Gym_class('Yoga', 'Juy', 60, 18, 'off-Peak hours', 'Activate')
        self.gym_class_3 = Gym_class('Boxing', 'Kate', 45, 6, 'off-Peak hours', 'Activate')


        self.booking = Booking(self.member_1, self.gym_class_1)
        


    def test_booking_has_member(self):
        self.assertEqual('Anna', self.booking.member.first_name)

    def test_booking_has__gym_class(self):
        self.assertEqual('Cycling', self.booking.gym_class.name)
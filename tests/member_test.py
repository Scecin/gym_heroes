import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member('Anna', 'Mackenzie', 'Standard', 'Activate')

    def test_member_has_first_name(self):
        self.assertEqual('Anna', self.member.first_name)

    def test_member_has_last_name(self):
        self.assertEqual('Mackenzie', self.member.last_name)

    def test_member_has_membership(self):
        self.assertEqual('Standard', self.member.membership)

    def test_member_has_state(self):
        self.assertEqual('Activate', self.member.state)
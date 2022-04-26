from models.gym_class import Gym_class
from models.member import Member
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

member_1 = Member('Anna', 'Mackenzie', 'Standard')
member_repository.save(member_1)
member_2 = Member('David', 'Brown', 'Premium')
member_repository.save(member_2)
member_3 = Member('Mary', 'Thomson', 'Premium')
member_repository.save(member_3)

gym_class_1 = Gym_class('Cycling', 'David', 45, 10, 'Peak hour')
gym_class_repository.save(gym_class_1)
gym_class_2 = Gym_class('Yoga', 'Juy', 60, 18, 'off-Peak hours')
gym_class_repository.save(gym_class_2)

booking_1 = Booking(member_1, gym_class_1)
booking_repository.save(booking_1)
booking_2 = Booking(member_2, gym_class_2)
booking_repository.save(booking_2)
booking_3 = Booking(member_3, gym_class_1)
booking_repository.save(booking_3)
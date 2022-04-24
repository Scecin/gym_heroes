from models.gym_class import Gym_class
from models.member import Member
from models.gym import Gym

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.gym_repository as gym_repository

member_1 = Member('Anna', 'Mackenzie')
member_repository.save(member_1)

gym_class_1 = Gym_class('Cycling', 'David', 45)
gym_class_repository.save(gym_class_1)

gym = Gym('Gym Heros', member_1, gym_class_1)
gym_repository.save(gym)
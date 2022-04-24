from models.member import Member

import repositories.member_repository as member_repository

member_1 = Member('Anna', 'Mackenzie')
member_repository.save(member_1)
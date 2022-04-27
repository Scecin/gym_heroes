from repositories.member_repository import by_class

def check_capacity(gym_class):
    capacity = True
    if len(by_class(gym_class.id)) >= gym_class.capacity:
        capacity = False
    return  capacity



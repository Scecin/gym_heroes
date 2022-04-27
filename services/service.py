from repositories.member_repository import by_class

#  Check if there's free space in the class
def check_capacity(gym_class):
    capacity = True

    if len(by_class(gym_class.id)) >= gym_class.capacity:
        capacity = False
    return  capacity

# check the membership and hour kind to book a class
def check_membership_and_peak_hour(gym_class, member):
    membership = False

    if gym_class.peak_hour == "Peak hour" and member.membership == "Premium" or gym_class.peak_hour == "off-Peak hours" and member.membership == "Standard" or gym_class.peak_hour == "off-Peak hours" and member.membership == "Premium":
        membership = True

    return membership


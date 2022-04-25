from asyncio import FastChildWatcher
from repositories.member_repository import by_class

def check_capacity(gym_class):
    capacity = True
    if len(by_class(gym_class.id)) >= gym_class.capacity:
        capacity = False
    return  capacity

#check if it's peak hour
def check_peak_hour(gym_class):
    peak_hour = False
    if gym_class.peak_hour == True:
        peak_hour = True
    return peak_hour



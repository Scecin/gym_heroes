from db.run_sql import run_sql

from models.gym import Gym
from models.gym_class import Gym_class
from models.member import Member
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository

# save gym
def save(gym):
    sql = "INSERT INTO gyms (name, member_id, gym_class_id) VALUES (%s, %s, %s) RETURNING id"
    values = [gym.name, gym.member.id, gym.gym_class.id]
    results = run_sql (sql, values)
    gym.id = results[0]['id']
    return gym


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

# Select all the information inside gym
def select_all():
    gyms = []

    sql = "SELECT * FROM gyms"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        gym_class = gym_class_repository.select(row['gym_class_id'])
        gym = Gym(row['name'], member, gym_class, row['id'])
        gyms.append(gym)
    return gyms

# Select
def select(id):
    sql = "SELECT * FROM gyms WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = member_repository.select(result["member_id"])
    gym_class = gym_class_repository.select(result["gym_class_id"])
    gym = Gym(result["name"], member, gym_class, result["id"])
    return gym

# Delete all
def delete_all():
    sql = "DELETE FROM gyms"
    run_sql(sql)

# Delete just one
def delete(id):
    sql = "DELETE FROM gyms WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Update
def update(gym):
    sql = "UPDATE gyms SET (name, member_id, gym_class_id) = (%s, %s, %s) WHERE id = %s"
    values = [gym.name, gym.member.id, gym.gym_class.id, gym.id]
    run_sql(sql, values)
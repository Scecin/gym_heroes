from db.run_sql import run_sql
from models.gym_class import Gym_class

# Save classes
def save(gym_class):
    sql = "INSERT INTO gym_classes (name, teacher, duration) VALUES (%s, %s, %s) RETURNING id"
    values = [gym_class.name, gym_class.teacher, gym_class.duration]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class
from unittest import result
from db.run_sql import run_sql
from models.gym_class import Gym_class

# Save classes
def save(gym_class):
    sql = "INSERT INTO gym_classes (name, teacher, duration) VALUES (%s, %s, %s) RETURNING id"
    values = [gym_class.name, gym_class.teacher, gym_class.duration]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

# Select all Classes
def select_all():
    gym_classes = []

    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)

    for row in results:
        gym_class = Gym_class(row['name'], row['teacher'], row['duration'], row ['id'])
        gym_classes.append(gym_class)
    return gym_classes

# Select jus a class
def select(id):
   def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Gym_class(result['name'], result['teacher'], result['duration'], result['id'])
    return gym_class

# Update a class
def update(gym_class):
    sql = "UPDATE gym_classes SET name = %s Where id = %s"
    values = [gym_class.name, gym_class.teacher, gym_class.duration, gym_class.id]
    run_sql(sql, values)
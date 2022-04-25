from unittest import result
from controllers.member_controller import members
from db.run_sql import run_sql
from models.gym_class import Gym_class
from models.member import Member

# Save classes
def save(gym_class):
    sql = "INSERT INTO gym_classes (name, teacher, duration, capacity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [gym_class.name, gym_class.teacher, gym_class.duration, gym_class.capacity]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

# Select all Classes
def select_all():
    gym_classes = []

    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)

    for row in results:
        gym_class = Gym_class(row['name'], row['teacher'], row['duration'], row['capacity'], row ['id'])
        gym_classes.append(gym_class)
    return gym_classes

# Select jus a class
def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Gym_class(result['name'], result['teacher'], result['duration'], result['capacity'], result['id'])
    return gym_class

# Update a class
def update(gym_class):
    sql = "UPDATE gym_classes SET (name, teacher, duration, capacity) = (%s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, gym_class.teacher, gym_class.duration, gym_class.capacity, gym_class.id]
    run_sql(sql, values)

# Delete all members
def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

# Delete a member
def delete(id):
   sql = "DELETE FROM gym_classes WHERE id = %s"
   values = [id]
   run_sql(sql, values)
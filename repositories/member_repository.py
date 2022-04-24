from unittest import result
from db.run_sql import run_sql

from models.member import Member
from models.gym_class import Gym_class

# Save a member
def save(member):
    sql = "INSERT INTO members(first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [member.first_name, member.last_name]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

# Select all the members
def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['id'])
        members.append(member)
    return members


# Select just one member
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['id'])
    return member

# Update a member
def update(member):
    sql = "UPDATE members SET name = %s Where id = %s"
    values = [member.first_name, member.last_name, member.id]
    run_sql(sql, values)

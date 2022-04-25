from socket import SOCK_SEQPACKET
from unittest import result
from db.run_sql import run_sql

from models.member import Member
from models.gym_class import Gym_class

# Save a member
def save(member):
    sql = "INSERT INTO members(first_name, last_name, membership) VALUES (%s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.membership]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

# Select all the members
def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['membership'], row['id'])
        members.append(member)
    return members


# Select just one member
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['membership'], result['id'])
    return member

# Update a member
def update(member):
    sql = "UPDATE members SET (first_name, last_name, membership) = (%s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.membership, member.id]
    run_sql(sql, values)

# Delete all members
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

# Delete a member
def delete(id):
   sql = "DELETE FROM members WHERE id = %s"
   values = [id]
   run_sql(sql, values)

# check members in a class
def by_class(id):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.gym_class_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        member = Member(result["first_name"], result["last_name"], result["membership"])
        members.append(member)
    return members

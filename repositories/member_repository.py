from db.run_sql import run_sql

from models.member import Member
from models.gym_class import Class

# Save a member
def save(member):
    sql = "INSERT INTO members(first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [member.first_name, member.last_name]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member
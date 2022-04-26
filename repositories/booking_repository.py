from db.run_sql import run_sql

from models.booking import Booking
from models.gym_class import Gym_class
from models.member import Member
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository

# save booking
def save(booking):
    sql = "INSERT INTO bookings (member_id, gym_class_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.gym_class.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    booking.id = id

# Select bookings
def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    
    for row in results:
        member = member_repository.select(row["member_id"])
        gym_class = gym_class_repository.select(row["gym_class_id"])
        booking = Booking(member, gym_class, row["id"])
        bookings.append(booking)
    return bookings

# Select jusst one booking
def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is  not None:
        member = member_repository.select(result["member_id"])
        gym_class = gym_class_repository.select(result["gym_class_id"])
        booking = Booking(member, gym_class, result["id"])
    return booking

# Delete all
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

# Delete just one
def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Update
def update(booking):
    sql = "UPDATE bookings SET (member_id, gym_class_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.gym_class.id, booking.id]
    run_sql(sql, values)
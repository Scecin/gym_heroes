from crypt import methods
from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
from services.service import check_capacity, check_peak_hour

bookings_blueprint = Blueprint("bookings", __name__)

# INDEX
@bookings_blueprint.route("/bookings")
def booking():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

# NEW
@bookings_blueprint.route("/bookings/new")
def new_booking():
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template ("bookings/new.html", members = members, gym_classes = gym_classes)

# CREATE
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member_id = request.form["member_id"]
    gym_class_id = request.form["gym_class_id"]
    member = member_repository.select(member_id)
    gym_class = gym_class_repository.select(gym_class_id)
    if check_capacity(gym_class):
        # if member.membership == "Standard":
        #     if check_peak_hour(gym_class):
                new_booking = Booking(member, gym_class)
                booking_repository.save(new_booking)
    return redirect("/bookings")

#DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods = ["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")


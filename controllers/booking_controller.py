from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
from services.service import check_capacity


bookings_blueprint = Blueprint("bookings", __name__)

# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)


@bookings_blueprint.route("/refused")
def refused():
    return render_template("refused/index.html")

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
    print(gym_class.peak_hour)
    if check_capacity(gym_class):
        if gym_class.peak_hour == "Peak hour" and member.membership == "Premium" or gym_class.peak_hour == "off-Peak hours" and member.membership == "Standard" or gym_class.peak_hour == "off-Peak hours" and member.membership == "Premium":
            new_booking = Booking(member, gym_class)
            booking_repository.save(new_booking)
            return redirect("/bookings")
    return redirect("/refused")

#EDIT
@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking =booking_repository.select(id)
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("bookings/edit.html", booking = booking, members = members, gym_classes = gym_classes)

#UPDATE
@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    member_id = request.form["member_id"]
    gym_class_id = request.form["gym_class_id"]
    member = member_repository.select(member_id)
    gym_class = gym_class_repository.select(gym_class_id)
    booking = Booking(member, gym_class, id)
    booking_repository.update(booking)
    return redirect("/bookings")

#DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods = ["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")

# if member.membership == "Standard":
        #     if check_peak_hour(gym_class):


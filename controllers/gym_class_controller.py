from flask import Flask, redirect, render_template, request, Blueprint
from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository

gym_classes_blueprint = Blueprint("gym_classes", __name__)

# INDEX
@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes = gym_classes)

#NEW
@gym_classes_blueprint.route("/gym_classes/new")
def new_class():
    return render_template("gym_classes/new.html")

#CREATE
@gym_classes_blueprint.route("/gym_classes", methods = ['POST'])
def create_class():
    name = request.form["name"]
    teacher = request.form["teacher"]
    duration = request.form["duration"]
    new_class = Gym_class(name, teacher, duration)
    gym_class_repository.save(new_class)
    return redirect("/gym_classes")

# EDIT
@gym_classes_blueprint.route("/gym_classes/<id>/edit")
def edit_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template('gym_classes/edit.html', gym_class = gym_class)

# UPDATE
@gym_classes_blueprint.route("/gym_classes/<id>", methods=["POST"])
def update_class(id):
    name = request.form["name"]
    teacher = request.form["teacher"]
    duration = request.form["duration"]
    gym_class = Gym_class(name, teacher, duration, id)
    gym_class_repository.update(gym_class)
    return redirect("/gym_classes")
# from flask import Flask, render_template
# from flask import Blueprint
# from models.gym import Gym
# import repositories.gym_repository as gym_repository

# gyms_blueprint = Blueprint("gym", __name__)

# # INDEX
# @gyms_blueprint.route("/gym")
# def gym():
#     gyms = gym_repository.select_all()
#     return render_template("gym/index.html", gyms = gyms)
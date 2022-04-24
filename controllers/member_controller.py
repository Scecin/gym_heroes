from flask import Flask, redirect, render_template, request, Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

#INDEX
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

#NEW
@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")

#CREATE
@members_blueprint.route("/members", methods = ['POST'])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    new_member = Member(first_name, last_name)
    member_repository.save(new_member)
    return redirect("/members")


# EDIT
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member = member)

#UPDATE
@members_blueprint.route("/members<id>", methods = ['POST'])
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["lasst_name"]
    member = Member(first_name, last_name, id)
    member_repository.update(member)
    return redirect("/members")
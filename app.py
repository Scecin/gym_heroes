from flask import Flask, render_template

from controllers.member_controller import members_blueprint
from controllers.gym_class_controller import gym_classes_blueprint
# from controllers.gym_controller import gyms_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(gym_classes_blueprint)
# app.register_blueprint(gyms_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
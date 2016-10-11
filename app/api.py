from . import app, auth
from .models import User
from flask import jsonify, make_response, url_for, g

from publish import left, right, foward, reverse

# Tasks available

tasks = [
    {
        'id': 1,
        'description': 'left'
    },
    {
        'id': 2,
        'description': 'right'
    },
    {
        'id': 3,
        'description': 'forward'
    },
    {
        'id': 4,
        'description': 'reverse'
    }
]


# authentication
# @auth.verify_password
# def verify_password(username, password):
#     user = User.query.filter_by(username=username).first()
#     if not user or not user.verify_password(password):
#         return False
#     g.user = user
#     return True


# returns all the tasks
@app.route('/pi/app/tasks', methods=['GET'])
# @auth.login_required
def get_tasks():
    response = jsonify(tasks)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# handles 404 error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


# handles left task
@app.route('/pi/app/tasks/1', methods=['GET'])
# @auth.login_required
def left_command():
    left()
    response = jsonify(tasks[0])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# handles right task
@app.route('/pi/app/tasks/2', methods=['GET'])
# @auth.login_required
def right_command():
    right()
    response = jsonify(tasks[1])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# handles forward task
@app.route('/pi/app/tasks/3', methods=['GET'])
# @auth.login_required
def foward_command():
    foward()
    response = jsonify(tasks[2])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# handles reverse task
@app.route('/pi/app/tasks/4', methods=['GET'])
# @auth.login_required
def reverse_command():
    reverse()
    response = jsonify(tasks[3])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

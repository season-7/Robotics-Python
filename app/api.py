from . import app, auth
from .models import User
from flask import jsonify, make_response, url_for, g

from publish import left, right

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
        'description': 'foward'
    },
    {
        'id': 4,
        'description': 'reverse'
    }
]


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


@app.route('/pi/app/test')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})


@app.route('/pi/app/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.route('/pi/app/tasks/1', methods=['GET'])
@auth.login_required
def left_command():
    left()
    return jsonify(tasks[0])


@app.route('/pi/app/tasks/2', methods=['GET'])
@auth.login_required
def right_command():
    right()
    return jsonify(tasks[1])


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_tasks', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

from flask import Flask, jsonify, abort, make_response, url_for
from publish import left, right

app = Flask(__name__)

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


@app.route('/pi/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.route('/pi/api/tasks/1', methods=['GET'])
def left_command():
    left()
    return jsonify(tasks[0])


@app.route('/pi/api/tasks/2', methods=['GET'])
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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

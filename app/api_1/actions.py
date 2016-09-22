from flask import jsonify

from . import api


@api.route('')
def left():
    response = jsonify({'name': 'left'})
    return response

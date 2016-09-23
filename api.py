from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

tasks = {
    'left': 'Left',
    'right': 'Right',
    'reverse': 'Reverse',
    'foward': 'Foward'
}


class Foward(Resource):
    def get(self):
        return tasks['foward']


class Reverse(Resource):
    def get(self):
        return tasks['reverse']


class Left(Resource):
    def get(self):
        return tasks['left']


class Right(Resource):
    def get(self):
        return tasks['right']


api.add_resource(Foward, '/foward')
api.add_resource(Reverse, '/reverse')
api.add_resource(Left, '/left')
api.add_resource(Right, '/right')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

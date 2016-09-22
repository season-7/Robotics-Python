#!/usr/bin/env python
from app import create_app
from flask_script import Manager, Shell, Server

app = create_app('development')
manager = Manager(app)
server = Server(host='0.0.0.0')


def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", server)

if __name__ == '__main__':
    manager.run()

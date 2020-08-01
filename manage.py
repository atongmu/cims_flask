# -*- coding: utf-8 -*-
from flask_migrate import MigrateCommand
from flask_script import Manager

from app import create_app, config

app = create_app(config['development'])
# app = create_app(config['default'])
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()

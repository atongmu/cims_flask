# -*- coding: utf-8 -*-
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from app import create_app, config
from app.ext import db
from app.models import Managers

app = create_app(config['development'])

# 创建数据库迁移工具对象的步足有3步
# 1. 创建flask脚本管理工具对象
manager = Manager(app)

# 2. 创建数据库迁移工具对象
Migrate(app, db)

# 3. 向manager对象中添加数据库的操作命令
# 第一个参数是给这条命令取的名字叫什么,关于数据库的我们通常叫db
# 第二个参数就是具体的命令
manager.add_command("db", MigrateCommand)


# 创建管理员
@manager.command
def create_manager():
    managers = Managers(users_name="bing", password="888888")
    db.session.add(managers)
    try:
        db.session.commit()
        print(u"用户添加成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        print(u"用户添加失败")


if __name__ == "__main__":
    manager.run()

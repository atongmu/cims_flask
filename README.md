# flask_admin



#### 本地部署
*pip freeze > requirements.txt*
1. 安装依赖库 pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
2. 修改 app/config.py 数据库配置、app/__init__.py 环境配置。
3. 初始化数据库 python manage.py db init
4. 创建数据库 python manage.py db migrate
5. 创建数据库 python manage.py db upgrade
6. python table_sql.py create_ations
7. python table_sql.py create_permission 
8. python table_sql.py create_menu 
9. python table_sql.py create_role 
10. python table_sql.py create_user  *用户名和密码修改，table_sql.py下的create_user函数*
11. python table_sql.py create_role_permission
13. 测试运行 python manage.py runserver

#### ubuntu 16.04 部署

1. 安装虚拟环境

```bash
virtualenv venv
```

2. 激活虚拟环境

```bash
source venv/bin/activate 
```

3. 安装依赖库

```
pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
```

4. 安装uWSGI

```
pip install uwsgi
```

5. 利用supervisor重启uWSGI

```
sudo killall uwsgi
```

### 主要依赖说明

1. Flask-Cors 解决跨域问题
2. Flask-RESTful 用于在前端与后台进行通信的一套规范。
3. Flask-Caching 缓存组件 https://pythonhosted.org/Flask-Caching/
3. Flask-Avatars 头像生成工具组件 https://flask-avatars.readthedocs.io/en/latest/
4. flask-moment 时间和日期处理函数组件 https://github.com/miguelgrinberg/flask-moment/
4. Flask-Docs api文档

#### 使用说明


1.  接口文档 http://www.codingfly.site/admin_api/docs/api


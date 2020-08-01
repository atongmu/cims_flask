from flask import request


def load_middleware(app):
    @app.before_request
    def before():
        client_ip = request.remote_addr
        txt_before = "中间件:{}-{}".format(client_ip, request.url)
        print(txt_before)

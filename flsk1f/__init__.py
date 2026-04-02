from flask import Flask

from flsk1f.views import account, order


def create_app():
     app = Flask(__name__)
     from .views import account ,order
     app.register_blueprint(account.ac)
     app.register_blueprint(order.od)
     return app
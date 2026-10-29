from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.admin import admin
    app.register_blueprint(admin)

    return app

"""A script that starts a Flask web application"""

from flask import Flask
from flask_pymongo import PyMongo
from os import path
from flask_login import LoginManager

"""Naes the database"""
db = mongo(app)
DB_NAME = "database.db"

"""Creates a flask app"""
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'esbee27'
    app.config['MONGO_URI'] = 'mongodb://localhost/5000/{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

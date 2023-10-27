from flask import Flask
from website.utils.constants import DB_NAME, db
# from flask_login import LoginManager
from os import path

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "klew epqh"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+DB_NAME

    db.init_app(app)

    from website.views.views import views
    from website.auth.auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from website.models.user import User
    with app.app_context():
        create_database(app)
        # login_manager = LoginManager()
        # login_manager.login_view = "auth.login"
        # login_manager.init_app(app)
    
    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("/website"+DB_NAME):
        db.create_all()
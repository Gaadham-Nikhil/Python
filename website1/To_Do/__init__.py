from flask import Flask

#creating a function to create app
def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'Nikhil'
    
    from .views1 import views
    from .auth1 import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

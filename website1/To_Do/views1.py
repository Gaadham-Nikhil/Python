from flask import Blueprint, render_template

views = Blueprint("views", __name__)

#we set the route by giving blueprint variable name with character @ as @views in this case
#now we give the url of the route
@views.route('/')
def home():
    return render_template("home.html")

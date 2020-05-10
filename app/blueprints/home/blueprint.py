from flask import Blueprint, render_template, request

home = Blueprint('home', __name__)
@home.route('/home')
def route_name():
    return render_template('home.html') 

from flask import Blueprint, render_template, request, redirect, session
import requests ,json

page = Blueprint('page', __name__, template_folder='templates', static_folder='static/mainpage')
def check_login(login,password):
    url = 'http://unityddl.azurewebsites.net/login/teacher'
    post_data = {'email': login,
            'password': password}
    response = requests.post(url, post_data)
    return response

@page.route('/') #mainpage
def home():
    content = {
    }
    if request.method == 'GET':
        return render_template('mainpage/index.html', **content)






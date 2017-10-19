from flask import Blueprint, render_template, request, redirect, session
import requests ,json

page = Blueprint('page', __name__, template_folder='templates', static_folder='static/mainpage')
def check_login(login,password):
    url = 'http://unityddl.azurewebsites.net/login/teacher'
    post_data = {'email': login,
            'password': password}
    response = requests.post(url, post_data)
    return response
def get_student_stats():
    url = 'http://unityddl.azurewebsites.net/number/students'
    response = requests.get(url)
    return response.json()
def get_school_stats():
    url = 'http://unityddl.azurewebsites.net/number/school'
    response = requests.get(url)
    return response.json()
@page.route('/') #mainpage
def home():
    content = {
        'number_of_school':get_school_stats()['number'],
        'number_of_students': get_student_stats()['number']
    }
    if request.method == 'GET':
        return render_template('mainpage/index.html', content=content)






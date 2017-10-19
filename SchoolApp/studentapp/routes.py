from flask import Blueprint, render_template, request, session, redirect, url_for
import requests

studentpage = Blueprint('studentpage', __name__, template_folder='templates', static_folder='static')



def check_login(login,password):
    url = 'http://unityddl.azurewebsites.net/login/student'
    post_data = {'email': login,
            'password': password}
    response = requests.post(url, post_data)
    return response
def register_student(school_code,school_pass,email,password):# change
    url = 'http://unityddl.azurewebsites.net/register/student'
    post_data = {'email': email,
                 'password': password,
                 'key_code': school_code,
                 'key_pass': school_pass}
    response = requests.post(url, post_data)
    return response
def ApiGet(url_ending):
    url = 'http://unityddl.azurewebsites.net' + url_ending
    response = requests.get(url)
    return response

@studentpage.route('/login', methods=['GET' ,'POST'])  # login page
def loginstudent():
    if request.method == 'GET':
        return render_template('loginpage/loginscreen.html', object = '/student/login', object_register='/student/register', error = '',title = 'Logowanie do konta ucznia')
    if request.method == 'POST':
        data = check_login(request.form['email'] ,request.form['password'])
        if data.status_code != 401:
            session['student_name'] = data.json()['name']
            session['logged_as'] = 'student'
            session['school_id'] = data.json()['school']
            return redirect('/student')
        else:
            return render_template('loginpage/loginscreen.html', object = '/student/login', object_register='/student/register', error= 'Błędne dane', title = 'Logowanie do konta ucznia')

@studentpage.route('/register' ,methods=['GET' ,'POST'])
def register():
    error=''
    if request.method == 'POST':
        data = register_student(request.form['student_code'], request.form['student_pass'], request.form['email'],
                                request.form['password'],)
        if data.status_code == 500:
            error= 'Złe dane'
        else:
            redirect('/student/login')
    return render_template('studentregister.html', object ='/student/login', error=error)

@studentpage.route('/')
def studentmenu():
    if session.get('logged_as') != 'student':
        return redirect(url_for('studentpage.loginstudent'))
    return render_template('student.html')\


@studentpage.route('/ranking')
def studentranking():
    if session.get('logged_as') != 'student':
        return redirect(url_for('studentpage.loginstudent'))
    return render_template('segments/ranking.html')

@studentpage.route('/achivements')
def studentachivements():
    if session.get('logged_as') != 'student':
        return redirect(url_for('studentpage.loginstudent'))
#    return render_template('segments/achivements.html')

@studentpage.route('/game')
def studentgame():
    if session.get('logged_as') != 'student':
        return redirect(url_for('studentpage.loginstudent'))
   # return render_template('segments/game.html')



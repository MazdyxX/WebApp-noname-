from flask import Blueprint, render_template, request, session, redirect, url_for
import requests


teacherpage = Blueprint('teacherpage', __name__, template_folder='templates', static_folder='static')
current_class = ''
def check_login(login,password):
    url = 'http://unityddl.azurewebsites.net/login/teacher'
    post_data = {'email': login,
            'password': password}
    response = requests.post(url, post_data)
    return response
def register_teacher(school_code,school_pass,email,password):# put in on the test :v
    url = 'http://unityddl.azurewebsites.net/register/teacher'
    post_data = {'email': email,
                 'password': password,
                 'school_id': school_code,
                 'school_pass': school_pass}
    response = requests.post(url, post_data)
    return response
def ApiGet(url_ending):
    url = 'http://unityddl.azurewebsites.net' + url_ending
    try:
        response = requests.get(url).json()
        return response
    except:
        pass


###############ROUTES#####################

@teacherpage.route('/login', methods=['GET','POST']) #login page
def loginteacher():
    if request.method == 'GET':
        return render_template('loginpage/loginscreen.html', object = '/teacher/login', object_register='/teacher/register', error = '',title = 'Logowanie do konta nauczyciela')
    if request.method == 'POST':
        data = check_login(request.form['email'],
                           request.form['password'])
        if data.status_code != 401:
            session['teacher_name'] = data.json()['name']
            session['logged_as'] = 'teacher'
            session['school_id'] = data.json()['school']
            return redirect('/teacher')
        else:
            return render_template('loginpage/loginscreen.html', object = '/teacher/login', object_register='/teacher/register', error= 'Błędne dane', title = 'Logowanie do konta nauczyciela')
        
@teacherpage.route('/register',methods=['GET','POST'])
def register():
    error=''
    if request.method == 'POST':
        data = register_teacher(request.form['teacher_code'],
                                request.form['teacher_pass'],
                                request.form['email'],
                                request.form['password'],)
        if data.status_code == 500:
            error='Złe dane'
        else:
            redirect('/teacher/login')
    return render_template('teacherregister.html', object = '/teacher/login', error= error)


@teacherpage.route('/')
def index():
    if not session.get('logged_as') == 'teacher':
        return redirect('/teacher/login')
    else:
        content = {
            'classes': ApiGet('/class/show/'+ session.get('teacher_name')+ '/'+ session.get('school_id'))['classes']

        }
        return render_template('teacher.html', content=content)

@teacherpage.route('/<class_id>', methods=['POST','GET'])
def class_list(class_id = None):
    if session.get('logged_as') != 'teacher':
        return redirect('/')
    session['current_class'] = class_id
    content = {
        'students_ofclass': ApiGet('/student/points/'+class_id+'/'+session.get('school_id'))
    }
    return render_template('classlist.html', content = content)

@teacherpage.route('/<command>/<student_name>')
def changepoints(command = None, student_name = None):
    print("plusing called")
    if command == 'plus':
        ApiGet('/student/addPoints/' + student_name + '/'+session.get('current_class')+'/' + session.get('school_id'))
    if command == 'minus':
        ApiGet('/student/minusPoints/' + student_name + '/'+session.get('current_class')+'/' + session.get('school_id'))
    return redirect('/teacher/'+ session.get('current_class'))







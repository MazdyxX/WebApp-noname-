from flask import Blueprint, render_template, request, session, redirect, url_for
from . import api
import requests

adminpanel = Blueprint('adminpanel', __name__, template_folder='templates', static_folder='static')
apicont = api.apiController([],[])


@adminpanel.route('/login', methods=['GET','POST'])
def login():
    error = ''
    code = ''
    if request.method == 'POST':
        try:
            code = apicont.login(request.form['school_code'],request.form['school_pass'])
            if code != 'error':
                session['school_id']= code
                session['logged_as']='admin'
                return redirect('/admin')
            else:
                error = 'Błędne dane'
        except:
            error = 'Brak połączenia'
    return render_template('adminloginscreen.html', error = error)

@adminpanel.route('/')
def index():    
    if session.get('logged_as') != 'admin':
        return redirect('/admin/login')
    content = {
    }
    return render_template('adminpanel.html', content=content)


# -------------------------------------------------------------------#

@adminpanel.route('/classeslist/<command>', methods=['POST'])
@adminpanel.route('/classeslist', methods=['GET'])
def classlist(command = None):
    if session.get('logged_as') != 'admin':
        return redirect('/admin/login', code=302)
    if command == 'add':
        apicont.addclass(request.get_json(silent=True),session.get('school_id'))
    if command == 'delete':
        apicont.deleteclass(request.get_json(silent=True),session.get('school_id'))#refreshing to fix
    content = {
        'classes': apicont.getclasses(session.get('school_id'))
    }
    return render_template('lists/classes.html', content=content)


# -------------------------------------------------------------------#

@adminpanel.route('/teacherlist/<command>/<element>')
@adminpanel.route('/teacherlist', methods=['GET'])
def teacherlist(command = None, element= None):
    if session.get('logged_as') != 'admin':
        return redirect('/admin/login', code=302)
    if command == 'add':
        apicont.addteacher(element,session.get('school_id'))
    if command == 'delete':   
        apicont.deleteteacher(element,session.get('school_id'))
    content = {
        'teachers' : apicont.getteachers(session.get('school_id')),
        'unregistered_teachers': apicont.getunregistered_teachers(session.get('school_id'))
    }
    return render_template('lists/teachers.html', content=content)

# -------------------------------------------------------------------#@
@adminpanel.route('/studentform/<command>/<element>')
@adminpanel.route('/studentform/<command>')
@adminpanel.route('/studentform')
def studentform(command = None, element =None):
    if session.get('logged_as') != 'admin':
        return redirect('/admin/login', code=302)
    if command == 'initialize':
        apicont.getformlist(element,session.get('school_id'))
    elif command =='save':
        apicont.postformlist(session.get('school_id'))
    elif command =='add':
        apicont.addtoformlist(element, session.get('school_id'))
    elif command =='delete':
        apicont.deletefromformlist(element,session.get('school_id'))

    content = {
        'students': apicont.students_list
    }
    return  render_template('lists/studentform.html', content = content)

# -------------------------------------------------------------------#

@adminpanel.route('/assingedclasses/<element>')
@adminpanel.route('/assingedclasses')
def assingedclasses(element = None):
    if session.get('logged_as') != 'admin':
        return redirect('/admin/login', code=302)
    content = {
    'assinged_classes': apicont.getassigmentlist(element, session.get('school_id')),
    'possible_classes': apicont.getpossibleclasses(session.get('school_id'))
    }
    return  render_template('lists/classes_teacher.html', content = content)

# -------------------------------------------------------------------#
@adminpanel.route('/changeassigment/<command>/<element>')
def change_assigment(command = None, element = None):
    if command == 'add':
       apicont.addassigmenttolist(element,session.get('school_id'))
    if command == 'delete':
       apicont.deletefromassigmentlist(element,session.get('school_id'))
    return "refresh"
@adminpanel.route('/generate/<item>')
def givecodes(item=None):
    if item == 'teacher':
        response = requests.get('http://unityddl.azurewebsites.net/school/teacher/unregistered/' + session.get('school_id')).json()
        return render_template('lists/codes.html', codes=response)
    if item == 'students':
        response = requests.get('http://unityddl.azurewebsites.net/school/classes/'+session.get('school_id')).json()
        response = list((object['students'] for object in response['classes']))
        return render_template('lists/codes.html', codes = response)
    
from flask import Blueprint, render_template, request, session, redirect, url_for
from . import api

adminpanel = Blueprint('adminpanel', __name__, template_folder='templates', static_folder='static')
apicont = api.apiController([],[])



@adminpanel.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        code = apicont.login(request.form['school_code'],request.form['school_pass'])
        if code != 'error':
            session['school_id']= code
            session['logged_as']='admin'
        return redirect('/admin')
    return render_template('loginscreen.html')

@adminpanel.route('/')
def index():    
    if session.get('logged_as') != 'admin':
        return redirect('/admin/login')
    print(apicont.getclasses(session.get('school_id')))
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

@adminpanel.route('/teacherlist/<command>', methods=['POST'])
@adminpanel.route('/teacherlist', methods=['GET'])
def teacherlist(command = None):
    if session.get('logged_as') != 'admin':
        return redirect('/admin/login', code=302)
    if command == 'add':
        print("added" + request.get_json(silent=True))
        #apicont.addclass(request.get_json(silent=True))
    if command == 'delete':
        print("deleted" + request.get_json(silent=True))
        #apicont.deleteclass(request.get_json(silent=True))
    content = {
        'teachers' : apicont.getteachers(session.get('school_id'))
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
        apicont.getformlist(element)
    if command =='add':
        apicont.addtoformlist(element)
    if command =='delete':
        apicont.deletefromformlist(element)
    if command =='save':
        apicont.postformlist()#add json get
    content = {
        'students': apicont.students_list
    }
    return  render_template('lists/studentform.html', content = content)

# -------------------------------------------------------------------#

@adminpanel.route('/assingedclasses/<command>')
@adminpanel.route('/assingedclasses/<command>/<element>')
@adminpanel.route('/assingedclasses')
def assingedclasses(command = None, element = None):
    if session.get('logged_as') != 'admin':
        return redirect('/admin/login', code=302)
    if command == 'initialize':
        apicont.getassigmentlist(element)
    if command == 'add':
        apicont.addassigmenttolist(element)
    if command == 'delete':
        apicont.deletefromassigmentlist(element)
    if command == 'save':
        apicont.postassigmentlist()      # addjsonget
    content = {
        'assinged_classes': apicont.assigment_list,
        'possible_classes': apicont.getpossibleclasses()
    }
    return  render_template('lists/classes_teacher.html', content = content)

# -------------------------------------------------------------------#


    
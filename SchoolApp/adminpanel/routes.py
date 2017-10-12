from flask import Blueprint, render_template, request, session
from . import api

adminpanel = Blueprint('adminpanel', __name__, template_folder='templates', static_folder='static')
apicont = api.apiController
students_list = ['']




@adminpanel.route('/')
def index():
    content = {
    }
    return render_template('adminpanel.html', content=content)


# -------------------------------------------------------------------#

@adminpanel.route('/classeslist/<command>', methods=['POST'])
@adminpanel.route('/classeslist', methods=['GET'])
def classlist(command = None):
    if command == 'add':
        print("added" + request.get_json(silent=True))
        #apicont.addclass(request.get_json(silent=True))
    if command == 'delete':
        print("deleted" + request.get_json(silent=True))
        #apicont.deleteclass(request.get_json(silent=True))
    content = {
        'classes': apicont.getclasses(apicont, 2),
    }
    return render_template('lists/classes.html', content=content)


# -------------------------------------------------------------------#

@adminpanel.route('/teacherlist/<command>', methods=['POST'])
@adminpanel.route('/teacherlist', methods=['GET'])
def teacherlist(command = None):
    if command == 'add':
        print("added" + request.get_json(silent=True))
        #apicont.addclass(request.get_json(silent=True))
    if command == 'delete':
        print("deleted" + request.get_json(silent=True))
        #apicont.deleteclass(request.get_json(silent=True))
    content = {
        'teachers' : apicont.getteachers(apicont, 2),
    }
    return render_template('lists/teachers.html', content=content)

# -------------------------------------------------------------------#@
@adminpanel.route('/studentform/<command>/<element>')
@adminpanel.route('/studentform/<command>')
@adminpanel.route('/studentform')
def studentform(command = None, element =None):
    if command == 'initialize':
        students_list = apicont.getformlist(apicont,'2b')
    if command =='add':
        students_list.append(element)
    if command =='delete':
        students_list.remove(element)
    
    content = {
        'students': students_list
    }
    return  render_template('lists/studentform.html', content = content)

# -------------------------------------------------------------------#

@adminpanel.route('/assingedclasses')
def assingedclasses():
    content = {
        'students': "a"
    }
    return  render_template('lists/classes_teacher.html', content = content)

# -------------------------------------------------------------------#



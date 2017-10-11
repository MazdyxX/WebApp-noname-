from flask import Blueprint, render_template, request
from . import api

adminpanel = Blueprint('adminpanel', __name__, template_folder='templates', static_folder='static')
apicont = api.apiController

students = ['Tomek Marek','Adam Stańczuk','Piotr Karolak','Piotr Karolak','Piotr Karol']


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
        'classes': apicont.getclasses('2s'),
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
        'teachers' : apicont.getteachers('2s'),
    }
    return render_template('lists/teachers.html', content=content)

# -------------------------------------------------------------------#@

@adminpanel.route('/studentform')
def studentform():
    content = {
        'students':students
    }
    return  render_template('lists/studentform.html', content = content)

# -------------------------------------------------------------------#

@adminpanel.route('/assingedclasses')
def studentform():
    content = {
        'students':students
    }
    return  render_template('lists/classes_teacher.html', content = content)

# -------------------------------------------------------------------#



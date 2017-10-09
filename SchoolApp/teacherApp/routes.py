from flask import Blueprint, render_template, request


teacherpage = Blueprint('teacherpage', __name__, template_folder='templates', static_folder='static')

#TESTSTUFF!!DELETE#
students = ['Tomek Marek','Adam Stańczuk','Piotr Karolak']
classes = ['2F', '3B', '4C', '4A', '5M']
@teacherpage.route('/')
def index():
    content = {
        'classes': classes
    }
    return render_template('teacher.html', content=content)
@teacherpage.route('/<class_id>')
def class_list(class_id):
    #here will be query for students in class#
    content = {
        'classes': classes,
        'students_ofclass': students
    }
    return render_template('classlist.html', content = content)

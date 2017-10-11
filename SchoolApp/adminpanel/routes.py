from flask import Blueprint, render_template, request

adminpanel = Blueprint('adminpanel', __name__, template_folder='templates', static_folder='static')

teachers = ['Tomek Marek','Adam Stańczuk','Piotr Karolak']
students = ['Tomek Marek','Adam Stańczuk','Piotr Karolak','Piotr Karolak','Piotr Karol']
classes = ['2F', '3B', '4C', '4A', '5M']
@adminpanel.route('/')
def index():
    content = {
    }
    return render_template('adminpanel.html', content=content)


# -------------------------------------------------------------------#

@adminpanel.route('/classeslist', methods=['POST','GET'])
def classlist():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        classes.append(data)
    content = {
        'classes': classes,
    }
    return render_template('lists/classes.html', content=content)


# -------------------------------------------------------------------#

@adminpanel.route('/teacherlist')
def teacherlist():
    content = {
        'teachers' : teachers
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



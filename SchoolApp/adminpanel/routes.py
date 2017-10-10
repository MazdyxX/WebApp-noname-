from flask import Blueprint, render_template, request

adminpanel = Blueprint('adminpanel', __name__, template_folder='templates', static_folder='static')


@adminpanel.route('/')
def index():
    content = {
      #'classes': classes,
      #'students': students,
      #'teachers': teachers,
    }
    return render_template('adminpanel.html', content=content)


# -------------------------------------------------------------------#

@adminpanel.route('/<class_id>')
def classlist(class_id):
    content = {
        #'class': class_id
       # 'assinged_students': assinged_students,
    }
    return render_template('studentlist.html')


# -------------------------------------------------------------------#

@adminpanel.route('/<teacher_id>')
def teacherlist(teacher_id):
    content = {
        #'teacher': teacher_id,
        #'assinged_classes': assinged_classes,

    }
    return render_template('assingedclasses_list')



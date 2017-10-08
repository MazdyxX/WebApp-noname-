from flask import Blueprint, render_template, request


teacherpage = Blueprint('teacherpage', __name__, template_folder='templates', static_folder='static/teacherpage')

@teacherpage.route('/')
def index():
    return render_template('teacher.html')
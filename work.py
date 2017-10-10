from flask import Blueprint, render_template, request


adminpage = Blueprint('teacherpage', __name__, template_folder='templates', static_folder='static')

@adminpage.route('')
def index():
  

from flask import Flask, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

from SchoolApp.mainpage.routes import page
from SchoolApp.teacherApp.routes import teacherpage

app.register_blueprint(page)
app.register_blueprint(teacherpage, url_prefix="/teacher")





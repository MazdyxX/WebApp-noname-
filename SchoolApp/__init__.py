from flask import Flask, redirect, render_template, request, session, abort
import os, binascii

app = Flask(__name__)
app.secret_key = binascii.hexlify(os.urandom(24))

from SchoolApp.mainpage.routes import page
from SchoolApp.teacherApp.routes import teacherpage
from SchoolApp.adminpanel.routes import adminpanel

app.register_blueprint(page)
app.register_blueprint(teacherpage, url_prefix="/teacher")
app.register_blueprint(adminpanel, url_prefix="/admin")





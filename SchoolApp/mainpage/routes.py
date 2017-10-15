from flask import Blueprint, render_template, request, redirect


page = Blueprint('page', __name__, template_folder='templates', static_folder='static/mainpage')

def check():
    return True

@page.route('/') #mainpage
def index():
    content = {
    }
    if request.method == 'POST':
        login();
    if request.method == 'GET':
        return render_template('mainpage/index.html', **content)

@page.route('/loginstudent', methods=['GET','POST']) #login page
def loginstudent():
    if request.method == 'GET':

        return render_template('loginpage/loginscreen.html', object = '/loginstudent' )
    if request.method == 'POST':
        if check():
            return redirect('/student')


@page.route('/loginteacher', methods=['GET','POST']) #login page
def loginteacher():
    if request.method == 'GET':

        return render_template('loginpage/loginscreen.html', object = '/loginteacher')
    if request.method == 'POST':
        if check():
            return redirect('/teacher')


       
        



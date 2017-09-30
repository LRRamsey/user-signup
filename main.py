from flask import Flask , request, redirect, render_template
import cgi
import os 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('welcome_form.html')


@app.route("/hello", methods=['POST'])
def validate_info():
    username = str(request.form['username'])
    username_from_form = username
    username_error = ''

    if len(username_from_form) <= 0:
        username_error = "user name must contain at least 3 characters"

    if len(username_from_form) < 3:
        username_error = "user name must be longer than 3 charachters"

    if len(username_from_form) > 20:
        username_error = "user name cannot be longer than 20 characters"

    if " " in username_from_form:
        username_error = "user name may not contain spaces"


    password = str(request.form['password'])
    password_conf = str(request.form['password_conf'])
    password_error = ''
    
    if password != password_conf:
        password_error = "passwords do not match, please re enter."

    if len(password) <= 0:
        password_error = "password must contain at least 3 characters"

    if len(password) < 3:
        password_error = "password must be longer than 3 charachters"

    if len(password) > 20:
        password_error = "password cannot be longer than 20 characters"

    if " " in password:
        password_error = "password may not contain spaces"

 
    email_from_form = str(request.form['email'])
    email_error = ''

    if "." not in email_from_form:
        email_error = "please enter a valid email"

    if "@" not in email_from_form:
        email_error = "email must contain @ sign"

    if len(email_from_form) < 3:
        email_error = "email must be longer than 3 charachters"

    #if len(email) > 30:
    #    email_error = "email must be shorter than 20 characters"

    if " " in email_from_form:
        email_error = "email may not contain spaces"

    if not email_error and not username_error and not password_error:
        return redirect('/successful_sign_in'.format(username))

    else:
        return render_template('welcome_form.html', email_error=email_error, 
        password_error=password_error, username_error=username_error, 
        username=username_from_form, email=email_from_form)

@app.route('/successful_sign_in')
def success():
    return render_template('successful_sign_in.html')

app.run()
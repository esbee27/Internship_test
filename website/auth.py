from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from .models import Student
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


"""Login route"""
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Student.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=False)
                return redirect(url_for(''))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html")


"""Sign up route"""
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        
        user = Student.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 6:
            flash("Email must be greater than 5 characters", category='error')
        
        else:
            new_user = Student(email=email, id=id, username=username)
            db.session.add(new_user)
            db.session.commit()
            session['email'] = email
            flash("Account created successfully", category='success')
            return redirect(url_for('auth.login')

    return render_template('signup.html')


    
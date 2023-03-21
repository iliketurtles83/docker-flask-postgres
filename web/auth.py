from flask import Blueprint, redirect, render_template, request, url_for, abort, flash
from flask_login import login_required, login_user, logout_user
from web.models import db, User
from web.forms import LoginForm
import bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        hashed_pass = bcrypt.checkpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        print(user.password)
        print(hashed_pass)
        if user and user.password == hashed_pass:
            login_user(user)
            return redirect(url_for('main.hello'))
        else:
            return "Login failed"
    return "End of line"

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.hello'))

@auth.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = LoginForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first() == None:
            hashed_pass = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
            print(hashed_pass)
            user = User(
                email=form.email.data,
                password=hashed_pass
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.hello'))
        else:
            return "user exists"
    else:
        print(form.errors)

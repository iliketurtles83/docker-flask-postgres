from flask import Blueprint, redirect, url_for
from flask_login import login_required, login_user, logout_user
from project.models import db, User
from project.forms import LoginForm
import bcrypt
import binascii

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and bcrypt.checkpw(form.password.data.encode('utf-8'), binascii.unhexlify(user.password)):
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
            user = User(
                email=form.email.data,
                password=binascii.hexlify(hashed_pass)
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.hello'))
        else:
            return "user exists"
    else:
        print(form.errors)

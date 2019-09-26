from flask import (
    render_template, send_from_directory, current_app, flash, redirect, url_for,
)
from flask_login import current_user, login_user, login_required

from . import main_bp
from .forms import LoginForm
from app.models import User

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.manage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('main.login'))
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('main.manage'))
    return render_template('login.html', form=form)

@main_bp.route('/manage')
@login_required
def manage():
    return render_template('manage.html')

@main_bp.route('/resume')
def resume():
    return send_from_directory(current_app.static_folder, 'Resume.pdf')

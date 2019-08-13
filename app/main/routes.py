from . import main_bp
from flask import (
    render_template, send_from_directory, current_app
)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/resume')
def resume():
    return send_from_directory(current_app.static_folder, 'Resume.pdf')

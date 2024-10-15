from app import app
from flask import render_template

@app.route('/new_registration', methods=['GET'])
def new_registration():
    return render_template('new_registration.html')

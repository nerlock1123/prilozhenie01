from app import app
from flask import render_template, request, redirect, url_for
from utils import get_db_connection
from models.new_student_model import add_student

@app.route('/new_student', methods=['GET', 'POST'])
def new_student():
    if request.method == 'POST':
        student_name = request.form['student_name']
        student_number = request.form['student_number']
        student_degree = request.form['student_degree']

        conn = get_db_connection()
        add_student(conn, student_name, student_number, student_degree)

        return redirect(url_for('index'))

    return render_template('new_student.html')

from app import app
from flask import render_template, request, redirect, url_for
from utils import get_db_connection

# Страница для добавления нового преподавателя
@app.route('/new_teacher', methods=['GET', 'POST'])
def new_teacher():
    conn = get_db_connection()

    if request.method == 'POST':
        teacher_name = request.form['teacher_name']
        teacher_number = request.form['teacher_number']
        teacher_adress = request.form['teacher_adress']

        cur = conn.cursor()
        cur.execute('INSERT INTO teacher (teacher_name, teacher_number, teacher_adress) VALUES (?, ?, ?)',
                    (teacher_name, teacher_number, teacher_adress))
        conn.commit()

        return redirect(url_for('teacher'))

    return render_template('new_teacher.html')

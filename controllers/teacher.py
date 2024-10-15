from app import app
from flask import render_template, request, session, redirect, url_for
from utils import get_db_connection
from models.teacher_model import get_teachers, get_subject, get_programs

# Страница с преподавателями
@app.route('/teacher', methods=['GET'])
def teacher():
    conn = get_db_connection()

    # Логика выбора преподавателя
    if request.args.get('teacher'):
        teacher_id = int(request.args.get('teacher'))
        session['teacher_id'] = teacher_id
    else:
        session['teacher_id'] = 1  # По умолчанию выбран первый преподаватель

    # Получаем список преподавателей и программ
    df_teachers = get_teachers(conn)
    df_programs = get_programs(conn, session['teacher_id'])

    # Выбранный преподаватель
    selected_teacher = df_teachers[df_teachers['teacher_id'] == session['teacher_id']].iloc[0]

    # Получаем предмет преподавателя (первый предмет, по которому есть программы)
    subject = get_subject(conn, session['teacher_id'])

    return render_template('teacher.html', 
                           teacher_id=session['teacher_id'],
                           combo_box_teachers=df_teachers,
                           combo_box_teachers_len=len(df_teachers),
                           selected_teacher=selected_teacher,
                           subject=subject,  # Подгружаем предмет
                           programs=df_programs)

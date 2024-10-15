from app import app
from flask import render_template, request, session, redirect, url_for
from utils import get_db_connection
from models.index_model import get_students, get_schedule

# Функция для выбора страницы работы с учениками
@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()

    # Логика выбора ученика
    if request.args.get('student'):
        student_id = int(request.args.get('student'))
        session['student_id'] = student_id
    else:
        session['student_id'] = 1  # Стандартный выбор, если нет студента в сессии

    # Получаем информацию обо всех студентах и выбранном студенте
    df_students = get_students(conn)
    
    # Проверка, что выбранный студент есть в базе
    selected_student = df_students[df_students['student_id'] == session['student_id']].iloc[0]

    # Получаем расписание выбранного студента
    df_schedule = get_schedule(conn, session['student_id'])

    students_len = len(df_students)
    schedule_len = len(df_schedule)

    # Передаем данные в шаблон
    return render_template('index.html', 
                           student_id=session['student_id'], 
                           combo_box_1=df_students, 
                           combo_box_1_len=students_len, 
                           selected_student=selected_student,  # Данные выбранного студента
                           schedule=df_schedule, 
                           schedule_len=schedule_len)

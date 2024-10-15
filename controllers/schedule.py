from app import app
from flask import render_template, request
from utils import get_db_connection
from models.schedule_model import get_filtered_schedule, get_teachers, get_subjects

@app.route('/schedule', methods=['GET'])
def schedule():
    conn = get_db_connection()

    # Получаем список всех преподавателей и предметов для фильтра
    teachers = get_teachers(conn)
    subjects = get_subjects(conn)

    # Получаем параметры фильтров из запроса
    selected_teacher = request.args.get('teacher')
    selected_subject = request.args.get('subject')

    # Преобразуем в None, если фильтр не выбран
    if not selected_teacher:
        selected_teacher = None
    if not selected_subject:
        selected_subject = None

    # Получаем отфильтрованное расписание на основе выбранных фильтров
    schedule = get_filtered_schedule(conn, selected_teacher, selected_subject)

    return render_template('schedule.html', 
                           teachers=teachers, 
                           subjects=subjects,
                           selected_teacher=selected_teacher,
                           selected_subject=selected_subject,
                           schedule=schedule)

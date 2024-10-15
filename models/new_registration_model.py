import pandas as pd

def get_available_schedule(conn):
    return pd.read_sql('''
        SELECT
        schedule.schedule_id,
        schedule.schedule_day AS Дата_занятия,
        teacher.teacher_name AS Преподаватель,
        program.program_name AS Программа,
        program.program_degree AS Класс_или_Курс,
        program.program_price AS Стоимость
        FROM schedule
        JOIN teacher ON schedule.teacher_id = teacher.teacher_id
        JOIN program ON schedule.program_id = program.program_id
        ORDER BY schedule.schedule_day
    ''', conn)

def add_registration(conn, student_id, schedule_id):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO registration (student_id, schedule_id)
        VALUES (?, ?)
    ''', (student_id, schedule_id))
    conn.commit()

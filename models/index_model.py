import pandas as pd

def get_students(conn):
    # Получение списка студентов из базы данных
    query = 'SELECT student_id, student_name, student_number, student_degree FROM student'
    df_students = pd.read_sql(query, conn)
    return df_students

def get_student(conn):
    return pd.read_sql('SELECT * FROM student', conn)

def get_teacher(conn):
    return pd.read_sql('SELECT * FROM teacher', conn)

def get_schedule(conn, student_id):
    query = '''
    SELECT 
        r.registration_id, 
        t.teacher_name AS "Преподаватель", 
        p.program_name AS "Программа", 
        p.program_degree AS "Класс_или_Курс", 
        p.program_price AS "Стоимость", 
        s.schedule_day AS "Дата_занятия"
    FROM registration r
    JOIN schedule s ON r.schedule_id = s.schedule_id
    JOIN teacher t ON s.teacher_id = t.teacher_id
    JOIN program p ON s.program_id = p.program_id
    WHERE r.student_id = ?
    '''
    df_schedule = pd.read_sql(query, conn, params=(student_id,))
    return df_schedule


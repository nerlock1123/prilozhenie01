import pandas as pd

def get_teachers(conn):
    return pd.read_sql('SELECT teacher_id, teacher_name FROM teacher', conn)

def get_programs_by_teacher(conn, teacher_id):
    query = '''
    SELECT p.program_id, p.program_name
    FROM program p
    JOIN teacher t ON t.teacher_id = ?
    WHERE p.subject_id = (
        SELECT p2.subject_id 
        FROM program p2
        JOIN teacher t2 ON t2.teacher_id = ?
        LIMIT 1
    )
    '''
    return pd.read_sql(query, conn, params=(teacher_id, teacher_id))

def add_schedule(conn, teacher_id, program_id, schedule_day):
    try:
        query = '''
        INSERT INTO schedule (teacher_id, program_id, schedule_day)
        VALUES (?, ?, ?)
        '''
        conn.execute(query, (teacher_id, program_id, schedule_day))
        conn.commit()
        print(f"Занятие добавлено: Преподаватель ID {teacher_id}, Программа ID {program_id}, Дата {schedule_day}")
    except Exception as e:
        print(f"Ошибка при добавлении занятия: {e}")


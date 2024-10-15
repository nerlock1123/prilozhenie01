import pandas as pd

def get_teachers(conn):
    query = 'SELECT teacher_id, teacher_name FROM teacher'
    return pd.read_sql(query, conn)

def get_subjects(conn):
    query = 'SELECT subject_id, subject_name FROM subject'
    return pd.read_sql(query, conn)

def get_filtered_schedule(conn, teacher_id=None, subject_id=None):
    query = '''
    SELECT t.teacher_name, s.subject_name, p.program_name, sch.schedule_day, ti.time_hour
    FROM schedule sch
    JOIN program p ON sch.program_id = p.program_id
    JOIN teacher t ON sch.teacher_id = t.teacher_id
    JOIN subject s ON p.subject_id = s.subject_id
    JOIN registration r ON sch.schedule_id = r.schedule_id
    JOIN time ti ON r.registration_time = ti.time_hour
    WHERE (? IS NULL OR sch.teacher_id = ?)
    AND (? IS NULL OR p.subject_id = ?)
    ORDER BY sch.schedule_day, ti.time_hour
    '''
    return pd.read_sql(query, conn, params=(teacher_id, teacher_id, subject_id, subject_id))



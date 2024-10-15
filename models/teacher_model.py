import pandas as pd

def get_teachers(conn):
    query = 'SELECT teacher_id, teacher_name, teacher_number, teacher_adress FROM teacher'
    df_teachers = pd.read_sql(query, conn)
    return df_teachers

def get_subject(conn, teacher_id):
    query = '''
    SELECT s.subject_name 
    FROM subject s 
    JOIN program p ON s.subject_id = p.subject_id 
    JOIN schedule sc ON p.program_id = sc.program_id 
    WHERE sc.teacher_id = ?
    LIMIT 1
    '''
    df_subject = pd.read_sql(query, conn, params=(teacher_id,))
    return df_subject.iloc[0]['subject_name'] if not df_subject.empty else None

def get_programs(conn, teacher_id):
    query = '''
    SELECT program_name 
    FROM program p 
    JOIN schedule s ON p.program_id = s.program_id 
    WHERE s.teacher_id = ?
    '''
    df_programs = pd.read_sql(query, conn, params=(teacher_id,))
    return df_programs

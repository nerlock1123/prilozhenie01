def add_student(conn, student_name, student_number, student_degree):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO student (student_name, student_number, student_degree)
        VALUES (?, ?, ?)
    ''', (student_name, student_number, student_degree))
    conn.commit()

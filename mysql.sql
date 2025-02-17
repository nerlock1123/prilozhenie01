-- Таблица student
CREATE TABLE student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(100) NOT NULL,
    student_number VARCHAR(20) NOT NULL,
    student_degree VARCHAR(50)
);

-- Таблица teacher
CREATE TABLE teacher (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_name VARCHAR(100) NOT NULL,
    teacher_number VARCHAR(20) NOT NULL,
    teacher_adress VARCHAR(255) NOT NULL
);

-- Таблица subject
CREATE TABLE subject (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(100) NOT NULL
);

-- Таблица program
CREATE TABLE program (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    program_name VARCHAR(100) NOT NULL,
    program_degree VARCHAR(50) NOT NULL,
    program_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES subject(subject_id) ON DELETE CASCADE
);

-- Таблица time
CREATE TABLE time (
   time_id INTEGER PRIMARY KEY AUTOINCREMENT,
   time_hour TIME NOT NULL
);

-- Таблица schedule
CREATE TABLE schedule (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    schedule_day DATE NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES program(program_id) ON DELETE CASCADE
);

-- Таблица registration
CREATE TABLE registration (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    schedule_id INTEGER,
    registration_time TIME,
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (schedule_id) REFERENCES schedule(schedule_id) ON DELETE CASCADE
);

INSERT INTO student (student_name, student_number, student_degree) VALUES 
('Кагиров В.С.', '+7502887547', '1-9 класс'), 
('Бушуев Р.А.', '+79142887532', '10-11 класс'), 
('Филатов Д.А.', '+79086074565', '1-4 курс'), 
('Степанов С.В.', '+79506547654', '1-9 класс'), 
('Безруков А.А.', '+79145674322', '1-9 класс'), 
('Васильев В.П.', '+79243247654', '10-11 класс'),
('Новиков М.А.', '+79502885434', '10-11 класс'),
('Хорин С.В.', '+79085678532', '1-4 курс'),
('ДУбов С.М.', '+79146578943', '10-11 класс'),
('Дорозова У.М.', '+79504356677', '1-9 класс'),
('Медведьева М.П.', '+79246784381', '1-4 курс'),
('Корпин Д.Д.', '+79507849723', '11-11 класс'),
('Захаров В.Н.', '+79244690227', '1-4 курс'),
('Шухлин С.М.', '+79081178213', '10-11 класс'),
('Кустов В.И.', '+79506238407', '1-4 курс');

INSERT INTO subject (subject_name) VALUES
('Математика'),
('Физика'),
('Химия'),
('Русский язык'),
('История'),
('Английский язык'),
('Обществознание'),
('Экономика');

INSERT INTO program (subject_id, program_name, program_degree, program_price) VALUES
('1', 'Подготовка к ОГЭ', '1-9 класс', 1500),
('1', 'Подготовка к ЕГЭ', '10-11 класс', 2000),
('1', 'Общая подготовка', '1-9 класс', 1200),
('1', 'Линейная алгебра', '1-4 курс', 2000),
('2', 'Подготовка к ОГЭ', '1-9 класс', 1800),
('2', 'Подготовка к ЕГЭ', '10-11 класс', 2200),
('2', 'Теоретическая физика', '1-4 курс', 2500),
('2', 'Общая физика', '1-9 класс', 1600),
('3', 'Подготовка к ОГЭ', '1-9 класс', 1700),
('3', 'Подготовка к ЕГЭ', '10-11 класс', 2100),
('3', 'Органическая химия', '1-4 курс', 2300),
('3', 'Неорганическая химия', '1-4 курс', 2300),
('4', 'Подготовка к ОГЭ', '1-9 класс', 1400),
('4', 'Подготовка к ЕГЭ', '10-11 класс', 1900),
('4', 'Общая подготовка', '1-9 класс', 1100),
('5', 'Подготовка к ОГЭ', '1-9 класс', 1600),
('5', 'Подготовка к ЕГЭ', '10-11 класс', 2000),
('5', 'История России', '1-4 курс', 1800),
('6', 'Подготовка к ОГЭ', '1-9 класс', 1500),
('6', 'Подготовка к ЕГЭ', '10-11 класс', 2000),
('6', 'Общая подготовка', '1-9 класс', 1200),
('6', 'Разговорный английский', '1-4 курс', 2500),
('7', 'Подготовка к ОГЭ', '1-9 класс', 1700),
('7', 'Подготовка к ЕГЭ', '10-11 класс', 2200),
('7', 'Социология', '1-4 курс', 2100),
('8', 'Основы экономики', '1-9 класс', 1800),
('8', 'Подготовка к ЕГЭ', '10-11 класс', 2400),
('8', 'Микроэкономика', '1-4 курс', 2600);

INSERT INTO teacher (teacher_name, teacher_number, teacher_adress) VALUES
('Попова Е.А.', '+79144357742', 'ул. Светланская, 11'),
('Иванов И.И.', '+79141234567', 'ул. Пушкина, 25'),
('Смирнова О.В.', '+79147896543', 'ул. Ленина, 18'),
('Кузнецова М.С.', '+79149871234', 'пр. Мира, 5'),
('Сидоров А.П.', '+79142345678', 'ул. Гагарина, 8'),
('Фёдорова Н.Г.', '+79141239876', 'ул. Октябрьская, 3'),
('Михайлова Л.В.', '+79148765432', 'ул. Первомайская, 12'),
('Николаев С.В.', '+79143456789', 'ул. Красная, 17'),
('Петрова Е.И.', '+79142347890', 'ул. Советская, 22'),
('Васильев В.А.', '+79149874561', 'ул. Дальневосточная, 9');

INSERT INTO schedule (teacher_id, program_id, schedule_day) VALUES
('1', '1', '2024-01-10'), -- Попова Е.А. ведет подготовку к ОГЭ по математике
('1', '2', '2024-01-10'), -- Попова Е.А. ведет подготовку к ЕГЭ по математике
('1', '3', '2024-01-11'), -- Попова Е.А. ведет общую подготовку по математике
('1', '4', '2024-01-12'), -- Попова Е.А. ведет линейную алгебру
('2', '5', '2024-01-12'), -- Иванов И.И. ведет подготовку к ОГЭ по физике
('2', '6', '2024-01-13'), -- Иванов И.И. ведет подготовку к ЕГЭ по физике
('2', '7', '2024-01-14'), -- Иванов И.И. ведет теоретическую физику
('2', '8', '2024-01-15'), -- Иванов И.И. ведет общую физику
('3', '9', '2024-01-15'), -- Смирнова О.В. ведет подготовку к ОГЭ по химии
('3', '10', '2024-01-16'), -- Смирнова О.В. ведет подготовку к ЕГЭ по химии
('3', '11', '2024-01-16'), -- Смирнова О.В. ведет органическую химию
('3', '12', '2024-01-17'), -- Смирнова О.В. ведет неорганическую химию
('4', '13', '2024-01-17'), -- Кузнецова М.С. ведет подготовку к ОГЭ по русскому языку
('4', '14', '2024-01-18'), -- Кузнецова М.С. ведет подготовку к ЕГЭ по русскому языку
('4', '15', '2024-01-18'), -- Кузнецова М.С. ведет общую подготовку по русскому языку
('5', '17', '2024-01-18'), -- Сидоров А.П. ведет подготовку к ОГЭ по истории
('5', '18', '2024-01-19'), -- Сидоров А.П. ведет подготовку к ЕГЭ по истории
('5', '19', '2024-01-20'), -- Сидоров А.П. ведет курс по истории России
('6', '21', '2024-01-20'), -- Фёдорова Н.Г. ведет подготовку к ОГЭ по английскому языку
('6', '22', '2024-01-20'), -- Фёдорова Н.Г. ведет подготовку к ЕГЭ по английскому языку
('6', '23', '2024-01-21'), -- Фёдорова Н.Г. ведет общую подготовку по английскому языку
('6', '24', '2024-01-21'), -- Фёдорова Н.Г. ведет разговорный английский
('7', '25', '2024-01-21'), -- Михайлова Л.В. ведет подготовку к ОГЭ по обществознанию
('7', '26', '2024-01-22'), -- Михайлова Л.В. ведет подготовку к ЕГЭ по обществознанию
('7', '27', '2024-01-23'), -- Михайлова Л.В. ведет курс по социологии
('8', '29', '2024-01-23'), -- Николаев С.В. ведет курс по основам экономики
('8', '30', '2024-01-24'), -- Николаев С.В. ведет курс по микроэкономике
('8', '28', '2024-01-25'), -- Николаев С.В. ведет курс по подготовке к ЕГЭ по экономике
('9', '19', '2024-01-26'), -- Петрова Е.И. ведет курс по истории России
('9', '18', '2024-01-26'), -- Петрова Е.И. ведет подготовку к ЕГЭ по истории
('10', '1', '2024-01-27'), -- Васильев В.А. ведет подготовку к ОГЭ по математике
('10', '3', '2024-01-28'); -- Васильев В.А. ведет общую подготовку по математике

INSERT INTO time (time_hour) VALUES
("08:00:00"),
("10:00:00"),
("12:00:00"),
("14:00:00"),
("16:00:00");

INSERT INTO registration (schedule_id, registration_time)
SELECT schedule.schedule_id, time.time_hour
FROM schedule
CROSS JOIN time;
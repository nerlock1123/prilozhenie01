# импорт объекта для создания приложения
from flask import Flask, session

# создание экземпляра объекта приложения
app = Flask(__name__)

# установим секретный ключ для подписи.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# импорт всех контроллеров
import controllers.index
import controllers.new_student
import controllers.new_registration
import controllers.schedule
import controllers.statistics
import controllers.teacher, controllers.new_teacher




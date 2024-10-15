from app import app
from flask import render_template

@app.route('/statistics')
def statistics():
    # Простая заглушка для страницы статистики
    return render_template('statistics.html')

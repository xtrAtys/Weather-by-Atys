from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Путь к файлу, где будут храниться сообщения
DATA_FILE = 'messages.txt'

# Функция для сохранения сообщения в файл
def save_message(message):
    with open(DATA_FILE, 'a') as f:
        f.write(message + '\n')

# Функция для чтения всех сообщений из файла
def read_messages():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return f.readlines()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        if message:
            save_message(message)
            return redirect(url_for('index'))

    messages = read_messages()
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)

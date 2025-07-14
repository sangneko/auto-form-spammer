from flask import Flask, render_template, request
from spammer import spam_form
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_spam():
    form_url = request.form['form_url']
    yes_percent = int(request.form['yes_percent'])
    times = int(request.form['times'])

    threading.Thread(target=spam_form, args=(form_url, yes_percent, times)).start()
    return "Đã bắt đầu gửi biểu mẫu!"

if __name__ == '__main__':
    app.run(debug=True)

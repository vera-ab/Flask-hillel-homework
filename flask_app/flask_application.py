from flask import Flask, request
import time
import random
import string

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello world!'


@app.route('/whoami/')
def data():
    ip_address = request.remote_addr
    browser = request.user_agent.browser
    current_time = time.strftime('%H:%M:%S')
    return f'<h2> IP address is: {ip_address} <br> Browser is: {browser} <br> Current time is: {current_time} </h2>'


@app.route('/source_code/')
def code():
    with open('flask_app1.py') as file:
        text = file.read()
        return f'<pre>{text}</pre>'


@app.route('/random/')
def string_res():
    try:
        length: int = int(request.values.get('length', 0))
    except Exception:
        length = 0
    try:
        specials: int = int(request.values.get('specials', 0))
    except Exception:
        specials = 0
    try:
        digits: int = int(request.values.get('digits', 0))
    except Exception:
        digits = 0
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    spec = '!"№;%:?*()_+'
    digits_list = '0123456789'
    if specials == 1:
        alphabet += spec
    if digits == 1:
        alphabet += digits_list
    res = []
    if length is not None and range(1, 100):
        for i in range(length):
            res.append(random.choice(alphabet))

    result_string = ''.join(res)
    return f'{result_string}'


app.run(debug=True)

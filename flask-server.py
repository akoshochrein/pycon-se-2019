import random
import time
from flask import Flask


app = Flask(__name__)


@app.route('/nighty')
def hello():
    to_sleep = 5#random.randint(1, 5)
    time.sleep(to_sleep)
    return f'slept {to_sleep} seconds'

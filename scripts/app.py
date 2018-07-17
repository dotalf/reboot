# encoding:utf-8

from flask import Flask
from log_analyse import loganalyse

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello reboot'


@app.route('/index')
def test():
    return 'hello reboot'


@app.route('/log/')
def log_analyze():
    logfile = 'ngnix.log'
    return loganalyse(logfile=logfile)
    # return 'this is test'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)

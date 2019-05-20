
from flask import Flask
from loganalysis import logaly
from flask import render_template

# import log

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello'

@app.route('/logs/')
def logs():
	logfile = 'access.1w.log'
	rt_list =  logaly.loganalysis(logfile=logfile)
	print(rt_list)
	return render_template('logs.html',rt_list=rt_list,title = 'topn')


if __name__=='__main__':
	app.run(host='0.0.0.0',port=8001,debug=True)

import sys
from flask import Flask, render_template

app = Flask(__name__)
#app.config.from_object(__name__)

@app.route('/')
def home_page():
	return render_template("index.html")

@app.route('/curriculum')
def curriculum():
	return render_template("curriculum.html")    

if __name__ == '__main__':
	app.run(host='0.0.0.0')

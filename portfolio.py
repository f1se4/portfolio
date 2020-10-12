import sys
from flask import Flask, render_template
from flask_misaka import Misaka


app = Flask(__name__)
Misaka(app)

@app.route('/')
def home_page():
	return render_template("index.html")

@app.route('/curriculum')
def curriculum():
	file_path = url_for('static',filename='images/project3.jpg')
	with open("./md/curriculum.md", "r") as file:
		content = file.read()	
	return render_template("curriculum.html", text=content)    

if __name__ == '__main__':
	app.run(host='0.0.0.0')

import sys
from flask import Flask, render_template
from flask_misaka import markdown


app = Flask(__name__)
#Misaka(app, math_explicit=True)

@app.route('/')
def home_page():
	return render_template("index.html")

@app.route('/curriculum')
def curriculum():
	with open("./md/curriculum.md", "r") as file:
		content = file.read()	
	return render_template("curriculum.html", text=markdown(content,math_explicit=True))

@app.route('/gompertz')
def gompertz():
	with open("./md/gompertz.md", "r") as file:
		content = file.read()	
	return render_template("gompertz.html", text=markdown(content,math_explicit=True))  	

if __name__ == '__main__':
	app.run(host='0.0.0.0')

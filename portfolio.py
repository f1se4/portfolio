import sys
from flask import Flask, render_template, render_template_string
import markdown
from flask_misaka import Misaka

md = markdown.Markdown(extensions=['mdx_math'])

app = Flask(__name__)
Misaka(app)

@app.route('/')
def home_page():
	return render_template("index.html")

@app.route('/curriculum')
def curriculum():
	with open("./md/curriculum.md", "r") as file:
		content = file.read()
	return render_template("curriculum.html", text=content)

@app.route('/gompertz')
def gompertz():
	with open("./md/gompertz.md", "r") as file:
		content = file.read()
	return render_template("gompertz.html", text=md.convert(content))

if __name__ == '__main__':
	app.run(host='0.0.0.0')

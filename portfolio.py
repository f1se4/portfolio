import sys
from flask import Flask, render_template, render_template_string
import markdown
from flask_misaka import Misaka

md = markdown.Markdown(extensions=['mdx_math','fenced_code','tables'])

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
	with open("./md/gompertz/gompertz.md", "r") as file:
		notebook = file.read()
	with open("./md/gompertz/summary.md", "r") as file:
		summary = file.read()
	return render_template("gompertz.html", notebook=md.convert(notebook), summary=md.convert(summary))

@app.route('/covidmollet')
def covidmollet():
	with open("./md/covidmollet/covidmollet.md", "r") as file:
		notebook = file.read()
	with open("./md/gompertz/summary.md", "r") as file:
		summary = file.read()
	return render_template("covidmollet.html", notebook=md.convert(notebook), summary=md.convert(summary))

if __name__ == '__main__':
	app.run(host='0.0.0.0')

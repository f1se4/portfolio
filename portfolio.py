from flask import Flask, render_template, request, session, escape,\
                    redirect, url_for, flash, g, send_from_directory, abort,\
					render_template_string
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import os
import sys
import urllib.parse, hashlib

import markdown
from flask_misaka import Misaka

md = markdown.Markdown(extensions=['mdx_math','fenced_code','tables','sane_lists'])
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpge", "gif", "pdf"])

app = Flask(__name__)
Misaka(app)

@app.route('/')
def home_page():
	return render_template("index.html")

@app.route('/airbnb')
def airbnb():
	with open("./md/airbnb/part1.md", "r") as file:
		part1 = file.read()
	with open("./md/airbnb/part2.md", "r") as file:
		part2 = file.read()	
	with open("./md/airbnb/part3.md", "r") as file:
		part3 = file.read()
	with open("./md/airbnb/part4.md", "r") as file:
		part4 = file.read()					
	return render_template("airbnb.html", 
							part1=md.convert(part1),
							part2=md.convert(part2),
							part3=md.convert(part3),
							part4=md.convert(part4)
							)

@app.route('/mapairbnb')
def mapairbnb():
	return render_template("mapairbnb.html")

@app.route('/gompertz')
def gompertz():
	with open("./md/gompertz/gompertz.md", "r") as file:
		notebook = file.read()
	with open("./md/gompertz/summary.md", "r") as file:
		summary = file.read()
	return render_template("gompertz.html", notebook=md.convert(notebook), summary=md.convert(summary))

@app.route('/molletweather')
def molletweather():
	with open("./md/molletweather/MolletWeather.md", "r") as file:
		notebook = file.read()
	with open("./md/molletweather/summary.md", "r") as file:
		summary = file.read()
	return render_template("gompertz.html", notebook=md.convert(notebook), summary=md.convert(summary))

@app.route('/covidmollet')
def covidmollet():
	with open("./md/covidmollet/covidmollet.md", "r") as file:
		notebook = file.read()
	with open("./md/covidmollet/summary.md", "r") as file:
		summary = file.read()
	return render_template("covidmollet.html", notebook=md.convert(notebook), summary=md.convert(summary))

@app.route('/dashboard')
def dashboard():
	with open("./md/dashboard/dashboard.md", "r") as file:
		notebook = file.read()
	with open("./md/dashboard/summary.md", "r") as file:
		summary = file.read()
	return render_template("dashboard.html", notebook=md.convert(notebook), summary=md.convert(summary))

@app.route('/isaac')
def isaac():
	with open("./md/isaacgonzalez/isaac.md", "r") as file:
		notebook = file.read()
	with open("./md/isaacgonzalez/summary.md", "r") as file:
		summary = file.read()
	return render_template("isaac.html", notebook=md.convert(notebook), summary=md.convert(summary))		

if __name__ == '__main__':
	app.run(host='0.0.0.0')

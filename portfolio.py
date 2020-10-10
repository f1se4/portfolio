from flask import Flask

app = Flask(__name__)

def holamundo():
	return 'Hola Mundo!'

@app.route('/')
def holamundo():
	return 'Hola Sergi!'

if __name__ == '__main__':
	app.run(host='0.0.0.0')

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')

@app.route('/github')
def github():
	user = 'JaviCeRodriguez'
	response = requests.get(f'https://api.github.com/users/{user}').json()
	return render_template('github.html', response=response)

if __name__ == '__main__':
  app.run()

# Ejecutar estos comandos:
# > set FLASK_APP=main.py
# > set FLASK_ENV=DEVELOPMENT
# > set FLASK_DEBUG=1
# > flask run
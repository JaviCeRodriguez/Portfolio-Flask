from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
  print('Estoy en Home')
  return render_template('home.html')

@app.route('/projects')
def projects():
  print('Estoy en Projects')
  return render_template('projects.html')

@app.route('/github')
def github():
  print('Estoy en Github')
  return render_template('github.html')

if __name__ == '__main__':
  app.run()

from flask import Flask, render_template, request, url_for, redirect
from apiRequest import API
import inputUser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = inputUser.CommentForm(request.form)
    if request.method == 'POST':
        username = form.username.data
        print(f'Searching user: {username}')
        return redirect(url_for('user', name = username))
    return render_template('base/base.html', form = form)

@app.route('/user/<name>')
def user(name):
    form = inputUser.CommentForm(request.form)
    response = API.requestGet(name)
    codeHTTP = response.status_code
    if codeHTTP != 200:
        print(f'User not found, GET {codeHTTP}')
        return redirect(url_for('error'))
    else:
        print(f'User {name} found!')
        userData = API.jsonPrint(response.json())
        return render_template('profile.html', form = form, userData = userData)

@app.route('/error')
def error():
    form = inputUser.CommentForm(request.form)
    return render_template('notfound.html', form = form)

if __name__ == '__main__':
  app.run()
 
from wtforms import Form, StringField

class CommentForm(Form):
    username = StringField('Username: ')
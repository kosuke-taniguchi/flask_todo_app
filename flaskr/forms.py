from wtforms import StringField, TextAreaField, SubmitField, PasswordField, DateField
from wtforms import Form
from wtforms.validators import DataRequired, Email, EqualTo


class LoginFrom(Form):
    email = StringField('Eメール: ', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード: ', validators=[DataRequired()])
    submit = SubmitField('ログイン')


class RegisterForm(Form):
    username = StringField('ユーザ名: ', validators=[DataRequired()])
    email = StringField('Eメール: ', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード: ', validators=[DataRequired(), EqualTo('confirm_password', message='パスワードが一致しません')])
    confirm_password = PasswordField('パスワードの確認: ', validators=[DataRequired()])
    submit = SubmitField('登録')


class PostForm(Form):
    title = StringField('タイトル: ', validators=[DataRequired()])
    content = TextAreaField('やること: ', validators=[DataRequired()])
    due_date = DateField('期日: ', validators=[DataRequired()])
    submit = SubmitField('投稿: ')


class UpdateForm(Form):
    title = StringField('タイトル: ', validators=[DataRequired()])
    content = TextAreaField('やること: ', validators=[DataRequired()])
    due_date = DateField('期日: ', validators=[DataRequired()])
    submit = SubmitField('投稿: ')
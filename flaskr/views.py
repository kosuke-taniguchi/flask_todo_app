from flask import render_template, redirect, url_for, request, flash
from flask import Blueprint
from flaskr.forms import PostForm, LoginFrom, RegisterForm, UpdateForm
from flaskr.models import Post, User
from flaskr import db
from flask_login import login_user, logout_user, login_required, current_user


bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/todohome')
@login_required
def todohome():
    posts = Post.query.all()
    username = current_user.username
    return render_template('todohome.html', posts=posts, username=username)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom(request.form)
    email = form.email.data
    password = form.password.data
    if request.method == 'POST' and form.validate():
        user = User.select_user_by_email(email)
        if user and user.validate_password(password):
            login_user(user)
            next = request.args.get('next')
            if not next:
                next = url_for('app.todohome')
            return redirect(next)
        elif not user:
            flash('このユーザは存在しません')
        elif not user.validate_password(password):
            flash('パスワードが正しくありません')
    return render_template('login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app.home'))

@bp.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(
            email,
            username,
            password
        )
        user.add_user()
        return redirect(url_for('app.login'))
    return render_template('register.html', form=form)


@bp.route('/post', methods=['POST', 'GET'])
@login_required
def post():
    form = PostForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        due_date = form.due_date.data
        posts = Post(
            title,
            content,
            due_date
        )
        posts.add_post()
        return redirect(url_for('app.todohome'))
    return render_template('post.html', form=form)

@bp.route('/delete/<int:post_id>')
@login_required
def delete(post_id):
    post = Post.query.get(post_id)
    post.delete_post()
    return redirect(url_for('app.todohome'))

@bp.route('/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def update(post_id):
    form = UpdateForm(request.form)
    post = Post.query.get(post_id)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        post.update_post(title, content)
        return redirect(url_for('app.todohome'))
    return render_template('update.html', form=form, post=post)
from flaskr import db
from flask_bcrypt import generate_password_hash, check_password_hash
from flaskr import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):

    __tabelname__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(64))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def add_user(self):
        with db.session.begin(subtransactions=True):
            db.session.add(self)
        db.session.commit()
 

    @classmethod
    def select_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


class Post(db.Model):

    __tabelname__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    content = db.Column(db.Text)
    due_date = db.Column(db.Integer)
    # posts_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, content, due_date):
        self.title = title
        self.content = content
        self.due_date = due_date

    def add_post(self):
        with db.session.begin(subtransactions=True):
            db.session.add(self)
        db.session.commit()

    def delete_post(self):
        with db.session.begin(subtransactions=True):
            db.session.delete(self)
        db.session.commit()

    def update_post(self, title, content):
        with db.session.begin(subtransactions=True):
            self.title = title
            self.content = content
            db.session.add(self)
        db.session.commit()
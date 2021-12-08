from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from flask_bcrypt import Bcrypt
from forms import LoginForm



application = Flask(__name__)
application.config['SECRET_KEY'] = 'some_secret_key'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)


class User(db.Model):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


db.create_all()

login_manager = LoginManager()
login_manager.init_app(application)
bcrypt = Bcrypt()

@login_manager.user_loader
def user_loader(user_id):
    """
    Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)

@application.route("/login", methods=["GET", "POST"])
def login():
    """
    For GET requests, display the login form. 
    For POSTS, login the current user by processing the form.
    """
    if current_user.is_authenticated:
        return render_template('landing_page.html', title='Landing Page', tabtitle='Landing Page')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("index"))
    return render_template("login.html", form=form, tabtitle='Login',title='Login')

@application.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("logout.html", tabtitle='Logout')


@application.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('landing_page.html', title='Landing Page', tabtitle='Landing Page')
    else:
        return redirect(url_for("login"))


if __name__ == '__main__':
    application.run(debug=True)

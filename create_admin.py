from getpass import getpass
import sys

from flask import current_app
from application import application
from flask_bcrypt import Bcrypt
from application import User, db

def main():
    """Main entry point for script."""
    with application.app_context():
        db.metadata.create_all(db.engine)
        if User.query.all():
            print('A user already exists! Create another? (y/n):')
            create = input()
            if create == 'n':
                return

        print('Enter email address: ')
        email = input()
        password = getpass()
        assert password == getpass('Password (again):')

        user = User(
            email=email, 
            password=bcrypt.generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        print('User added.')

bcrypt = Bcrypt()

if __name__ == '__main__':
    sys.exit(main())
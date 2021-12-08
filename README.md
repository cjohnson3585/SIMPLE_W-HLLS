# SIMPLE_W-HLLS
Simple flask web app template with three tabs (Home-Login-Logout) and security using Flask-Login, sessioning, and Cookies.

**The test email and password are _'mywebsite'_ and _'mywebsite'_.**

To run the app, you can either start a virtual environment or just run locally on your command line.

Running locally from the command line, run:
```
  pip3 install -r requirements.txt
```
to install all the dependencies.

Then run:
```
  python3 application.py
```

Navigate to http://127.0.0.1:5000/ to see the app running.


To run from a virtual environment (I used _virtualenv_) run:
```
  virtualenv myenv
  source myenv/bin/activate
  pip3 install -r requirements.txt
  python3 application.py
```

Then navigate to http://127.0.0.1:5000/ to see the app running.

To create a new user run:
```
  python3 create_admin.py
```
and type a new email address and password (twice) then the user is created in the database 'db.sqlite'.

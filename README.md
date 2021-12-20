# SIMPLE_W-HLLS
Simple flask web app template with three tabs (Home-Login-Logout) and security using Flask-Login, sessioning, and Cookies.

**The test email and password are _'mywebsite'_ and _'mywebsite'_.**



<img width="1151" alt="Screen Shot 2021-12-20 at 9 43 34 AM" src="https://user-images.githubusercontent.com/43188404/146785513-bbaab7e0-9116-4e53-b1d5-b3916a5e4c7f.png">


<img width="1301" alt="Screen Shot 2021-12-20 at 9 43 52 AM" src="https://user-images.githubusercontent.com/43188404/146785530-f17aa560-bf4a-4a16-99d8-24c6a6039cea.png">


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

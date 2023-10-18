# TeleWork
A web application that will help users find remote jobs and provide interview prep.

# Note that 
you must have  installed the required Python packages (e.g., Flask, Flask-WTF, Flask-Login, and Flask-Bootstrap) using pip

pip install Flask 

pip install flask-bootstrap

# run the app 
python app.py

# 'pytz' module
pip3 install pytz

# for database on Mongodb
pip install Flask-PyMongo

# Login/Registarion
pip install Flask-Login

Install or upgrade using pip.

pip install -U Flask-WTF

git clone https://github.com/wtforms/flask-wtf
pip install -e ./flask-wtf
Or install the latest build from an archive.

pip install -U https://github.com/wtforms/flask-wtf/archive/main.tar.gz

# OS
Python has a built-in os module with methods for interacting with the operating system, like creating files and directories, management of files and directories, input, output, environment variables, process management, etc.

# csrf = CSRFProtect(app)
Flask-WTF CSRF Protection: In this code, CSRFProtect is part of the Flask-WTF extension, which provides forms handling in Flask applications. One of the features of Flask-WTF is built-in CSRF protection. When you initialize CSRFProtect with app, it sets up middleware to protect your Flask application against CSRF attacks.

# Error to fix
ImportError: cannot import name 'url_decode' from 'werkzeug.urls' (/workspace/.pyenv_mirror/user/current/lib/python3.12/site-packages/werkzeug/urls.py). Did you mean: 'urlencode'?
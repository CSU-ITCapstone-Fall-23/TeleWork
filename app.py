from flask import Flask, render_template   
from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from forms.forms import LoginForm, RegistrationForm
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)
csrf = CSRFProtect(app)

app.secret_key = 'your_secret_key_here'  # Change this to a secure key
# app.config['SESSION_TYPE'] = 'filesystem'  # Set the session type
app.config['SECRET_KEY'] = os.urandom(24)
bootstrap = Bootstrap(app)

# Configure login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Sample job listings (you can replace this with a database)
job_listings = [
    {
        'id': 1,
        'title': 'Software Developer',
        'description': 'Develop software applications.',
    },
    {
        'id': 2,
        'title': 'Data Analyst',
        'description': 'Analyze data and generate insights.',
    },
]

# Mock user database
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.username = "user"
        self.password = "password"

users = {"user": User(1)}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users.get(form.username.data)
        if user and form.password.data == user.password:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.username.data not in users:
            user = User(form.username.data)
            user.password = form.password.data
            users[user.username] = user
            return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/job/<int:job_id>')
def job_details(job_id):
    job = next((job for job in job_listings if job['id'] == job_id), None)
    if job:
        return render_template('job_details.html', job=job)
    else:
        return 'Job not found', 404

@app.route('/apply/<int:job_id>', methods=['POST'])
def apply_for_job(job_id):
    if request.method == 'POST':
        # In a real application, you would handle the job application logic here
        flash('Application submitted successfully', 'success')
        return redirect(url_for('job_details', job_id=job_id))

@app.route('/job_search')
def job_search():
    return render_template('job_search.html', job_listings=job_listings)

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name)    

if __name__ == "__main__":        # when running python app.py
    #app.run()                     # run the flask app
    #change app.run() to the following
    app.run(debug=True)
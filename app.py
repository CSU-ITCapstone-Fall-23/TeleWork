from flask import Flask, render_template   
from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure key
app.config['SESSION_TYPE'] = 'filesystem'  # Set the session type
bootstrap = Bootstrap(app)

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

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/job_postings')
# def job_postings():
#     # You can fetch job postings from a database here
#     job_postings_data = [
#         {'Doctor': 'Job 1', 'description': 'Description 1'},
#         {'Teacher': 'Job 2', 'description': 'Description 2'},
#     ]
#     return render_template('job_postings.html', job_postings=job_postings_data)

# @app.route('/job/<int:job_id>')
# def job_details(job_id):
#     # Fetch job details based on job_id from database
#     job_details_data = {'Doctor': 'Job 1', 'description': 'Description 1'}
#     return render_template('job_details.html', job=job_details_data)   

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

# @app.route('/post_job', methods=['GET', 'POST'])
# def post_job():
#     if request.method == 'POST':
#         title = request.form['title']
#         description = request.form['description']
#         # In the real application, you would save the job posting to a database.
#         # we added it to the dummy data.
#         job_id = len(job_postings) + 1
#         job_postings.append({"id": job_id, "title": title, "description": description})
#         return redirect(url_for('index'))
#     return render_template('post_job.html')

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name)    

if __name__ == "__main__":        # when running python app.py
    #app.run()                     # run the flask app
    #change app.run() to the following
    app.run(debug=True)
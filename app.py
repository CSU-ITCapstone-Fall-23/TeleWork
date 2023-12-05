
from flask import Flask, render_template   
from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
#from flask_pymongo import PyMongo
#from flask import jsonify

# Create the Flask app
app = Flask(__name__)
# Configure MongoDB
# app.config['MONGO_URI'] = 'mongodb+srv://<TeleWork>:<CapStone2023>@cluster1.bryy6up.mongodb.net/'
# mongo = PyMongo(app)
bootstrap = Bootstrap(app)

#code for accessing the indeed jobs database
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
url = "mongodb+srv://TeleWork:CapStone2023@cluster1.bryy6up.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    db = client.IndeedJobs
    indeed = db["IndeedJobs"]
    for job in indeed.find():
        print(job)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#code for accessing RemoteCo database
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
url = "mongodb+srv://TeleWork:CapStone2023@cluster1.bryy6up.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    db = client.RemoteCo
    indeed = db["RemoteCo"]
    for job in indeed.find():
        print(job)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)  

#code for accessing data from the interviewprep database, mixture of questions and answers, and dress code advice
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
url = "mongodb+srv://TeleWork:CapStone2023@cluster1.bryy6up.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    db = client.InterviewPrep
    indeed = db["InterviewPrep"]
    for job in indeed.find():
        print(job)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e) 
    
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

@app.route('/job/<int:job_id>')
def job_details(job_id):
    job = next((job for job in job_listings if job['id'] == job_id), None)
    if job:
        return render_template('job_details.html', job=job)
    else:
        return 'Job not found', 404
# @app.route('/job/<int:job_id>')
# def job_details(job_id):
#     job = mongo.db.IndeedJobs.DBJobs.find_one({'_id': ObjectId(job_id)}) 
#     if job:
#         return render_template('job_details.html', job=job)
#     else:
#         return 'Job not found', 404


@app.route('/apply/<int:job_id>', methods=['POST'])
def apply_for_job(job_id):
    if request.method == 'POST':
        # In a real application, you would handle the job application logic here
        flash('Application submitted successfully', 'success')
        return redirect(url_for('job_details', job_id=job_id))

@app.route('/job_search')
def job_search():
    #job_listings = mongo.db.IndeedJobs.DBJobs.find()
    return render_template('job_search.html', job_listings=job_listings)

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name)    

@app.route("/interviewprep")
def interview():
    return render_template("interviewprep.html")    

@app.route("/contact")
def contactus():
    return render_template("contact.html")    

@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    # Handle form submission here
    # You can process the form data and save it to a database if needed
    # For now, let's just redirect to the thank you page

    return redirect(url_for('thank_you'))

@app.route("/thankyou")
def thank_you():
    return render_template("thankyou.html")


if __name__ == "__main__": 
    app.run(debug=True)
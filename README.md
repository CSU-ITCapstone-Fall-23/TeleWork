# TeleWork
A web application that will help users find remote jobs and provide interview prep.

# Note that 
you must have  installed the required Python packages (e.g., Flask Flask-Login, and Flask-Bootstrap) using pip

pip install Flask 

pip install flask-bootstrap

pip install --upgrade pip

# for database on Mongodb
pip install Flask-PyMongo

# run the app 
python app.py

# for render
pip install Flask Flask-PyMongo Flask-Bootstrap

  # from mongodb
    mongodb://localhost:27017
    mongodb+srv://TeleWork:*****@cluster1.bryy6up.mongodb.net/
    user:TeleWork
    Password: CapStone2023
  
  # To connect and check database
  # MongoDB configuration
mongodb_url = "mongodb+srv://TeleWork:CapStone2023@cluster1.bryy6up.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb_url, server_api=ServerApi('1'))

# Check MongoDB connection
def check_mongodb_connection(database_name):
    try:
        client.admin.command('ping')
        db = client[database_name]
        collection = db[database_name]
        for job in collection.find():
            print(job)
        print(f"Pinged your deployment. You successfully connected to MongoDB - {database_name}!")
    except Exception as e:
        print(e)

# Check connections for different databases
check_mongodb_connection("IndeedJobs")
check_mongodb_connection("RemoteCo")
check_mongodb_connection("InterviewPrep")



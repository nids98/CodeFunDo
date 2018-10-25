from flask import Flask, render_template, request, json, url_for, session, redirect, flash
from flaskext.mysql import MySQL
# from appC.tasks import test 
# from appC.tasks.tweet import database

app = Flask(__name__)
mysql = MySQL()

app.config['SECRET_KEY'] = 'mykey'

# MySQL setup
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'nidhi'
app.config['MYSQL_DATABASE_DB'] = 'codefundo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# Configs
# REDIS_HOST = "0.0.0.0"
# REDIS_PORT = 6379
# BROKER_URL = environ.get('REDIS_URL', "redis://{host}:{port}/0".format(
    # host=REDIS_HOST, port=str(REDIS_PORT)))
# CELERY_RESULT_BACKEND = BROKER_URL

# def make_celery(app):
    # create context tasks in celery
    # celery = Celery(
        # app.import_name,
        # broker=BROKER_URL
    # )
    # TaskBase = celery.Task

    # class ContextTask(TaskBase):
        # abstract = True

        # def __call__(self, *args, **kwargs):
            # with app.app_context():
                # return TaskBase.__call__(self, *args, **kwargs)

    # celery.Task = ContextTask

    # return celery

# celery = make_celery(app)


# Connection to the database
# conn = mysql.connect()
# cursor = conn.cursor()

#Check login status
loggedin=0
registered=0
city='Udupi'

#database.init(app)

@app.route('/')
def index():
    with open('tweets.txt', 'r') as f:
        alltext = f.read()
        tweet_list = alltext.split(',,,')
    with open('retweetcount.txt', 'r') as f:
        alltext = f.read()
        retweet_count = alltext.split(',,,')
        return render_template('index.html', city = city, registered=registered, tweet_list=zip(tweet_list,retweet_count))


@app.route("/login",  methods=['POST'])
def login():
	conn = mysql.connect()
	cursor = conn.cursor()
	print("INSIDE LOGIN")
	email = request.form["lemail"]
	print(email)
	password = request.form["lpass"]
	print(password)	
	cursor.execute("SELECT * from volunteers where email='"+email+"' and password='"+password+"'")
	data = cursor.fetchone()
	cursor.close()
	conn.close()
	print(data[0])
	if data is None:
		return render_template('index.html')
	else:
		loggedin = 1
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("SELECT * from victims where status ='missing' and city='"+city+"'")
		missing = cursor.fetchall()
		print(list(missing))
		cursor.execute("SELECT * from victims where status ='safe' and city='"+city+"'")
		safe = cursor.fetchall()
		print(list(safe))
		cursor.execute("SELECT * from victims where status ='dead' and city='"+city+"'")
		dead = cursor.fetchall()
		print(list(dead))
		return render_template('dashboard.html', email=email, loggedin=loggedin, missing=missing, dead=dead, safe=safe)
		# return "Logged in successfully"

@app.route('/signup', methods=['POST'])
def signup():
	print('Entered /signup in main.py')
	try:
		print('inside try')
		conn = mysql.connect()
		cursor = conn.cursor()
		# Fetching the data from form
		name = request.form["sname"]
		print(name)
		email = request.form["semail"]
		print(email)
		region = request.form["sregion"]
		print(region)
		password = request.form["spass"]
		print(password)
		contact = request.form["scontact"]
		print(contact)
		#checking if all fields are entered
		if name and password and contact and email:
			print('reached')
			#Execute query - inserting into database
			cursor.execute("INSERT INTO volunteers(name, email, region, password, contact) VALUES(%s, %s, %s, %s, %s)",(name, email, region, password, contact))
			data = cursor.fetchall()
			# Checking if query was successful
			if len(data) is 0:
				# On success
				conn.commit()
				registered=1
				# flash('You have successfully registered. Now login to continue!')
				# return redirect("url_for('index')")
				return "You have successfully signed up"
				# return render_template('index.html')
			else:
				# On Failure
				print(json.dumps({ 'error' : str(data[0]) }))
				return str(data[0])
		else:
			return "Enter the required fields"
	except Exception as e:
		print(str(e))
		return "Please fill all fields"
	finally:
		cursor.close()
		conn.close()

@app.route('/dashboard')
def dashboard():
	print("inside Dashboard")
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT * from victims where status ='missing'")
	missing = cursor.fetchall()
	print(missing)
	cursor.execute("SELECT * from victims where status ='safe'")
	safe = cursor.fetchall()
	print(safe)
	cursor.execute("SELECT * from victims where status ='dead'")
	dead = cursor.fetchall()
	print(dead)
	return render_template('dashboard.html', missing=missing, dead=dead, safe=safe)

@app.route('/logout')
def logout():
	return render_template('index.html', city=city)

if __name__ == "__main__":
	app.run(debug=True)

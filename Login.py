from flask import Flask,render_template,request,redirect, jsonify
import json
app = Flask(__name__)
import pymongo

#Connect with database
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['local']
mycol = mydb['logined']

#calling Html file
@app.route('/')
def loginPage():
	return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():

	error=None
	#collecting input data
	rec = request.form	
	json_msg = {
			'email' : rec['email'],
			'password' : rec['password']
		}
	#finding the input data if it is already exist
	x=mycol.find(json_msg)
	print(x)
	#if it doesnt exist show the following data and message
	if x is None:
		status =200
		message= 'incorrect credential'
		login_state = False

		data = {
			'status' :status,
			'message':message,
			'login_state':login_state

		}

		return jsonify(data)
	#if it doesnt exist return the following data and message	
	else:
		status = 200
		message = 'Login Successful!'
		login_state = True

		data = {
			'status':status,
			'message':message,
			'login_state':login_state
		}
		return jsonify(data)
		
#function to sign up 
@app.route('/register',methods = ['POST'])
def register():

	rec = request.form

	json_msg = {
		'email' : rec['email'],
		'password' : rec['password']
	}
	print(json_msg)
#stores the input data into db_result
	db_result= mycol.find_one(json_msg)

	if db_result is None:
	#if the the input data is not in the database then insert	
		mycol.insert_one(json_msg)
		return 'Successful'
	else:
		return 'User already exist'	


						
if __name__ == '__main__':
	app.run(debug = True)
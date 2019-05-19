from flask import Flask,render_template,flash,request,redirect, jsonify
import json
app = Flask(__name__)
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['local']

mycol = mydb['logined']

@app.route('/')
def Login_Page():
	return render_template('index.html')


@app.route('/login', methods = ['POST'])
def Login():
	error=None
	if request.method == 'POST':
		
		rec = request.form
		###########
		# received_msg = request.data
		# decoded = received_msg.decode('utf8').replace("'",'"')
		# json_msg = json.loads(decoded)
		# print(json_msg)
		json_msg = {
			'email' : rec['email'],
			'password' : rec['password']
		}
		x = mycol.find_one(json_msg)
		print(x)

		if x is None:
			status = 200
			message = 'Incorrect credential!'
			login_state = False

			data = {
				'status':status,
				'message':message,
				'login_state':login_state
			}

			return jsonify(data)
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

		
@app.route('/registers', methods = ['POST'])
def register():

	rec = request.form
	json_msg = {
			'email' : rec['email'],
			'password' : rec['password']
		}
	print(json_msg)

	x = mycol.find_one(json_msg)

	if x is None:	
		mycol.insert_one(json_msg)
		return 'Successful'
	else:
		return 'User already exist'	


			
if __name__=='__main__':
	app.run(debug = True)
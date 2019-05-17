from flask import Flask,render_template,flash,request,redirect, jsonify
import json
app = Flask(__name__)


@app.route('/')
def Login_Page():
	return render_template('index.html')


@app.route('/login', methods = ['POST','GET'])
def Login():
	error=None
	if request.method == 'POST':
		print(request.data)

		###########
		received_msg = request.data
		decoded = received_msg.decode('utf8').replace("'",'"')
		json_msg = json.loads(decoded)
		print(json_msg)


		if json_msg['email']=='admin@admin' and \
			json_msg['password']=='admin':
			status = 200
			message = 'Login Successful!'
			login_state = True

			data = {
				'status':status,
				'message':message,
				'login_state':login_state
			}
			return jsonify(data)
		else:
			status = 200
			message = 'Incorrect credential!'
			login_state = False

			data = {
				'status':status,
				'message':message,
				'login_state':login_state
			}

			return jsonify(data)

			
if __name__=='__main__':
	app.run(debug = True)
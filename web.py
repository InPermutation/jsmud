import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import mudparse

app = Flask(__name__)
app.debug = True
app.secret_key = 'sdfghjklkufdcvbnmj'

@app.route("/")
def index():
	if not session.get('room'):
		session['room'] = "0_0"
	return render_template('index.html')

@app.route('/cmd')
def process_command():
	return mudparse.interpret(request.args.get('cmd', ''))

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)



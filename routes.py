from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os

#from flask_login import login_user, current_user, logout_user, login_required #Optional login imports, need to 'pip install flask_login'

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
  return render_template("home.html")

@app.route('/timesheets')
def timesheets():
  return render_template("timesheets.html", title="timesheets")

@app.route('/milestones')
def milestones():
  return render_template("milestones.html")


if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True)

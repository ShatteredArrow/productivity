from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os
from app.models import Timesheet, Milestone, Category
from app import app, db
from app import Config
from app.forms import AddMilestone

@app.route('/')
@app.route('/home')
def index():
  return render_template("home.html")

@app.route('/timesheets')
def timesheets():
  timesheets = Timesheet.query.all()
  return render_template("timesheets.html", title="timesheets", timesheets=timesheets)

@app.route('/milestones')
def milestones():
  addMilestoneForm = AddMilestone()
  milestones = Milestone.query.all()
  return render_template("milestones.html", milestones=milestones, addMilestoneForm=addMilestoneForm)


if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True)

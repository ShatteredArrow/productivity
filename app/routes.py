from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os
from app.models import Timesheet, Milestone, Category
from app import app, db
from app import Config
from app.forms import AddMilestoneForm, AddTimesheetForm

@app.route('/')
@app.route('/home')
def index():
  return render_template("home.html")

@app.route('/timesheets', methods=['GET', 'POST'])
def timesheets():
  addTimesheetForm = AddTimesheetForm()
  timesheets = Timesheet.query.all()
  if addTimesheetForm.validate_on_submit():
    timesheet = Timesheet()
    timesheet.milestone_id =0 
    timesheet.addTimesheet(addTimesheetForm.data)

    return redirect(url_for("timesheets"))
  return render_template("timesheets.html", title="timesheets", addTimesheetForm=addTimesheetForm, timesheets=timesheets)

@app.route('/milestones', methods=['GET', 'POST'])
def milestones():
  addMilestoneForm = AddMilestoneForm()
  milestones = Milestone.query.all()
  if addMilestoneForm.validate_on_submit():
    milestone = Milestone()
    milestone.addMilestone(addMilestoneForm.data)
    return redirect(url_for("milestones"))
  return render_template("milestones.html", milestones=milestones, addMilestoneForm=addMilestoneForm)


if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True)


#Attach a milestone to a timesheet
#many timesheets can be attached to one milestone

#Each event have many locations == Each milestone can have many timesheets
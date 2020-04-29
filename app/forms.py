
from flask_wtf import FlaskForm
from wtforms.fields.html5 import URLField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField,RadioField
from wtforms.validators import DataRequired, Regexp
from flask_wtf.file import FileRequired
from wtforms import SelectField, SelectMultipleField, FileField,DateTimeField
from app.models import Timesheet

class AddMilestone(FlaskForm):
    name = StringField('Milestone', validators=[DataRequired()])
    targetDate = DateTimeField('Target Date')
    startedDate = DateTimeField('Started Date')
    completedDate = DateTimeField('Completed Date')
    link = StringField('Link')
    note = TextAreaField('Notes')
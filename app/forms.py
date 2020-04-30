
from flask_wtf import FlaskForm
from wtforms.fields.html5 import URLField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField,RadioField
from wtforms.validators import DataRequired, Regexp
from flask_wtf.file import FileRequired
from wtforms import SelectField, SelectMultipleField, FileField,DateTimeField
from app.models import Timesheet,Milestone


#Import statements for autogenerating forms from models
from wtforms_alchemy import ModelForm,model_form_factory 
ModelForm = model_form_factory(FlaskForm)


class AddMilestoneForm(ModelForm):
    class Meta:
        model = Milestone

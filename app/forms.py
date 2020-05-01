
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from app.models import Timesheet,Milestone
#Import statements for autogenerating forms from models
from wtforms_alchemy import ModelForm,ModelFieldList, model_form_factory 
ModelForm = model_form_factory(FlaskForm)
from wtforms.fields import FormField


class AddMilestoneForm(ModelForm):
    class Meta:
        model = Milestone
    

class AddTimesheetForm(ModelForm):
    class Meta:
        model = Timesheet
    milestone = ModelFieldList(FormField(AddMilestoneForm))
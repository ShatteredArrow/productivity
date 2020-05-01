from app import db

milestoneCategories = db.Table("milestoneCategories",
    db.Column("milestoneId", db.Integer, db.ForeignKey("milestone.id"), primary_key=True),
    db.Column("categoryId", db.Integer, db.ForeignKey("category.id"), primary_key=True)
)

class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(254))
    targetDate = db.Column(db.Date)
    startedDate = db.Column(db.Date)
    completedDate = db.Column(db.Date)
    link  = db.Column(db.String(128))
    note = db.Column(db.String(254))
    timesheets = db.relationship("Timesheet", backref="milestones", lazy=True)
    
    categories = db.relationship('Category', secondary=milestoneCategories, lazy='subquery',
        backref=db.backref('milestones', lazy=True))

    def __repr__(self):
       return 'Milestone: {}'.format(self.id)

    def addMilestone(self, formDict):
        for key, value in formDict.items():
            try:
                setattr(self, key, value)
            except AttributeError:
                pass
        db.session.add(self)
        db.session.commit()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    
    def __repr__(self):
       return 'Category: {}'.format(self.id)

class Timesheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    timeSpent = db.Column(db.Integer)
    enjoyment = db.Column(db.Integer)
    notes = db.Column(db.String(254))
    milestone_id = db.Column(db.Integer, db.ForeignKey("milestone.id"))
    milestone = db.relationship("Milestone", backref='timesheetss')

    def addTimesheet(self, formDict):
        for key, value in formDict.items():
            try:
                setattr(self, key, value)
            except AttributeError:
                pass
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
       return 'Timesheet: {}'.format(self.id)
       
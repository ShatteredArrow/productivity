from app import db


milestoneCategories = db.Table("milestoneCategories",
    db.Column("milestoneId", db.Integer, db.ForeignKey("milestone.id"), primary_key=True),
    db.Column("categoryId", db.Integer, db.ForeignKey("category.id"), primary_key=True)
)

class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(254))
    targetDate = db.Column(db.DateTime)
    startedDate = db.Column(db.DateTime)
    completedDate = db.Column(db.DateTime)
    link  = db.Column(db.String(128))
    note = db.Column(db.String(254))
    timesheets = db.relationship("Timesheet", backref="milestone", lazy=True)
    categories = db.relationship('Category', secondary=milestoneCategories, lazy='subquery',
        backref=db.backref('milestones', lazy=True))

    def __repr__(self):
       return 'Milestone: {}'.format(self.id)



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    
    def __repr__(self):
       return 'Category: {}'.format(self.id)

class Timesheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    timeSpent = db.Column(db.Integer)
    enjoyment = db.Column(db.Integer)
    notes = db.Column(db.String(254))
    milestone_id = db.Column(db.Integer, db.ForeignKey("milestone.id"), nullable=False)

    def __repr__(self):
       return 'Timesheet: {}'.format(self.id)
       
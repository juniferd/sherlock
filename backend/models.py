from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.types import Enum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class CaseFile(db.Model):
    __tablename__ = 'casefile'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False, default='')
    date_updated = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    #  a case can have multiple leads 
    leads = db.relationship('Lead', backref='casefile', lazy=True)
    points = db.Column(db.Integer, nullable=True)
    status_solved = db.Column(db.Boolean, nullable=False, default=False)
    # a case can have multiple Clues
    clues = db.relationship('Clue', backref="casefile", lazy=True)

    def __repr__(self):
        return '<CaseFile %r>' % self.title

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Lead(db.Model):
    __tablename__ = 'lead'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # a lead has one case
    case_id = db.Column(db.Integer, db.ForeignKey('casefile.id'), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    lead_type = db.Column(db.Enum('Person', 'Place', 'Informant'), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Category %r>' % self.name

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

suspects = db.Table('suspects',
    db.Column('suspect_id', db.Integer, db.ForeignKey('suspect.id'), 
        primary_key=True),
    db.Column('clue_id', db.Integer, db.ForeignKey('clue.id'), 
        primary_key=True)    
)

class Clue(db.Model):
    __tablename__ = 'clue'
    id = db.Column(db.Integer, primary_key=True)
    # a clue has one case
    case_id = db.Column(db.Integer, db.ForeignKey('casefile.id'), nullable=False)
    title = db.Column(db.String(150), nullable=True)
    description = db.Column(db.Text, nullable=True)
    clue_type = db.Column(db.Enum(
        'Direct',
        'Hearsay',
        'Circumstantial',
        'Other'), nullable=False)
    clue_source = db.Column(db.String(50), nullable=False)
    # a clue can be used to build a timeline
    date_started = db.Column(db.DateTime, nullable=True)
    date_ended = db.Column(db.DateTime, nullable=True)
    suspects = db.relationship('Suspect', secondary=suspects, lazy='subquery',
        backref=db.backref('clues', lazy=True))

    def __repr__(self):
        return '<Clue %s>' % self.id

class Suspect(db.Model):
    __tablename__ = 'suspect'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

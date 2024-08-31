from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mentorconnect.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Mentee(db.Model):
    __tablename__ = 'Mentees'
    mentee_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    college_name = db.Column(db.String(255))
    gender = db.Column(db.String(50))
    current_address = db.Column(db.String(255))
    source = db.Column(db.String(255))

class Mentor(db.Model):
    __tablename__ = 'Mentors'
    mentor_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    dob = db.Column(db.Date)
    gender = db.Column(db.String(50))
    phone_number = db.Column(db.String(15))
    resume = db.Column(db.String(255))
    identification = db.Column(db.String(255))
    expectations = db.Column(db.Text)
    current_company = db.Column(db.String(255))
    designation_unit = db.Column(db.String(255))
    current_address = db.Column(db.String(255))
    source = db.Column(db.String(255))
    verified = db.Column(db.Boolean, default=False)
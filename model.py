
from email.policy import default
from app import db
from datetime import datetime

user_role = db.Table('user_role',
                     db.Column('user_id', db.Integer,
                               db.ForeignKey('users.id')),
                     db.Column('role_id', db.Integer,
                               db.ForeignKey('roles.id')))


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(40), nullable=False)
    assignment = db.relationship(
        'Role', secondary=user_role, backref="assignments")

    def __init__(self, name, surname, email, password, phone):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.phone = phone


# class Meeting(db.Model):
#     __tablename__ = "meetings"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(40), nullable=False)
#     start_date = db.Column(db.DateTime, nullable=False)
#     end_date = db.Column(db.DateTime, nullable=False)
#     patient_id = db.Column(
#         db.Integer, db.ForeignKey('users.id'), nullable=False)
#     patient = db.relationship(
#         'User', foreign_keys=[patient_id], lazy=True)
#     doctor_id = db.Column(
#         db.Integer, db.ForeignKey('users.id'), nullable=False)
#     doctor = db.relationship(
#         'User', foreign_keys=[doctor_id], lazy=True)


# class Comments(db.Model):
#     __tablename__ = "comments"
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String, nullable=False)
#     patient_id = db.Column(
#         db.Integer, db.ForeignKey('users.id'), nullable=False)
#     patient = db.relationship(
#         'User', foreign_keys=[patient_id], lazy=True)
#     doctor_id = db.Column(
#         db.Integer, db.ForeignKey('users.id'), nullable=False)
#     doctor = db.relationship(
#         'User', foreign_keys=[doctor_id], lazy=True)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow())


# class About(db.Model):
#     __tablename__ = "about"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(40), nullable=False)
#     text = db.Column(db.String, nullable=False)
#     doctor_id = db.Column(
#         db.Integer, db.ForeignKey('users.id'), nullable=False)


# class Education(db.Model):
#     __tablename__ = "education"
#     id = db.Column(db.Integer, primary_key=True)
#     institution = db.Column(db.String(40), nullable=False)
#     desciripton = db.Column(db.String(500), nullable=False)
#     start_date = db.Column(db.DateTime, nullable=False)
#     end_date = db.Column(db.DateTime, nullable=False)
#     average = db.Column(db.Float, nullable=False)
#     doctor_id = db.Column(
#         db.Integer, db.ForeignKey('users.id'), nullable=False)


# class Certification(db.Model):
#     __tablename__ = "certification"
#     id = db.Column(db.Integer, primary_key=True)
#     institution = db.Column(db.String(40), nullable=False)
#     desciripton = db.Column(db.String(500), nullable=False)
#     start_date = db.Column(db.DateTime, nullable=False)
#     end_date = db.Column(db.DateTime, nullable=True, default=None)
#     doctor_id = db.Column(
#         db.Integer, db.ForeignKey('users.id'), nullable=False)


# class Blog(db.Model):
#     __tablename__ = "blog"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(40), nullable=False)
#     text = db.Column(db.String, nullable=False)
#     doctor_id = db.Column(
#         db.Integer, db.ForeignKey('users.id'), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow())


# class Role(db.Model):
#     __tablename__ = "roles"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(40), nullable=False)

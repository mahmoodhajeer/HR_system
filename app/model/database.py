from flask_sqlalchemy import SQLAlchemy
import datetime
from marshmallow import Schema, fields, pre_load, validate, ValidationError
from flask_marshmallow import Marshmallow

ma = Marshmallow()
db = SQLAlchemy()

class Candidate(db.Model):
    __tablename__ = 'candidate'

    id                     = db.Column(db.Integer, primary_key=True)
    full_name              = db.Column(db.String(30),nullable=False)
    date_of_birth          = db.Column(db.String(10),nullable=False)
    years_of_experience    = db.Column(db.Integer, nullable=False)
    department_ID          = db.Column(db.Integer, nullable=False)
    resume                 = db.Column(db.String(10), nullable=False)
    created                = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)


class CandidateSchema(ma.Schema):
    id                    = fields.Integer(dump_only=True)
    full_name             = fields.String(required=True, error_messages={"required": "name is required."})
    date_of_birth         = fields.String(required=True, error_messages={"required": "date of birth is required."})
    years_of_experience   = fields.Integer(required=True,  error_messages={"required": "years of experience is required."})
    #department_ID values: IT = 0, HR = 1, Finance = 2
    department_ID         = fields.Integer(required=True, validate=validate.OneOf([0, 1, 2]), error_messages={"required": "Age is required."})
    resume                = fields.String(required=True, error_messages={"required": "resume is required."})
    created               = fields.DateTime(dump_only=True)
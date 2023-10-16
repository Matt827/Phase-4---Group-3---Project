from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

class House(db.model, SerializerMixin):
    __tablename__ = 'houses'
    
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.String)
    description = db.Column(db.String)
    num_of_beds = db.Column(db.String)
    num_of_baths = db.Column(db.String)
    square_feet = db.Column(db.Integer)

class Account(db.model, SerializerMixin):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key = True)
    name  = db.Column(db.String)

class Villow(db.model, SerializerMixin):
    __tablename__ = 'villows'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    house_id = db.Column(db.Integer,db.ForeignKey("houses.id"))
    account_id = db.Column(db.Integer,db.ForeignKey("accounts.id"))
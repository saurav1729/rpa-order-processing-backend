from utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    contact_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    users = db.relationship('User', backref='company', lazy=True, cascade="all, delete")
    Connections = db.relationship('Connection', back_populates='company', lazy=True, cascade="all, delete")  # Corrected

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "contact_number": self.contact_number,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(100), nullable=False)
#     last_name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     role = db.Column(db.String(50), nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
#     updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
#     company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

# class Connection(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     email_monitoring_address = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
#     updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
#     company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
#     rpabot = db.relationship('RpaBot', backref='Connection', uselist=False, cascade="all, delete")

# class RpaBot(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     status = db.Column(db.String(50), nullable=False)
#     last_active_at = db.Column(db.DateTime, nullable=True)
#     created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
#     updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
#     Connection_id = db.Column(db.Integer, db.ForeignKey('Connection.id'), nullable=False)
#     total_orders_processed = db.Column(db.Integer, nullable=False, default=0)
#     total_errors = db.Column(db.Integer, nullable=False, default=0)
#     error_rate = db.Column(db.Float, nullable=False, default=0.0)




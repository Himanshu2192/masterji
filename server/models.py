from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class AdminUser(db.Model):
    __tablename__ = "admin_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "is_active": self.is_active}


class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "slug": self.slug,
            "name": self.name,
            "description": self.description
        }


class ContactInquiry(db.Model):
    __tablename__ = "contact_inquiries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(30), nullable=True)
    service = db.Column(db.String(50), nullable=True)
    company = db.Column(db.String(160), nullable=True)
    preferred_contact = db.Column(db.String(20), nullable=True)
    budget_range = db.Column(db.String(50), nullable=True)
    timeline = db.Column(db.String(50), nullable=True)
    pickup_address = db.Column(db.Text, nullable=True)
    pickup_date = db.Column(db.Date, nullable=True)
    pickup_time = db.Column(db.String(30), nullable=True)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="new", index=True)
    internal_notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "service": self.service,
            "company": self.company,
            "preferred_contact": self.preferred_contact,
            "budget_range": self.budget_range,
            "timeline": self.timeline,
            "pickup_address": self.pickup_address,
            "pickup_date": self.pickup_date.isoformat() if self.pickup_date else None,
            "pickup_time": self.pickup_time,
            "message": self.message,
            "status": self.status,
            "internal_notes": self.internal_notes,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

from flask import Blueprint, request, jsonify
from models import db, ContactInquiry
from datetime import date
from sqlalchemy.exc import SQLAlchemyError
from auth import admin_required

contact_bp = Blueprint("contact", __name__)


@contact_bp.post("/")
def submit_contact():
    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip().lower()
    message = str(data.get("message", "")).strip()

    if not name or not email or not message:
        return jsonify({"error": "name, email and message are required"}), 400
    optional_lengths = {
        "phone": 30,
        "service": 50,
        "company": 160,
        "preferred_contact": 20,
        "budget_range": 50,
        "timeline": 50,
    }
    if len(name) > 120 or len(email) > 120 or len(message) > 10000:
        return jsonify({"error": "One or more fields exceed the allowed length"}), 400
    if any(
        len(str(data.get(field, ""))) > max_length
        for field, max_length in optional_lengths.items()
    ):
        return jsonify({"error": "One or more fields exceed the allowed length"}), 400
    pickup_date = None
    if data.get("pickup_date"):
        try:
            pickup_date = date.fromisoformat(str(data["pickup_date"]))
        except ValueError:
            return jsonify({"error": "pickup_date must use YYYY-MM-DD format"}), 400

    inquiry = ContactInquiry(
        name=name,
        email=email,
        phone=str(data.get("phone", "")).strip() or None,
        service=str(data.get("service", "")).strip() or None,
        company=str(data.get("company", "")).strip() or None,
        preferred_contact=str(data.get("preferred_contact", "")).strip() or None,
        budget_range=str(data.get("budget_range", "")).strip() or None,
        timeline=str(data.get("timeline", "")).strip() or None,
        pickup_address=str(data.get("pickup_address", "")).strip() or None,
        pickup_date=pickup_date,
        pickup_time=str(data.get("pickup_time", "")).strip() or None,
        message=message
    )
    try:
        db.session.add(inquiry)
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Unable to save your enquiry right now"}), 503

    return jsonify(inquiry.to_dict()), 201


@contact_bp.get("/")
@admin_required
def list_contacts():
    inquiries = ContactInquiry.query.order_by(ContactInquiry.created_at.desc()).all()
    return jsonify([i.to_dict() for i in inquiries])

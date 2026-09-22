from datetime import date
from flask import Blueprint, jsonify, request, session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from auth import admin_required, issue_token
from models import AdminUser, ContactInquiry, Service, db

admin_bp = Blueprint("admin", __name__)


def _json():
    return request.get_json(silent=True) or {}


def _text(data, key, limit, required=False):
    value = str(data.get(key, "")).strip()
    if required and not value:
        raise ValueError("%s is required" % key)
    if len(value) > limit:
        raise ValueError("%s exceeds the allowed length" % key)
    return value or None


@admin_bp.post("/login")
def login():
    data = _json()
    username = str(data.get("username", "")).strip()
    password = data.get("password")
    user = AdminUser.query.filter_by(username=username).first()
    if not user or not user.is_active or not isinstance(password, str) or not user.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 401
    session.clear()
    session["admin_id"] = user.id
    return jsonify({"admin": user.to_dict(), "token": issue_token(user)})


@admin_bp.post("/logout")
def logout():
    session.clear()
    return jsonify({"message": "Logged out"})


@admin_bp.get("/me")
@admin_required
def me():
    from auth import _current_admin
    return jsonify(_current_admin().to_dict())


def _service_payload(data, existing=None, partial=False):
    if partial and existing:
        data = {**existing.to_dict(), **data}
    slug = _text(data, "slug", 50, True)
    name = _text(data, "name", 100, True)
    description = _text(data, "description", 10000)
    if existing:
        existing.slug, existing.name, existing.description = slug, name, description
        return existing
    return Service(slug=slug, name=name, description=description)


@admin_bp.get("/services")
@admin_required
def list_services():
    return jsonify([item.to_dict() for item in Service.query.order_by(Service.id).all()])


@admin_bp.post("/services")
@admin_required
def create_service():
    try:
        service = _service_payload(_json())
        db.session.add(service)
        db.session.commit()
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "slug already exists"}), 409
    return jsonify(service.to_dict()), 201


@admin_bp.route("/services/<int:service_id>", methods=["PUT", "PATCH"])
@admin_required
def update_service(service_id):
    service = db.session.get(Service, service_id)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    try:
        _service_payload(_json(), service, request.method == "PATCH")
        db.session.commit()
    except ValueError as error:
        db.session.rollback()
        return jsonify({"error": str(error)}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "slug already exists"}), 409
    return jsonify(service.to_dict())


@admin_bp.delete("/services/<int:service_id>")
@admin_required
def delete_service(service_id):
    service = db.session.get(Service, service_id)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted"})


def _inquiry_payload(data, existing=None, partial=False):
    if partial and existing:
        current = {
            key: getattr(existing, key)
            for key in (
                "name", "email", "phone", "service", "company",
                "preferred_contact", "budget_range", "timeline",
                "pickup_address", "pickup_date", "pickup_time", "message",
                "status", "internal_notes",
            )
        }
        data = {**current, **data}
    fields = {
        "name": (120, True), "email": (120, True), "phone": (30, False),
        "service": (50, False), "company": (160, False),
        "preferred_contact": (20, False), "budget_range": (50, False),
        "timeline": (50, False), "pickup_address": (10000, False),
        "pickup_time": (30, False), "message": (10000, True),
    }
    values = {}
    for key, (limit, required) in fields.items():
        values[key] = _text(data, key, limit, required)
    values["email"] = values["email"].lower()
    values["status"] = _text(data, "status", 20) or (existing.status if existing else "new")
    if values["status"] not in {"new", "contacted", "qualified", "closed"}:
        raise ValueError("status is invalid")
    values["internal_notes"] = _text(data, "internal_notes", 10000)
    if data.get("pickup_date"):
        try:
            values["pickup_date"] = date.fromisoformat(str(data["pickup_date"]))
        except ValueError:
            raise ValueError("pickup_date must use YYYY-MM-DD format")
    else:
        values["pickup_date"] = None
    if existing:
        for key, value in values.items():
            setattr(existing, key, value)
        return existing
    return ContactInquiry(**values)


@admin_bp.get("/contact-inquiries")
@admin_required
def list_inquiries():
    return jsonify([item.to_dict() for item in ContactInquiry.query.order_by(ContactInquiry.created_at.desc()).all()])


@admin_bp.post("/contact-inquiries")
@admin_required
def create_inquiry():
    try:
        inquiry = _inquiry_payload(_json())
        db.session.add(inquiry)
        db.session.commit()
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Unable to save inquiry"}), 503
    return jsonify(inquiry.to_dict()), 201


@admin_bp.route("/contact-inquiries/<int:inquiry_id>", methods=["PUT", "PATCH"])
@admin_required
def update_inquiry(inquiry_id):
    inquiry = db.session.get(ContactInquiry, inquiry_id)
    if not inquiry:
        return jsonify({"error": "Contact inquiry not found"}), 404
    try:
        _inquiry_payload(_json(), inquiry, request.method == "PATCH")
        db.session.commit()
    except ValueError as error:
        db.session.rollback()
        return jsonify({"error": str(error)}), 400
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Unable to update inquiry"}), 503
    return jsonify(inquiry.to_dict())


@admin_bp.delete("/contact-inquiries/<int:inquiry_id>")
@admin_required
def delete_inquiry(inquiry_id):
    inquiry = db.session.get(ContactInquiry, inquiry_id)
    if not inquiry:
        return jsonify({"error": "Contact inquiry not found"}), 404
    db.session.delete(inquiry)
    db.session.commit()
    return jsonify({"message": "Contact inquiry deleted"})

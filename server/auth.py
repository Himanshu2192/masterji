from functools import wraps

from flask import current_app, jsonify, request, session
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

from models import AdminUser


def _serializer():
    return URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt="admin-auth")


def issue_token(user):
    return _serializer().dumps({"admin_id": user.id})


def _current_admin():
    admin_id = session.get("admin_id")
    if admin_id:
        return AdminUser.query.filter_by(id=admin_id, is_active=True).first()

    header = request.headers.get("Authorization", "")
    if not header.lower().startswith("bearer "):
        return None
    try:
        payload = _serializer().loads(header[7:].strip(), max_age=current_app.config["ADMIN_TOKEN_MAX_AGE"])
    except (BadSignature, SignatureExpired, ValueError):
        return None
    return AdminUser.query.filter_by(id=payload.get("admin_id"), is_active=True).first()


def admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        admin = _current_admin()
        if admin is None:
            return jsonify({"error": "Authentication required"}), 401
        return view(*args, **kwargs)

    return wrapped


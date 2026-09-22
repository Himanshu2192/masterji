from flask import Blueprint, jsonify
from models import Service

services_bp = Blueprint("services", __name__)


@services_bp.get("/")
def list_services():
    services = Service.query.all()
    return jsonify([s.to_dict() for s in services])


@services_bp.get("/<slug>")
def get_service(slug):
    service = Service.query.filter_by(slug=slug).first()
    if not service:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(service.to_dict())

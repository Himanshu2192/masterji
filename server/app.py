from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
from config import Config
from models import db
from routes.services import services_bp
from routes.contact import contact_bp
from routes.admin import admin_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    origins = app.config.get("ALLOWED_ORIGINS", "*")
    CORS(app, origins=origins.split(",") if origins != "*" else "*")
    db.init_app(app)

    app.register_blueprint(services_bp, url_prefix="/api/services")
    app.register_blueprint(contact_bp, url_prefix="/api/contact")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")

    @app.before_request
    def enforce_https():
        # Redirects http -> https when ENFORCE_HTTPS is on. In most real
        # deployments TLS is already terminated by the hosting/proxy layer,
        # so this is a backup safety net, not a substitute for a real
        # certificate (Let's Encrypt / your host's managed TLS).
        if not app.config.get("ENFORCE_HTTPS"):
            return None
        is_secure = request.is_secure or request.headers.get("X-Forwarded-Proto", "http") == "https"
        if not is_secure:
            return redirect(request.url.replace("http://", "https://", 1), code=301)
        return None

    @app.after_request
    def set_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        if app.config.get("ENFORCE_HTTPS"):
            response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
        return response

    @app.errorhandler(404)
    def not_found(_error):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(500)
    def server_error(_error):
        return jsonify({"error": "Internal server error"}), 500

    @app.get("/api/health")
    def health():
        return {"status": "ok"}

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)

"""Create an administrator.

Usage:
    ADMIN_USERNAME=admin ADMIN_PASSWORD='use-a-long-random-password' \
      DATABASE_URL=... python scripts/create_admin.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from models import AdminUser, db

username = os.environ.get("ADMIN_USERNAME", "").strip()
password = os.environ.get("ADMIN_PASSWORD", "")
if not username or not password:
    raise SystemExit("ADMIN_USERNAME and ADMIN_PASSWORD are required")
if len(username) > 80 or len(password) < 12:
    raise SystemExit("Username must be <= 80 characters and password must be at least 12 characters")

app = create_app()
with app.app_context():
    user = AdminUser.query.filter_by(username=username).first()
    if user is None:
        user = AdminUser(username=username)
        db.session.add(user)
    user.set_password(password)
    user.is_active = True
    db.session.commit()
    print("Admin user created or updated.")

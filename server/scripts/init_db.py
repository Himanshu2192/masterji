"""
Create (or update) database tables against a real Postgres instance.

Vercel's serverless functions never execute the `if __name__ == "__main__":`
block in app.py, so table creation has to be run separately, once, pointed
at your production database.

Usage:
    DATABASE_URL=postgresql://user:pass@host:5432/dbname python scripts/init_db.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from models import db

app = create_app()
with app.app_context():
    db.create_all()
    print("Tables created (or already existed).")

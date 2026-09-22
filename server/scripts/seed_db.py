"""
Seed the `services` table with the four core services.
Safe to re-run: skips any slug that already exists.

Usage:
    DATABASE_URL=postgresql://user:pass@host:5432/dbname python scripts/seed_db.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from models import db, Service

SERVICES = [
    ("tour_travel", "Tour & Travel Bookings",
     "Domestic and international trip planning, flights, hotels and packages."),
    ("solar_panel", "Solar Panel Installation",
     "Residential and commercial solar setup, consultation and maintenance."),
    ("interior_design", "Interior Design",
     "End-to-end interior design for homes and offices."),
    ("touring_services", "Touring Services",
     "Guided local tours, itineraries and travel logistics."),
]

app = create_app()
with app.app_context():
    for slug, name, description in SERVICES:
        if not Service.query.filter_by(slug=slug).first():
            db.session.add(Service(slug=slug, name=name, description=description))
            print(f"Added: {name}")
        else:
            print(f"Skipped (already exists): {name}")
    db.session.commit()
    print("Done.")

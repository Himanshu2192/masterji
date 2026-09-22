"""
Vercel Python serverless entrypoint.

Vercel's @vercel/python builder looks for a WSGI-compatible `app` object
in a file under /api. This just imports and exposes the real Flask app
factory result from ../app.py.
"""
import os
import sys

# Make the server/ root (one level up from api/) importable, so
# `from app import create_app` resolves regardless of Vercel's cwd.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app  # noqa: E402

app = create_app()

import os
from urllib.parse import quote

basedir = os.path.abspath(os.path.dirname(__file__))


def _normalize_db_url(url: str) -> str:
    # Some managed Postgres providers (Neon, Vercel Postgres, Heroku-style)
    # hand out "postgres://" URLs, but SQLAlchemy 1.4+/2.x requires
    # "postgresql://". Normalize so either form works.
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    return url


class Config:
    # Set these via environment variables in production (Vercel project
    # → Settings → Environment Variables). Defaults below are for local dev only.
    DB_USER = os.environ.get("DB_USER", "postgres")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "hk219287@")
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", "5432")
    DB_NAME = os.environ.get("DB_NAME", "masterji_db")

    _default_url = (
        f"postgresql://{quote(DB_USER, safe='')}:{quote(DB_PASSWORD, safe='')}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_DATABASE_URI = _normalize_db_url(
        os.environ.get("DATABASE_URL", _default_url)
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    ADMIN_TOKEN_MAX_AGE = int(os.environ.get("ADMIN_TOKEN_MAX_AGE", str(8 * 60 * 60)))
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"

    # HTTPS is already handled by Vercel's edge network with a managed
    # certificate once your domain is connected. This flag is only a
    # safety-net redirect for other hosts; leave it off on Vercel.
    ENFORCE_HTTPS = os.environ.get("ENFORCE_HTTPS", "false").lower() == "true"
    SESSION_COOKIE_SECURE = ENFORCE_HTTPS

    # Restrict CORS to your deployed frontend once you know its URL, e.g.
    # https://masterji-client.vercel.app — comma-separated for multiple
    # origins (production + preview URLs). "*" (default) is fine for local dev.
    ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "*")

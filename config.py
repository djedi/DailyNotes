import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    JWT_SECRET_KEY = os.environ.get("API_SECRET_KEY")
    DB_ENCRYPTION_KEY = os.environ.get("DB_ENCRYPTION_KEY")
    PREVENT_SIGNUPS = os.environ.get("PREVENT_SIGNUPS", False)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI"
    ) or "sqlite:///" + os.path.join(basedir + "/config", "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)
    EXPORT_FILE = os.path.join(basedir, "config", "export.zip")
    UPLOAD_FOLDER = os.path.join(basedir, "config", "uploads")
    MAX_UPLOAD_SIZE = int(
        os.environ.get("MAX_UPLOAD_SIZE") or 10 * 1024 * 1024
    )  # 10MB default
    ALLOWED_UPLOAD_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
    DEFAULT_TIMEZONE = os.environ.get("DEFAULT_TIMEZONE") or None

    # SMTP Configuration for password reset and magic link emails
    SMTP_HOST = os.environ.get("SMTP_HOST")
    SMTP_PORT = int(os.environ.get("SMTP_PORT") or 587)
    SMTP_USER = os.environ.get("SMTP_USER")
    SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
    SMTP_USE_TLS = (os.environ.get("SMTP_USE_TLS") or "true").lower() == "true"
    SMTP_FROM_EMAIL = os.environ.get("SMTP_FROM_EMAIL")
    SMTP_FROM_NAME = os.environ.get("SMTP_FROM_NAME") or "DailyNotes"

    # Application URL for email links (e.g., password reset, magic link)
    APP_URL = os.environ.get("APP_URL") or "http://localhost:8000"

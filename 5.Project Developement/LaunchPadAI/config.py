import os
from dotenv import load_dotenv

# -----------------------------------------
# Load Environment Variables
# -----------------------------------------
load_dotenv()


class Config:
    """
    LaunchPad AI Configuration
    """

    # -----------------------------------------
    # Flask Configuration
    # -----------------------------------------

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change-this-secret-key"
    )

    DEBUG = True

    TESTING = False

    # -----------------------------------------
    # Database Configuration
    # -----------------------------------------

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///launchpad.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # -----------------------------------------
    # Gemini AI Configuration
    # -----------------------------------------

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Default model for google-genai SDK
    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )

    # -----------------------------------------
    # Request Limits
    # -----------------------------------------

    MAX_CONTENT_LENGTH = 5 * 1024 * 1024

    MAX_STARTUP_LENGTH = 2000

    MIN_STARTUP_LENGTH = 50

    # -----------------------------------------
    # Session Settings
    # -----------------------------------------

    SESSION_COOKIE_HTTPONLY = True

    SESSION_COOKIE_SAMESITE = "Lax"

    PERMANENT_SESSION_LIFETIME = 3600

    # -----------------------------------------
    # Upload Folder (Future Use)
    # -----------------------------------------

    UPLOAD_FOLDER = "uploads"
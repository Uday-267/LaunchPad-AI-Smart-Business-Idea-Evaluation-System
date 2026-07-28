from flask import Flask
from config import Config
from models.startup import db

from routes.home import home_bp
from routes.history import history_bp

import logging


def create_app():
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)

    # -----------------------------
    # Load Configuration
    # -----------------------------
    app.config.from_object(Config)

    # -----------------------------
    # Initialize Database
    # -----------------------------
    db.init_app(app)

    # -----------------------------
    # Configure Logging
    # -----------------------------
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )

    # -----------------------------
    # Register Blueprints
    # -----------------------------
    app.register_blueprint(home_bp)
    app.register_blueprint(history_bp)

    # -----------------------------
    # Create Database Tables
    # -----------------------------
    with app.app_context():
        db.create_all()

    return app


# ---------------------------------
# Create Application
# ---------------------------------

app = create_app()


# ---------------------------------
# Run Server
# ---------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
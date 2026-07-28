from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# ------------------------------------------
# SQLAlchemy Instance
# ------------------------------------------

db = SQLAlchemy()


# ------------------------------------------
# Startup Analysis Model
# ------------------------------------------

class StartupAnalysis(db.Model):
    """
    Stores startup information and
    AI-generated analysis reports.
    """

    __tablename__ = "startup_analysis"

    # Primary Key
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Startup Information
    startup_name = db.Column(
        db.String(150),
        nullable=False
    )

    startup_idea = db.Column(
        db.Text,
        nullable=False
    )

    target_audience = db.Column(
        db.String(250),
        nullable=False
    )

    business_model = db.Column(
        db.String(250),
        nullable=False
    )

    product_features = db.Column(
        db.Text,
        nullable=False
    )

    # AI Generated Report
    analysis_result = db.Column(
        db.Text,
        nullable=False
    )

    # Timestamp
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # ------------------------------------------
    # Representation
    # ------------------------------------------

    def __repr__(self):
        return (
            f"<StartupAnalysis "
            f"{self.id} - "
            f"{self.startup_name}>"
        )

    # ------------------------------------------
    # Convert Object to Dictionary
    # ------------------------------------------

    def to_dict(self):
        """
        Convert model into dictionary.
        Useful for future REST APIs.
        """

        return {

            "id": self.id,

            "startup_name": self.startup_name,

            "startup_idea": self.startup_idea,

            "target_audience": self.target_audience,

            "business_model": self.business_model,

            "product_features": self.product_features,

            "analysis_result": self.analysis_result,

            "created_at": self.created_at.strftime(
                "%d-%m-%Y %H:%M"
            )

        }
from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    redirect,
    url_for,
)
from markdown import markdown
from models.startup import db, StartupAnalysis
from services.gemini_service import gemini_service
from config import Config
import logging

home_bp = Blueprint("home", __name__)


# ==========================================================
# Validate User Input
# ==========================================================

def validate_input(data):

    required_fields = [
        "startup_name",
        "startup_idea",
        "target_audience",
        "business_model",
        "product_features"
    ]

    for field in required_fields:

        value = data.get(field, "").strip()

        if not value:
            return False, f"{field.replace('_',' ').title()} is required."

        if len(value) > Config.MAX_STARTUP_LENGTH:
            return (
                False,
                f"{field.replace('_',' ').title()} exceeds "
                f"{Config.MAX_STARTUP_LENGTH} characters."
            )

    if len(data["startup_idea"]) < Config.MIN_STARTUP_LENGTH:
        return (
            False,
            f"Startup Idea should contain at least "
            f"{Config.MIN_STARTUP_LENGTH} characters."
        )

    return True, ""


# ==========================================================
# Home Page
# ==========================================================

@home_bp.route("/")
def home():

    return render_template("home.html")


# ==========================================================
# Startup Validation Page
# ==========================================================

@home_bp.route("/validate", methods=["GET", "POST"])
def validate():

    if request.method == "GET":

        return render_template("validate.html")


    startup_name = request.form.get("startup_name", "").strip()
    startup_idea = request.form.get("startup_idea", "").strip()
    target_audience = request.form.get("target_audience", "").strip()
    business_model = request.form.get("business_model", "").strip()
    product_features = request.form.get("product_features", "").strip()

    form_data = {
        "startup_name": startup_name,
        "startup_idea": startup_idea,
        "target_audience": target_audience,
        "business_model": business_model,
        "product_features": product_features,
    }

    valid, message = validate_input(form_data)

    if not valid:

        return render_template(
            "validate.html",
            error=message,
            form=form_data,
        )

    # ======================================================
    # Gemini Analysis
    # ======================================================

    response = gemini_service.analyze_startup(
        startup_name,
        startup_idea,
        target_audience,
        business_model,
        product_features,
    )

    if not response["success"]:

        logging.error(response["message"])

        return render_template(
            "validate.html",
            error=response["message"],
            form=form_data,
        )

    report_html = markdown(response["result"])

    # ======================================================
    # Save Report
    # ======================================================

    try:

        analysis = StartupAnalysis(
            startup_name=startup_name,
            startup_idea=startup_idea,
            target_audience=target_audience,
            business_model=business_model,
            product_features=product_features,
            analysis_result=response["result"],
        )

        db.session.add(analysis)
        db.session.commit()

        logging.info(
            f"Startup '{startup_name}' analyzed successfully."
        )

        return redirect(
            url_for(
                "history.report",
                id=analysis.id
            )
        )

    except Exception as e:

        db.session.rollback()

        logging.exception(e)

        return render_template(
            "validate.html",
            error="Database Error. Please try again.",
            form=form_data,
            result=report_html,
        )


# ==========================================================
# REST API
# ==========================================================

@home_bp.route("/api/analyze", methods=["POST"])
def api_analyze():

    data = request.get_json()

    if not data:

        return jsonify({
            "success": False,
            "message": "No JSON received."
        }), 400

    valid, message = validate_input(data)

    if not valid:

        return jsonify({
            "success": False,
            "message": message
        }), 400

    response = gemini_service.analyze_startup(
        data["startup_name"],
        data["startup_idea"],
        data["target_audience"],
        data["business_model"],
        data["product_features"],
    )

    return jsonify(response)
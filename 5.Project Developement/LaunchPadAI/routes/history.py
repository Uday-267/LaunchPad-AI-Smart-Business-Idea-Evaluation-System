from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from markdown import markdown

from models.startup import db, StartupAnalysis

import logging

history_bp = Blueprint("history", __name__)


# ==========================================================
# History Page
# ==========================================================

@history_bp.route("/history")
def history():

    search = request.args.get("search", "").strip()

    try:

        if search:

            analyses = StartupAnalysis.query.filter(
                StartupAnalysis.startup_name.ilike(f"%{search}%")
            ).order_by(
                StartupAnalysis.created_at.desc()
            ).all()

        else:

            analyses = StartupAnalysis.query.order_by(
                StartupAnalysis.created_at.desc()
            ).all()

        return render_template(
            "history.html",
            analyses=analyses,
            search=search,
        )

    except Exception as e:

        logging.exception(e)

        flash("Unable to load startup history.", "danger")

        return render_template(
            "history.html",
            analyses=[],
            search=search,
        )


# ==========================================================
# Report Page
# ==========================================================

@history_bp.route("/report/<int:id>")
def report(id):

    analysis = StartupAnalysis.query.get_or_404(id)

    # Convert Markdown → HTML
    formatted_report = markdown(
        analysis.analysis_result,
        extensions=["tables", "fenced_code"]
    )

    return render_template(
        "report.html",
        analysis=analysis,
        formatted_report=formatted_report,
    )


# ==========================================================
# Delete Report
# ==========================================================

@history_bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    analysis = StartupAnalysis.query.get_or_404(id)

    try:

        db.session.delete(analysis)

        db.session.commit()

        logging.info(
            f"Deleted Startup Analysis ID {id}"
        )

        flash(
            "Startup report deleted successfully.",
            "success"
        )

    except Exception as e:

        db.session.rollback()

        logging.exception(e)

        flash(
            "Unable to delete report.",
            "danger"
        )

    return redirect(
        url_for("history.history")
    )
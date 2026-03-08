from flask import Flask, render_template, request, redirect, url_for
from utils import load_reports, save_reports
from fallback import analyze_report
from ai_service import analyze_with_ai

app = Flask(__name__)


# ----------------------------
# Homepage
# ----------------------------
@app.route("/")
def index():

    reports = load_reports()

    query = request.args.get("q")

    if query:
        query = query.lower()
        reports = [
            r for r in reports
            if query in r["title"].lower()
            or query in r["location"].lower()
            or query in r["category"].lower()
        ]

    return render_template("index.html", reports=reports)


# ----------------------------
# View Report Details
# ----------------------------
@app.route("/report/<int:report_id>")
def view_report(report_id):

    reports = load_reports()

    report = next((r for r in reports if r["id"] == report_id), None)

    if not report:
        return "Report not found."

    return render_template("detail.html", report=report)


# ----------------------------
# Create Report
# ----------------------------
@app.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        title = request.form["title"].strip()
        description = request.form["description"].strip()
        location = request.form["location"].strip()
        severity = request.form["severity"].strip()

        # ---- validation ----

        if not title:
            return "Title is required."

        if len(description) < 10:
            return "Description must be at least 10 characters."

        if severity not in ["low", "medium", "high"]:
            return "Invalid severity value."

        # ---- AI analysis first ----

        ai_result = analyze_with_ai(description)

        if ai_result:

            category = ai_result["category"]
            summary = ai_result["summary"]
            steps = ai_result["next_steps"]
            analysis_source = "ai"

        else:

            fallback_result = analyze_report(description)

            category = fallback_result["category"]
            summary = fallback_result["summary"]
            steps = fallback_result["next_steps"]
            analysis_source = "fallback"

        reports = load_reports()

        new_report = {
            "id": len(reports) + 1,
            "title": title,
            "description": description,
            "location": location,
            "severity": severity,
            "category": category,
            "summary": summary,
            "next_steps": steps,
            "analysis_source": analysis_source
        }

        reports.append(new_report)

        save_reports(reports)

        return redirect(url_for("index"))

    return render_template("create.html")


# ----------------------------
# Edit Existing Report
# ----------------------------
@app.route("/edit/<int:report_id>", methods=["GET", "POST"])
def edit_report(report_id):

    reports = load_reports()

    report = next((r for r in reports if r["id"] == report_id), None)

    if not report:
        return "Report not found."

    if request.method == "POST":

        report["title"] = request.form["title"].strip()
        report["description"] = request.form["description"].strip()
        report["location"] = request.form["location"].strip()
        report["severity"] = request.form["severity"].strip()

        # ---- validation ----

        if not report["title"]:
            return "Title is required."

        if len(report["description"]) < 10:
            return "Description must be at least 10 characters."

        if report["severity"] not in ["low", "medium", "high"]:
            return "Invalid severity value."

        # ---- AI analysis first ----

        ai_result = analyze_with_ai(report["description"])

        if ai_result:

            report["category"] = ai_result["category"]
            report["summary"] = ai_result["summary"]
            report["next_steps"] = ai_result["next_steps"]
            report["analysis_source"] = "ai"

        else:

            fallback_result = analyze_report(report["description"])

            report["category"] = fallback_result["category"]
            report["summary"] = fallback_result["summary"]
            report["next_steps"] = fallback_result["next_steps"]
            report["analysis_source"] = "fallback"

        save_reports(reports)

        return redirect(url_for("view_report", report_id=report_id))

    return render_template("edit.html", report=report)


# ----------------------------
# Run Server
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
# Harbor

Harbor is a lightweight community safety and digital wellness assistant.

It allows users to report suspicious or unsafe situations and receive structured guidance about what the issue might be and what actions they can take.

The goal of Harbor is to turn scattered safety reports into **clear, understandable, and actionable information**.

---

# Scenario Chosen

**Intelligent Community Safety & Digital Wellness 🛡️**

Harbor focuses on helping people recognize and understand common safety issues such as:

- phishing emails  
- scam phone calls  
- fake investment messages  
- suspicious public WiFi networks  
- community safety concerns  

---

# Why Harbor Exists

In both community safety and cybersecurity, one of the biggest challenges is **signal vs noise**.

People frequently encounter suspicious messages, calls, or situations but often do not know:

- whether the situation is actually dangerous  
- what type of threat it might be  
- what actions they should take  

Harbor takes a simple approach:

1. collect a report  
2. analyze the situation  
3. summarize the risk  
4. provide recommended next steps  

The system also includes a fallback mechanism so it can still provide guidance even if AI analysis fails.

---

# Example User Flow

### 1. A user reports a suspicious incident

Example report:

**Title**  
Crypto Investment Message

**Description**  
"I received a message promising guaranteed crypto profits if I invest immediately."

**Location**  
Austin

**Severity**  
High

---

### 2. The system analyzes the report

After the report is submitted, the system analyzes the description.

The system attempts:

1. AI-assisted analysis  
2. Rule-based fallback classification if AI is unavailable

This ensures the system always produces a result.

---

### 3. The system generates guidance

Example output:

**Category**  
Investment Scam

**Summary**  
This report appears to involve an unsolicited investment offer promising unrealistic returns.

**Recommended Next Steps**

- Do not send money or personal details  
- Verify the organization independently  
- Report the account or message to the platform  

---

### 4. The report is stored

Reports are stored in a simple JSON database:

This allows the system to maintain a history of incidents.

---

### 5. The report appears on the dashboard

The report becomes visible on the dashboard where users can:

- view reports  
- search reports  
- read incident analysis  
- edit reports  

---

# Core Features

Harbor currently supports:

- Create new safety reports  
- View all reports on a dashboard  
- View detailed report analysis  
- Edit existing reports  
- Search reports by title, category, or location  
- Incident classification  
- AI-assisted analysis  
- Rule-based fallback analysis  
- Lightweight JSON storage  
- Unit tests using pytest  

---

# Tech Stack

- Python
- Flask
- HTML / CSS
- JSON file storage
- Pytest

📝 Case Study Summary

Candidate Name:
Kunsang Tsering

Scenario Chosen:
Intelligent Community Safety & Digital Wellness 🛡️

Estimated Time Spent:
Approximately 5 hours

🚀 Quick Start
● Prerequisites

Python 3.10+

pip

Git

● Run Commands

Clone the repository:

git clone https://github.com/ktsering2003/harbor-safety-assistant.git
cd harbor-safety-assistant

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

python3 -m pip install -r requirements.txt

Run the application:

python3 app.py

Open the app in your browser:

http://127.0.0.1:5000
● Test Commands

Run the unit tests:

python3 -m pytest
🤖 AI Disclosure

Did you use an AI assistant (Copilot, ChatGPT, etc.)?
Yes.

How did you verify the suggestions?

All suggestions were reviewed manually before being used. I tested each change locally, confirmed that the application behavior remained correct, and ensured the logic aligned with the intended functionality of the project.

I also ran the unit tests and manually tested the main user flow (creating reports, viewing reports, and editing reports) to confirm that the system behaved as expected.

Example of a suggestion I rejected or modified

One suggestion proposed relying entirely on AI-based classification for report analysis. I chose to modify this approach and implement a rule-based fallback classifier so the system would still function reliably even if AI analysis fails or is unavailable.

⚖️ Tradeoffs & Prioritization

What did you cut to stay within the 4–6 hour limit?

To keep the project within the time limit, I intentionally avoided adding:

database infrastructure (e.g., PostgreSQL)

authentication or user accounts

deployment configuration

advanced analytics or incident trend detection

Instead, I focused on delivering a clean end-to-end flow that demonstrates the core concept: collecting a report, analyzing it, generating guidance, and displaying it in a simple UI.

What would you build next if you had more time?

If I extended the project further, I would add:

database-backed storage instead of JSON

automatic severity scoring based on threat patterns

incident trend detection and visual dashboards

stronger AI classification and prompt tuning

threat pattern clustering across reports

These additions would help the system better identify patterns across incidents and provide deeper insights.

Known limitations

JSON storage is not designed for large-scale data

incident classification is intentionally simple

severity levels are currently user-defined

AI classification is optional and not deeply tuned

The current version focuses on demonstrating the core reporting and analysis workflow rather than production-scale infrastructure.

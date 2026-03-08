# Harbor

Harbor is a lightweight community safety and digital wellness assistant.

It allows users to report suspicious or unsafe situations and receive simple, structured guidance about what the issue might be and what actions they can take.

The goal of Harbor is to turn scattered safety reports into **clear, understandable, and actionable information**.

---

# Scenario Chosen

Intelligent Community Safety & Digital Wellness 🛡️

Harbor focuses on helping people recognize and understand common safety issues such as:

• phishing emails  
• scam phone calls  
• fake investment messages  
• suspicious public WiFi networks  
• local community safety concerns  

---

# Why Harbor Exists

In both community safety and cybersecurity, one of the biggest challenges is **signal vs noise**.

People frequently encounter suspicious messages, calls, or situations but often do not know:

• whether the situation is actually dangerous  
• what type of threat it might be  
• what actions they should take  

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

Title  
Crypto Investment Message

Description  
"I received a message promising guaranteed crypto profits if I invest immediately."

Location  
Austin

Severity  
High

---

### 2. The system analyzes the report

After the report is submitted, the system analyzes the description.

The system attempts:

AI-assisted analysis

If AI is unavailable or fails, the system automatically uses a rule-based fallback classifier.

This ensures the system always produces a result.

---

### 3. The system generates guidance

Example result:

Category  
Investment Scam

Summary  
This report appears to involve an unsolicited investment offer promising unrealistic returns.

Recommended Next Steps

• Do not send money or personal details  
• Verify the organization independently  
• Report the account or message to the platform  

---

### 4. The report is stored

Reports are stored in a simple JSON database:


## Tech Stack

- Python
- Flask
- HTML / CSS
- JSON file storage
- Pytest
- OpenAI API support via `.env` (optional / fallback-safe)



This allows the system to maintain a history of incidents.

---

### 5. The report appears on the dashboard

The report becomes visible on the dashboard where users can:

• view reports  
• search reports  
• read incident analysis  
• edit reports  

---

# Core Features

Harbor currently supports:

• Create new safety reports  
• View all reports on a dashboard  
• View detailed report analysis  
• Edit existing reports  
• Search reports by title, category, or location  
• Incident classification  
• AI-assisted analysis  
• Rule-based fallback analysis  
• Lightweight JSON storage  
• Unit tests with pytest  

---

# Tech Stack

Python  
Flask  
HTML / CSS  
JSON data storage  
Pytest

Optional AI integration via environment configuration.

---

# Project Structure

## Quick Start

### Prerequisites

- Python 3.10+
- pip

### Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
=======
### Incident Severity

Severity levels in Harbor are currently **user-defined**.

When creating a report, users choose:

- Low
- Medium
- High

This allows the reporting user to express the perceived urgency of the situation.

The AI-assisted classification system focuses on determining:

- threat category
- summary of the issue
- recommended next steps

Future improvements could allow the system to automatically suggest
or adjust severity levels based on detected threat patterns.
>>>>>>> e937cd9 (Complete Harbor Safety Assistant with AI classification and fallback system)

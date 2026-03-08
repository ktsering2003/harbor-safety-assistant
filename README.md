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

Optional AI integration via environment configuration.

---

# Project Structure

---

# Quick Start

## Prerequisites

- Python 3.10+
- pip

---

## Setup

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
nstall dependencies:

python3 -m pip install -r requirements.txt

Run the application:

python3 app.py

Open the application in your browser:

http://127.0.0.1:5000

Running Tests

Run unit tests using pytest:

python3 -m pytest


Future Improvements

This prototype focuses on simplicity and clarity. Future improvements could include:

database storage (PostgreSQL)

incident trend detection

automated severity scoring

improved AI classification

threat pattern analysis

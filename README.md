<<<<<<< HEAD
# Harbor

Harbor is a lightweight community safety and digital wellness assistant built for the Palo Alto Networks New Grad SWE take-home case study.

The goal of Harbor is to turn scattered or noisy safety reports into clear, calm, and actionable guidance. A user can create, view, update, and search reports. Each report is analyzed using a simple classification flow, and the system is designed to support an AI-assisted path with a rule-based fallback when AI is unavailable or unreliable.

## Scenario Chosen

Intelligent Community Safety & Digital Wellness 🛡️

## Why I Built This

One of the main problems in both community safety and cybersecurity is signal versus noise.

People often receive fragmented information about scams, suspicious activity, unsafe networks, or digital threats, but they do not always know what matters most or what to do next. I wanted to build something that takes a raw report and turns it into something more structured, understandable, and useful.

Harbor is a small prototype, but the pattern behind it is meaningful:
- ingest a signal
- classify it
- summarize it
- provide recommended next steps
- keep a fallback path when AI is unavailable or incorrect

That pattern is relevant to the broader security space, especially in environments where trust, speed, and clear action matter.

## Core Features

- Create a new safety report
- View all reports
- View report details
- Update an existing report
- Search reports by title, location, or category
- Analyze reports with rule-based classification
- Support AI-assisted analysis with a fallback path
- Use synthetic dataset only

## Tech Stack

- Python
- Flask
- HTML / CSS
- JSON file storage
- Pytest
- OpenAI API support via `.env` (optional / fallback-safe)

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

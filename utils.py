import json

DATA_FILE = "data/reports.json"

def load_reports():

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_reports(reports):

    with open(DATA_FILE, "w") as f:
        json.dump(reports, f, indent=2)
from fallback import analyze_report


def test_phishing_detection():
    result = analyze_report("Email pretending to be a bank asking for login credentials")
    assert result["category"] == "Phishing / Scam"
    assert len(result["next_steps"]) == 3


def test_network_detection():
    result = analyze_report("Suspicious open wifi network in apartment lobby")
    assert result["category"] == "Network Safety"


def test_unknown_fallback():
    result = analyze_report("Something strange happened but details are unclear")
    assert result["category"] == "General Advisory"
def analyze_report(description):
    text = description.lower()

    if any(word in text for word in ["email", "bank", "password", "login", "credential", "verify account"]):
        category = "Phishing / Scam"
        summary = "This report appears to describe a phishing attempt aimed at collecting sensitive account information."
        steps = [
            "Do not click any links or attachments",
            "Verify the sender through an official channel",
            "Change your password and enable two-factor authentication if needed"
        ]

    elif any(word in text for word in ["call", "support", "remote access", "microsoft", "apple support"]):
        category = "Phone Scam"
        summary = "This report appears to involve a scam caller pretending to offer technical or account support."
        steps = [
            "Hang up and avoid sharing personal information",
            "Do not install software or grant remote access",
            "Report the number as spam or fraud"
        ]

    elif any(word in text for word in ["wifi", "wi-fi", "network", "router", "public hotspot", "open network"]):
        category = "Network Safety"
        summary = "This report suggests a potential network safety issue involving an untrusted or suspicious connection."
        steps = [
            "Avoid connecting to unknown or open networks",
            "Use a trusted connection or VPN if available",
            "Review your device security settings"
        ]

    elif any(word in text for word in ["crypto", "investment", "returns", "trading group", "guaranteed profit"]):
        category = "Investment Scam"
        summary = "This report appears to involve an unsolicited or suspicious investment offer promising unrealistic returns."
        steps = [
            "Do not send money or personal details",
            "Verify the organization independently",
            "Report the account or message to the platform"
        ]

    elif any(word in text for word in ["theft", "stolen", "package", "break-in", "door", "suspicious person"]):
        category = "Physical Safety Concern"
        summary = "This report describes a local physical safety concern that may require caution or follow-up."
        steps = [
            "Stay aware of your surroundings",
            "Document useful details if safe to do so",
            "Contact local authorities or building management if appropriate"
        ]

    else:
        category = "General Advisory"
        summary = "This report describes a safety concern, but the exact type is unclear. A general precautionary response is recommended."
        steps = [
            "Review the situation carefully before acting",
            "Avoid sharing sensitive information until verified",
            "Escalate the concern if additional evidence appears"
        ]

    return {
        "category": category,
        "summary": summary,
        "next_steps": steps
    }
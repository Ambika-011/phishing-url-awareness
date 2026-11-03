import re
from urllib.parse import urlparse

# Messages that are information, not real warning signs
INFO_MESSAGES = (
    "No URL entered",
    "Could not identify",
    "This text is not a valid URL",
    "No listed warning",
)


def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    # Improvement C: malformed input (for example http://[bad) must not crash
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    # Check 2: very long URL
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # Check 3: IP address as hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    # Check 4: many hostname segments
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    # Check 5: punycode marker
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    # Check 6: plain HTTP
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append("No listed warning signs found. This does NOT prove safety.")

    return findings


def has_warnings(findings):
    """Improvement B helper: True only when the findings are real warnings."""
    return not findings[0].startswith(INFO_MESSAGES)


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    # Improvement A: keep checking URLs until the user quits
    while True:
        try:
            raw_url = input("\nEnter a sample URL (or type q to quit): ")
        except EOFError:
            print("\nGoodbye! Stay alert online.")
            break

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")
        for item in findings:
            print("- " + item)

        # Improvement B: clear summary when real warnings exist
        if has_warnings(findings):
            print("\nREVIEW CAREFULLY: " + str(len(findings)) + " warning sign(s) found.")

        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()

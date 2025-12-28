# Define what “secure” means
# Evaluate headers
# Return structured results

REQUIRED_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def evaluate_headers(headers):
    results = {}

    for header in REQUIRED_HEADERS:
        if header not in headers:
            results[header] = "FAIL"
            continue

        value = headers.get(header, "")

        if header == "Strict-Transport-Security":
            results[header] = "PASS" if "max-age" in value else "WEAK"

        elif header == "X-Content-Type-Options":
            results[header] = "PASS" if value.lower() == "nosniff" else "WEAK"

        else:
            results[header] = "PASS"

    return results

def evaluate_cookies(headers):
    results = []

    cookies = headers.get("Set-Cookie")
    if not cookies:
        return ["[INFO] No Set-Cookie header found"]

    if not isinstance(cookies, list):
        cookies = [cookies]

    for cookie in cookies:
        flags = {
            "Secure": "Secure" in cookie,
            "HttpOnly": "HttpOnly" in cookie,
            "SameSite": "SameSite" in cookie
        }

        for flag, present in flags.items():
            status = "PASS" if present else "FAIL"
            results.append(f"[{status}] Cookie {flag}")

    return results

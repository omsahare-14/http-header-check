
# List of HTTP security headers that represent a baseline web security posture.
# These headers are widely supported, non deprecated, and mitigate common attacks
# such as clickjacking, XSS, SSL stripping, and information leakage.
# This list is intentionally small to avoid scope creep and false confidence.

REQUIRED_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def evaluate_headers(headers):

    '''
    Evaluates the presence and basic correctness of common HTTP security headers.
    
    Parameters:
        headers:
            HTTP response headers returned by the requests library.

    Returns
        dict:
            A mapping of header name to evaluation result.
            Possible values are PASS, FAIL, or WEAK.
    '''

    # Dictionary to store evaluation results for each header.
    results = {}

    # Iterate through each required security header.
    for header in REQUIRED_HEADERS:
        # If the header is completely missing from the response,
        # mark it as FAIL and continue to the next header.
        if header not in headers:
            results[header] = "FAIL"
            continue

        # Safely retrieve the header value.
        # Using .get() avoids KeyError and ensures a default empty string.
        value = headers.get(header, "")

        # Special handling for Strict-Transport-Security.
        # HSTS without a max-age directive is ineffective,
        # so presence alone is not sufficient.
        if header == "Strict-Transport-Security":
            results[header] = "PASS" if "max-age" in value else "WEAK"

        # Special handling for X-Content-Type-Options.
        # The only valid and meaningful value is "nosniff".
        # Any other value is treated as weak configuration.
        elif header == "X-Content-Type-Options":
            results[header] = "PASS" if value.lower() == "nosniff" else "WEAK"

        # For all other headers, presence alone is considered PASS.
        # Directive correctness varies widely and is intentionally
        # out of scope to avoid false confidence.
        else:
            results[header] = "PASS"

    return results

def evaluate_cookies(headers):
    '''
    Evaluates presence of common security flags on cookies.
    
    Parameters:
        headers:
            HTTP response headers returned by the requests library.
    
    Returns:
        list:
            A list of formatted strings representing cookie flag evaluation results.
    '''

    # List to store cookie evaluation results.
    results = []

    # Retrieve the Set-Cookie header from the response.
    cookies = headers.get("Set-Cookie")

    # If no cookies are set, return an informational message.
    # Not all responses are expected to set cookies.
    if not cookies:
        return ["[INFO] No Set-Cookie header found"]

    # Normalize cookies to a list.
    # requests may return a single string or a list of strings.
    if not isinstance(cookies, list):
        cookies = [cookies]

    # Iterate through each cookie string.
    for cookie in cookies:
        # Dictionary mapping security flags to their presence.
        flags = {
            "Secure": "Secure" in cookie,
            "HttpOnly": "HttpOnly" in cookie,
            "SameSite": "SameSite" in cookie
        }

        # For each flag, record whether it is present or missing.
        for flag, present in flags.items():
            # Presence of a flag is PASS.
            # Absence is FAIL.
            status = "PASS" if present else "FAIL"
            results.append(f"[{status}] Cookie {flag}") # Append formatted result string.
    
    # Return all cookie evaluation results.
    return results
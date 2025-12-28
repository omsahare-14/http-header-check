# HTTP Security Headers and Cookie Checker

A simple Python CLI tool that checks common HTTP security headers and cookie flags for a given URL.  
The goal of this project is to validate baseline web security posture and reinforce understanding of how HTTP headers mitigate real world attacks.

---

## What This Tool Does

Given a target URL, the tool:

• Fetches HTTP response headers  
• Checks for presence and basic correctness of common security headers  
• Analyzes cookie flags for session security  
• Produces a clear PASS FAIL WEAK style report  

This is a **baseline checker**, not a full security audit tool.

---

## Security Headers Checked

### Strict-Transport-Security  
Forces browsers to always use HTTPS.  
Helps prevent SSL stripping and downgrade attacks.

### Content-Security-Policy  
Restricts where scripts and other resources can load from.  
Helps mitigate XSS and script injection attacks.

### X-Frame-Options  
Controls whether the site can be embedded in iframes.  
Helps prevent clickjacking attacks.

### X-Content-Type-Options  
Prevents browsers from MIME type sniffing.  
Helps prevent certain XSS attacks caused by incorrect content interpretation.

### Referrer-Policy  
Controls how much referrer information is sent with requests.  
Helps prevent leakage of sensitive URLs and parameters.

### Permissions-Policy  
Restricts access to powerful browser features like camera and microphone.  
Helps limit abuse by malicious scripts.

---

## Cookie Security Checks

The tool also analyzes the `Set-Cookie` header and checks for:

• Secure  
Ensures cookies are only sent over HTTPS.

• HttpOnly  
Prevents JavaScript access to cookies in case of XSS.

• SameSite  
Helps mitigate CSRF attacks.

Only presence is checked. Policy correctness is intentionally out of scope.

---

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py https://example.com
```

## Design Notes

• Evaluates headers even for non 200 responses
• Clearly displays HTTP status code
• Uses minimal validation to avoid false confidence
• Focuses on clarity and learning rather than exhaustive scanning

## Limitations

• Does not validate directive correctness
• Does not analyze TLS configuration
• Does not inspect DOM or runtime behavior

This tool is intended for learning and baseline checks only.

## Why This Project

This project was built to:

• Reinforce understanding of HTTP security headers
• Translate theory into practical tooling
• Practice clean CLI tool design
• Serve as a small but complete portfolio project
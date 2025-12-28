# Fetch headers from a URL
# Handle network errors cleanly
# Return headers or exit with a clear message

import requests

def fetch_headers(url:str):
    try:
        response = requests.get(url, timeout=10)
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None
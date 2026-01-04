
import requests

def fetch_headers(url:str):
    """
    Fetches HTTP response headers for a given URL.

    This function is responsible only for making the HTTP request and
    returning response headers. It does not perform any security analysis
    or output formatting.

    Parameters:
        url (str):
            Target URL to send the HTTP GET request to.

    Returns:
        dict or None:
            Returns a dictionary-like object containing HTTP response headers
            if the request is successful.
            Returns None if a network error or request failure occurs.
    """
    try:
        # Perform an HTTP GET request to the target URL.
        # A timeout is specified to avoid hanging indefinitely on slow
        # or unresponsive hosts.
        response = requests.get(url, timeout=10)

        # Return only the response headers.
        # The headers object behaves like a dictionary and is suitable
        # for direct evaluation by the evaluator module.
        return response.headers
    
    except requests.exceptions.RequestException as e:
        # Catch all request related exceptions including:
        # - Connection errors
        # - Timeouts
        # - Invalid URLs
        # - SSL errors
        # The function prints the error message and returns None,
        # allowing the caller to decide how to handle the failure.
        
        print(f"Error fetching headers: {e}")
        return None
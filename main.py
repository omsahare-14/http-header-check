import sys
from checker.headers import fetch_headers
from checker.evaluator import evaluate_headers, evaluate_cookies
from colorama import Fore, Style, init

# Initialize colorama to enable colored output across platforms.
# autoreset=True ensures colors do not bleed into subsequent prints.
init(autoreset=True)

def color_status(status):
    """
    Applies color formatting to evaluation status strings.

    This function is purely presentational and intentionally kept
    separate from evaluation logic to maintain clean separation
    of concerns.

    Parameters:
        status (str):
            One of PASS, FAIL, WEAK, or INFO.

    Returns:
        str:
            Colored version of the status string suitable for CLI output.
    """
    if status == "PASS":
        return Fore.GREEN + status + Style.RESET_ALL
    if status == "FAIL":
        return Fore.RED + status + Style.RESET_ALL
    if status == "WEAK":
        return Fore.YELLOW + status + Style.RESET_ALL
    
    # Default case for informational messages or unexpected status values.
    return Fore.BLUE + status + Style.RESET_ALL


def main():
    """
    Entry point for the CLI tool.

    Responsible for:
    - Parsing command line arguments
    - Fetching HTTP headers
    - Invoking evaluation logic
    - Formatting and printing results

    This function does not perform any security analysis itself.
    """

    # Ensure exactly one argument (the target URL) is provided.
    # If the argument count is incorrect, display usage and exit.
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)

    # Extract target URL from command line arguments.
    url = sys.argv[1]

    # Fetch HTTP response headers for the target URL.
    headers = fetch_headers(url)

    # If header fetching failed (e.g., network error),
    # exit gracefully without attempting evaluation.
    if headers is None:
        sys.exit(1)

    # Evaluate HTTP security headers.
    results = evaluate_headers(headers)

    # Print target information.
    print(f"\nTarget: {url}\n")

    # Print header evaluation results with colored status indicators.
    for header, status in results.items():
        print(f"[{color_status(status)}] {header}")
    
    # Begin cookie analysis section.
    print("\nCookie Analysis:\n")

    # Evaluate cookie security flags.
    cookie_results = evaluate_cookies(headers)

    # Process each cookie evaluation line.
    for line in cookie_results:
        # If the line follows the expected "[STATUS] message" format,
        # extract the status for colorized output.
        if line.startswith("["):
            status = line.split("]")[0][1:]
            rest = line.split("]")[1].strip()
            print(f"[{color_status(status)}] {rest}")
        # For informational messages or non standard output,
        # print the line as is.
        else:
            print(line)

# Standard Python entry point check.
# Ensures main() runs only when this file is executed directly.
if __name__ == "__main__":
    main()

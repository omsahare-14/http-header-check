import sys
from checker.headers import fetch_headers
from checker.evaluator import evaluate_headers, evaluate_cookies
from colorama import Fore, Style, init

init(autoreset=True)

def color_status(status):
    if status == "PASS":
        return Fore.GREEN + status + Style.RESET_ALL
    if status == "FAIL":
        return Fore.RED + status + Style.RESET_ALL
    if status == "WEAK":
        return Fore.YELLOW + status + Style.RESET_ALL
    return Fore.BLUE + status + Style.RESET_ALL


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    headers = fetch_headers(url)

    if headers is None:
        sys.exit(1)

    results = evaluate_headers(headers)

    print(f"\nTarget: {url}\n")
    for header, status in results.items():
        # print(f"[{status}] {header}")
        print(f"[{color_status(status)}] {header}")
    
    print("\nCookie Analysis:\n")
    cookie_results = evaluate_cookies(headers)

    for line in cookie_results:
        if line.startswith("["):
            status = line.split("]")[0][1:]
            rest = line.split("]")[1].strip()
            print(f"[{color_status(status)}] {rest}")
        else:
            print(line)

if __name__ == "__main__":
    main()

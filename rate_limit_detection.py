import requests

class RateLimitDetection:
    def __init__(self, target_url, headers=None):
        self.target_url = target_url
        self.headers = headers or {}
        self.session = requests.Session()

    def detect_rate_limits(self):
        try:
            response = self.send_request()
            rate_limit_headers = self.extract_rate_limit_headers(response)
            return rate_limit_headers
        except Exception as e:
            print(f"Rate limit detection failed with an exception: {str(e)}")
            return {}

    def send_request(self):
        try:
            response = self.session.get(self.target_url, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed with an exception: {str(e)}")
            return None

    def extract_rate_limit_headers(self, response):
        rate_limit_headers = {}
        if response:
            for header in response.headers:
                if "ratelimit" in header.lower():
                    rate_limit_headers[header] = response.headers[header]
        return rate_limit_headers

if __name__ == "__main__":
    # Configure the target URL and headers as needed
    target_url = "https://api.example.com/endpoint"
    headers = {
        "User-Agent": "Rate-Limit Detection",
    }

    # Initialize the RateLimitDetection
    detector = RateLimitDetection(target_url, headers)

    # Detect and print rate-limiting headers
    rate_limit_headers = detector.detect_rate_limits()
    if rate_limit_headers:
        print("Detected Rate-Limit Headers:")
        for header, value in rate_limit_headers.items():
            print(f"{header}: {value}")
    else:
        print("No rate-limit headers detected.")

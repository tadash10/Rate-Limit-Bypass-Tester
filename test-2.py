import requests
import time

class RateLimitBypassTester:
    def __init__(self, target_url, headers=None):
        self.target_url = target_url
        self.headers = headers or {}
        self.session = requests.Session()

    def bypass_rate_limit(self, num_requests, interval, payload=None):
        try:
            for _ in range(num_requests):
                response = self.send_request(payload)
                if response:
                    print(f"Request {_:>2}/{num_requests}:")
                    print(f"Status Code: {response.status_code}")
                    print(f"Response Content: {response.text}")
                    print("")

                time.sleep(interval)

        except KeyboardInterrupt:
            print("Rate-limit bypass testing interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def send_request(self, payload=None):
        try:
            response = self.session.get(self.target_url, headers=self.headers, params=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

            return response

        except requests.exceptions.RequestException as e:
            print(f"Request failed with an exception: {str(e)}")
            return None

if __name__ == "__main__":
    # Configure the target URL and headers as needed
    target_url = "https://api.example.com/endpoint"
    headers = {
        "User-Agent": "Rate-Limit Bypass Tester",
    }

    # Initialize the RateLimitBypassTester
    tester = RateLimitBypassTester(target_url, headers)

    # Configure the number of requests and time interval between requests
    num_requests = 50  # Adjust as needed
    interval = 1  # Adjust as needed (in seconds)

    # Optional: Define custom payloads if required by the target API
    custom_payload = {
        "param1": "value1",
        "param2": "value2",
    }

    # Simulate bypassing rate limits
    tester.bypass_rate_limit(num_requests, interval, custom_payload)

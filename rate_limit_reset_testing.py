import requests
import time

class RateLimitResetTesting:
    def __init__(self, target_url, headers=None):
        self.target_url = target_url
        self.headers = headers or {}
        self.session = requests.Session()

    def send_request(self, payload=None):
        try:
            response = self.session.get(self.target_url, headers=self.headers, params=payload)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed with an exception: {str(e)}")
            return None

    def test_rate_limit_reset(self, num_requests, reset_interval, payload=None):
        try:
            for _ in range(num_requests):
                response = self.send_request(payload)
                if response:
                    print(f"Request {_:>2}/{num_requests}:")
                    print(f"Status Code: {response.status_code}")
                    print(f"Response Content: {response.text}")
                    print("")
                    if "X-RateLimit-Reset" in response.headers:
                        reset_time = int(response.headers["X-RateLimit-Reset"])
                        print(f"Rate limit reset in {reset_time} seconds.")
                        time.sleep(reset_time)
                else:
                    break  # Stop testing if a request fails

        except KeyboardInterrupt:
            print("Rate limit reset testing interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Configure the target URL and headers as needed
    target_url = "https://api.example.com/endpoint"
    headers = {
        "User-Agent": "Rate Limit Reset Tester",
    }

    # Initialize the RateLimitResetTesting
    tester = RateLimitResetTesting(target_url, headers)

    # Configure the number of requests, reset interval, and optional payload
    num_requests = 50  # Adjust as needed
    reset_interval = 3600  # Rate limit reset interval in seconds
    custom_payload = {
        "param1": "value1",
        "param2": "value2",
    }  # Optional payload

    # Test rate limit reset mechanisms
    tester.test_rate_limit_reset(num_requests, reset_interval, custom_payload)

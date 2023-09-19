import requests

class CustomRateLimitConfiguration:
    def __init__(self, target_url, headers=None, custom_rate_limit_headers=None):
        self.target_url = target_url
        self.headers = headers or {}
        self.custom_rate_limit_headers = custom_rate_limit_headers or {}
        self.session = requests.Session()

    def send_request(self, payload=None):
        try:
            response = self.session.get(self.target_url, headers=self.headers, params=payload)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed with an exception: {str(e)}")
            return None

    def configure_rate_limits(self, num_requests, custom_headers=None, payload=None):
        try:
            for _ in range(num_requests):
                headers = {**self.headers, **custom_headers}
                response = self.send_request(payload)
                if response:
                    print(f"Request {_:>2}/{num_requests}:")
                    print(f"Status Code: {response.status_code}")
                    print(f"Response Content: {response.text}")
                    print("")

        except KeyboardInterrupt:
            print("Custom rate limit configuration testing interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Configure the target URL and headers as needed
    target_url = "https://api.example.com/endpoint"
    headers = {
        "User-Agent": "Custom Rate Limit Configuration Tester",
    }

    # Define custom rate-limit headers as needed
    custom_rate_limit_headers = {
        "X-RateLimit-Limit": "100",
        "X-RateLimit-Remaining": "50",
        "X-RateLimit-Reset": "3600",
    }

    # Initialize the CustomRateLimitConfiguration
    configurator = CustomRateLimitConfiguration(target_url, headers, custom_rate_limit_headers)

    # Configure the number of requests, custom headers, and optional payload
    num_requests = 50  # Adjust as needed
    custom_headers = {
        "X-Custom-Header": "value",
    }  # Custom headers for rate limit configuration
    custom_payload = {
        "param1": "value1",
        "param2": "value2",
    }  # Optional payload

    # Configure custom rate limits
    configurator.configure_rate_limits(num_requests, custom_headers, custom_payload)

import requests
import time

class RateLimitExceedanceDetection:
    def __init__(self, target_url, headers=None):
        self.target_url = target_url
        self.headers = headers or {}
        self.session = requests.Session()
        self.request_count = 0

    def monitor_rate_limit(self, max_requests):
        try:
            while self.request_count < max_requests:
                response = self.send_request()
                if response:
                    self.request_count += 1
                else:
                    break

        except KeyboardInterrupt:
            print("Rate limit exceedance testing interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        print(f"Total requests made: {self.request_count}")
        if self.request_count >= max_requests:
            print("Rate limit exceeded.")
        else:
            print("Rate limit not exceeded.")

    def send_request(self):
        try:
            response = self.session.get(self.target_url, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed with an exception: {str(e)}")
            return None

if __name__ == "__main__":
    # Configure the target URL and headers as needed
    target_url = "https://api.example.com/endpoint"
    headers = {
        "User-Agent": "Rate-Limit Exceedance Detection",
    }

    # Initialize the RateLimitExceedanceDetection
    detector = RateLimitExceedanceDetection(target_url, headers)

    # Configure the maximum number of requests to monitor
    max_requests = 100  # Adjust as needed

    # Monitor rate limit exceedance
    detector.monitor_rate_limit(max_requests)

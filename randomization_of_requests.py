import requests
import random
import time

class RandomizationOfRequests:
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

    def randomize_request_timing(self, num_requests, min_interval, max_interval, payload=None):
        try:
            for _ in range(num_requests):
                response = self.send_request(payload)
                if response:
                    print(f"Request {_:>2}/{num_requests}:")
                    print(f"Status Code: {response.status_code}")
                    print(f"Response Content: {response.text}")
                    print("")

                random_interval = random.uniform(min_interval, max_interval)
                time.sleep(random_interval)

        except KeyboardInterrupt:
            print("Randomized request testing interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Configure the target URL and headers as needed
    target_url = "https://api.example.com/endpoint"
    headers = {
        "User-Agent": "Randomization of Requests",
    }

    # Initialize the RandomizationOfRequests
    randomizer = RandomizationOfRequests(target_url, headers)

    # Configure the number of requests, minimum, and maximum interval
    num_requests = 50  # Adjust as needed
    min_interval = 0.5  # Minimum interval in seconds
    max_interval = 2.0  # Maximum interval in seconds

    # Optional: Define custom payloads if required by the target API
    custom_payload = {
        "param1": "value1",
        "param2": "value2",
    }

    # Randomize request timing
    randomizer.randomize_request_timing(num_requests, min_interval, max_interval, custom_payload)

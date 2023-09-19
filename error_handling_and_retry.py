
import requests
import time

class ErrorHandlingAndRetry:
    def __init__(self, target_url, headers=None):
        self.target_url = target_url
        self.headers = headers or {}
        self.session = requests.Session()
        self.max_retry_attempts = 3

    def send_request(self, payload=None):
        for _ in range(self.max_retry_attempts):
            try:
                response = self.session.get(self.target_url, headers=self.headers, params=payload)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                print(f"Request failed with an exception: {str(e)}")
                print(f"Retrying in 5 seconds...")
                time.sleep(5)

        return None

    def handle_errors_and_retry(self, num_requests, payload=None):
        try:
            for _ in range(num_requests):
                response = self.send_request(payload)
                if response:
                    print(f"Request {_:>2}/{num_requests}:")
                    print(f"Status Code: {response.status_code}")
                    print(f"Response Content: {response.text}")
                    print("")

        except KeyboardInterrupt:
            print("Rate limit bypass testing interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Configure the target URL and headers as needed
    target_url = "https://api.example.com/endpoint"
    headers = {
        "User-Agent": "Error Handling and Retry Tester",
    }

    # Initialize the ErrorHandlingAndRetry
    tester = ErrorHandlingAndRetry(target_url, headers)

    # Configure the number of requests and optional payload
    num_requests = 50  # Adjust as needed
    custom_payload = {
        "param1": "value1",
        "param2": "value2",
    }  # Optional payload

    # Handle errors and retry
    tester.handle_errors_and_retry(num_requests, custom_payload)

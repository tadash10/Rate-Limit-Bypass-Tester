import requests
import concurrent.futures

class ConcurrencyTesting:
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

    def test_concurrency(self, num_requests, max_concurrent_requests, payload=None):
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_concurrent_requests) as executor:
                futures = [executor.submit(self.send_request, payload) for _ in range(num_requests)]

                for future in concurrent.futures.as_completed(futures):
                    response = future.result()
                    if response:
                        print(f"Status Code: {response.status_code}")
                        print(f"Response Content: {response.text}")
                        print("")

        except KeyboardInterrupt:
            print("Concurrency testing interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Configure the target URL and headers as needed
    target_url = "https://api.example.com/endpoint"
    headers = {
        "User-Agent": "Concurrency Tester",
    }

    # Initialize the ConcurrencyTesting
    tester = ConcurrencyTesting(target_url, headers)

    # Configure the number of requests, maximum concurrent requests, and optional payload
    num_requests = 50  # Adjust as needed
    max_concurrent_requests = 10  # Adjust as needed
    custom_payload = {
        "param1": "value1",
        "param2": "value2",
    }  # Optional payload

    # Test concurrency
    tester.test_concurrency(num_requests, max_concurrent_requests, custom_payload)

import requests
import time

class MultiplePayloadsTester:
    def __init__(self, target_url, headers=None):
        self.target_url = target_url
        self.headers = headers or {}
        self.session = requests.Session()

    def test_with_payloads(self, payloads):
        for payload in payloads:
            response = self.send_request(payload)
            if response:
                print(f"Payload: {payload}")
                print(f"Status Code: {response.status_code}")
                print(f"Response Content: {response.text}")
                print("")

    def send_request(self, payload=None):
        try:
            response = self.session.get(self.target_url, headers=self.headers, params=payload)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed with an exception: {str(e)}")
            return None

if __name__ == "__main__":
    # Configure the target URL and headers as needed
    target_url = "https://api.example.com/endpoint"
    headers = {
        "User-Agent": "Multiple Payloads Tester",
    }

    # Initialize the MultiplePayloadsTester
    tester = MultiplePayloadsTester(target_url, headers)

    # Define a list of payloads to test
    payloads = [
        {"param1": "value1"},
        {"param1": "value2"},
        # Add more payloads as needed
    ]

    # Test with multiple payloads
    tester.test_with_payloads(payloads)

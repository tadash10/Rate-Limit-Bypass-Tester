import requests
import time
import logging

class LoggingAndReporting:
    def __init__(self, target_url, headers=None):
        self.target_url = target_url
        self.headers = headers or {}
        self.session = requests.Session()
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger("RateLimitBypassTester")
        logger.setLevel(logging.INFO)

        # Create a file handler and set the log file name
        file_handler = logging.FileHandler("rate_limit_bypass.log")
        file_handler.setLevel(logging.INFO)

        # Create a log format
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(log_format)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        return logger

    def send_request(self, payload=None):
        try:
            response = self.session.get(self.target_url, headers=self.headers, params=payload)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed with an exception: {str(e)}")
            return None

    def log_and_report(self, num_requests, payload=None):
        try:
            for _ in range(num_requests):
                response = self.send_request(payload)
                if response:
                    self.logger.info(f"Request {_:>2}/{num_requests} - Status Code: {response.status_code}")
                else:
                    self.logger.info(f"Request {_:>2}/{num_requests} - Failed")
                time.sleep(1)  # Adjust the delay between requests as needed

        except KeyboardInterrupt:
            self.logger.warning("Testing interrupted by user.")
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Configure the target URL and headers as needed
    target_url = "https://api.example.com/endpoint"
    headers = {
        "User-Agent": "Logging and Reporting Tester",
    }

    # Initialize the LoggingAndReporting
    reporter = LoggingAndReporting(target_url, headers)

    # Configure the number of requests and optional payload
    num_requests = 50  # Adjust as needed
    custom_payload = {
        "param1": "value1",
        "param2": "value2",
    }  # Optional payload

    # Log and report requests
    reporter.log_and_report(num_requests, custom_payload)

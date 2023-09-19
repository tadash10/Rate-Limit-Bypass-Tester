# main_script.py

# Import functions from separate files
from user_friendly_cli_interface import parse_args
from concurrency_testing import concurrency_test
from custom_rate_limit_configuration import custom_rate_limit_test
from error_handling_and_retry import error_handling_and_retry
from logging_and_reporting import log_and_report
from multiple_payloads import multiple_payload_test
from randomization_of_requests import random_request_timing
from rate_limit_detection import rate_limit_detection
from rate_limit_evasion import rate_limit_evasion
from rate_limit_exceedance_detection import rate_limit_exceedance_detection
from rate_limit_reset_testing import rate_limit_reset_test

def main():
    args = parse_args()  # User-friendly CLI interface

    # Perform specific rate-limit testing scenarios based on user-provided options
    if args.scenario == "concurrency":
        concurrency_test(args)
    elif args.scenario == "custom_rate_limit":
        custom_rate_limit_test(args)
    elif args.scenario == "error_handling_retry":
        error_handling_and_retry(args)
    elif args.scenario == "log_and_report":
        log_and_report(args)
    elif args.scenario == "multiple_payloads":
        multiple_payload_test(args)
    elif args.scenario == "random_request_timing":
        random_request_timing(args)
    elif args.scenario == "rate_limit_detection":
        rate_limit_detection(args)
    elif args.scenario == "rate_limit_evasion":
        rate_limit_evasion(args)
    elif args.scenario == "rate_limit_exceedance_detection":
        rate_limit_exceedance_detection(args)
    elif args.scenario == "rate_limit_reset_test":
        rate_limit_reset_test(args)
    else:
        print("Invalid scenario. Please choose a valid scenario.")

if __name__ == "__main__":
    main()

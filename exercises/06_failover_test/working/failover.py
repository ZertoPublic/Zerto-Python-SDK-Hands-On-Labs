#!/usr/bin/env python3
"""
Exercise 6: Failover Testing - Solution
This script demonstrates how to perform a failover test on a VPG.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

Usage:
    python failover.py --vpg-name "My-VPG"

This solution demonstrates:
- Finding a VPG by name
- Starting a failover test with default settings
- Monitoring test progress
- Stopping the test when requested
"""

import sys
import os
import logging
import json
import argparse
import time
from pathlib import Path
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Add prerequisites to Python path
prerequisites_path = Path(__file__).parent.parent.parent.parent / "prerequisites"
sys.path.append(str(prerequisites_path))

# Import the SDK modules
from zvml import ZVMLClient

# Import configuration
try:
    from config import (
        ZVM_HOST,
        ZVM_PORT,
        ZVM_SSL_VERIFY,
        CLIENT_ID,
        CLIENT_SECRET
    )
except ImportError:
    print("Error: Please copy config.example.py to config.py and update with your values")
    print("Expected path:", prerequisites_path / "config.py")
    sys.exit(1)

def main():
    """
    Main function to demonstrate failover testing.
    """
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    try:
        # Step 1: Parse command line arguments
        # TODO: Add code to get sites and site identifiers
        # HINT: Use this syntax:
        # parser = argparse.ArgumentParser(description='Perform failover test on a VPG')
        # parser.add_argument('--vpg-name', required=True,
        #                 help='Name of the VPG to test')
        # args = parser.parse_args()
        # ← ADD YOUR CODE HERE

        # Step 2: Create ZVMLClient instance
        # TODO: Add code to get sites and site identifiers
        # HINT: Use this syntax:
        logging.info(f"Initializing ZVMLClient for ZVM at {ZVM_HOST}")
        # client = ZVMLClient(
        #     zvm_address=ZVM_HOST,
        #     client_id=CLIENT_ID,
        #     client_secret=CLIENT_SECRET,
        #     verify_certificate=ZVM_SSL_VERIFY
        # )
        # ← ADD YOUR CODE HERE

        # Step 3: Start the test with default settings
        # TODO: Add code to get sites and site identifiers
        # HINT: Use this syntax:
        # response = client.vpgs.failover_test(vpg_name=args.vpg_name, sync=True)    
        # logging.info(f"Faiolver test response: {response}")
         # ← ADD YOUR CODE HERE
       
        # Step 4: Handle test stop request
        # TODO: Add code to get sites and site identifiers
        # HINT: Use this syntax:
        # response = input("\nWould you like to stop the test? (yes/no): ").lower()
        # if response in ['yes', 'y']:
        #     logging.info(f"Stopping faiolver test for VPG '{args.vpg_name}'...")
        #     response = client.vpgs.stop_failover_test(vpg_name=args.vpg_name)
        #     logging.info(f"Stop failover test response: {response}")
        # ← ADD YOUR CODE HERE

    except Exception as e:
        logging.error(f"Failover test failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
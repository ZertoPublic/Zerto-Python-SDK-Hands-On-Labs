#!/usr/bin/env python3
"""
Exercise 6: Failover Testing - Template
This script demonstrates how to perform a failover test on a VPG.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

Usage:
    python failover.py --vpg-name "My-VPG"

Your task:
1. Implement VPG lookup by name using get_vpgs()
2. Start a failover test using failover_test() method
3. Monitor test progress using get_vpg_test_status()
4. Stop the test using stop_vpg_test() method when requested

The script should:
- Find the VPG by name and verify it exists
- Start a failover test with default settings
- Monitor the test progress and status
- Allow stopping the test when requested
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

def parse_arguments():
    """Parse command line arguments."""
    # TODO: Implement argument parsing
    # Required argument:
    # --vpg-name: Name of the VPG to test
    pass

def find_vpg_by_name(client, vpg_name):
    """
    Find a VPG by its name using get_vpgs() method.
    
    Args:
        client: ZVMLClient instance
        vpg_name: Name of the VPG to find
        
    Returns:
        dict: VPG object if found, None otherwise
        
    TODO: Implement the function to:
    1. Call client.vpgs.get_vpgs() to get all VPGs
    2. Find the VPG with matching name
    3. Log the VPG details if found
    4. Return the VPG object or None
    """
    pass

def start_failover_test(client, vpg_name):
    """
    Start a failover test for the specified VPG using failover_test() method.
    
    Args:
        client: ZVMLClient instance
        vpg_name: Name of the VPG to test
        
    Returns:
        str: Test identifier (task_id)
        
    TODO: Implement the function to:
    1. Call client.vpgs.failover_test() with sync=True
    2. Log the test initiation
    3. Return the task_id
    """
    pass

def monitor_test_progress(client, vpg_name, test_id):
    """
    Monitor the progress of a failover test using get_vpg_test_status().
    
    Args:
        client: ZVMLClient instance
        vpg_name: Name of the VPG
        test_id: Test identifier (task_id)
        
    Returns:
        bool: True if test completed successfully, False otherwise
        
    TODO: Implement the function to:
    1. Call client.vpgs.get_vpg_test_status() to get test status
    2. Log the status and progress
    3. Return True for 'Succeeded', False for 'Failed' or 'Stopped'
    4. Return False if test is still running
    """
    pass

def stop_failover_test(client, vpg_name, test_id):
    """
    Stop a running failover test using stop_vpg_test() method.
    
    Args:
        client: ZVMLClient instance
        vpg_name: Name of the VPG
        test_id: Test identifier (task_id)
        
    TODO: Implement the function to:
    1. Call client.vpgs.stop_vpg_test() with sync=True
    2. Wait for the stop operation to complete
    3. Log the stop operation status
    """
    pass

def main():
    """
    Main function to demonstrate failover testing.
    
    TODO: Implement the following steps:
    1. Parse command line arguments for VPG name
    2. Create ZVMLClient instance
    3. Find the VPG by name using find_vpg_by_name()
    4. Start failover test using start_failover_test()
    5. Monitor test progress and handle stop request:
       - Monitor progress using monitor_test_progress()
       - If test completes successfully, exit
       - If user requests to stop, call stop_failover_test()
    """
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    try:
        # TODO: Step 1: Parse command line arguments
        # args = parse_arguments()
        
        # TODO: Step 2: Create ZVMLClient instance
        # client = ZVMLClient(...)
        
        # TODO: Step 3: Find the VPG
        # vpg = find_vpg_by_name(client, args.vpg_name)
        # if not vpg:
        #     logging.error(f"VPG '{args.vpg_name}' not found!")
        #     sys.exit(1)
        
        # TODO: Step 4: Start failover test
        # test_id = start_failover_test(client, args.vpg_name)
        
        # TODO: Step 5: Monitor test progress and handle stop request
        # while True:
        #     success = monitor_test_progress(client, args.vpg_name, test_id)
        #     if success:
        #         logging.info("Test completed successfully")
        #         break
        #     
        #     # Check if user wants to stop the test
        #     response = input("\nWould you like to stop the test? (yes/no): ").lower()
        #     if response in ['yes', 'y']:
        #         stop_failover_test(client, args.vpg_name, test_id)
        #         break
        #     
        #     time.sleep(10)  # Wait before next status check
        
    except Exception as e:
        logging.error(f"Failover test failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
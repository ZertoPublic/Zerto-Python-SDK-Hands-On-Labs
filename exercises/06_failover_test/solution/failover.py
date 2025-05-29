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

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Perform failover test on a VPG')
    parser.add_argument('--vpg-name', required=True,
                      help='Name of the VPG to test')
    return parser.parse_args()

def find_vpg_by_name(client, vpg_name):
    """
    Find a VPG by its name.
    
    Args:
        client: ZVMLClient instance
        vpg_name: Name of the VPG to find
        
    Returns:
        dict: VPG object if found, None otherwise
    """
    vpg = client.vpgs.list_vpgs(vpg_name=vpg_name)
    # logging.info(f"Found vpg {json.dumps(vpg, indent=4)}")
    return vpg if vpg else None

def start_failover_test(client, vpg_name):
    """
    Start a failover test for the specified VPG using default settings.
    
    Args:
        client: ZVMLClient instance
        vpg_name: Name of the VPG to test
        
    Returns:
        str: Test identifier
    """
    logging.info(f"Starting failover test for VPG '{vpg_name}'")
    
    # Start the test with default settings
    response = client.vpgs.failover_test(
        vpg_name=vpg_name,
        sync=True  # Wait for the test to start
    )
    
    logging.info(f"Faiolver test response: {response}")
    return response

def monitor_test_progress(client, vpg_name, test_id):
    """
    Monitor the progress of a failover test.
    
    Args:
        client: ZVMLClient instance
        vpg_name: Name of the VPG
        test_id: Test identifier
        
    Returns:
        bool: True if test completed successfully, False otherwise
    """
    test_status = client.vpgs.get_vpg_test_status(vpg_name, test_id)
    status = test_status.get('Status')
    progress = test_status.get('Progress', 0)
    
    logging.info(f"Test status: {status} (Progress: {progress}%)")
    
    if status == 'Succeeded':
        return True
    elif status in ['Failed', 'Stopped']:
        logging.error(f"Test {status.lower()}: {test_status.get('Message', 'No message')}")
        return False
    
    return False  # Test is still running

def stop_failover_test(client, vpg_name):
    """
    Stop a running failover test.
    
    Args:
        client: ZVMLClient instance
        vpg_name: Name of the VPG
    """
    logging.info(f"Stopping faiolver test for VPG '{vpg_name}'...")
    response = client.vpgs.stop_failover_test(vpg_name=vpg_name)

    logging.info(f"Stop failover test response: {response}")

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
        args = parse_arguments()
        
        # Step 2: Create ZVMLClient instance
        logging.info(f"Initializing ZVMLClient for ZVM at {ZVM_HOST}")
        client = ZVMLClient(
            zvm_address=ZVM_HOST,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            verify_certificate=ZVM_SSL_VERIFY
        )
        
        # Step 3: Find the VPG
        vpg = find_vpg_by_name(client, args.vpg_name)
        if not vpg:
            logging.error(f"VPG '{args.vpg_name}' not found!")
            sys.exit(1)
        
        # Step 4: Start failover test
        response = start_failover_test(client, args.vpg_name)
        
        # Step 5: Handle test stop request
        response = input("\nWould you like to stop the test? (yes/no): ").lower()
        if response in ['yes', 'y']:
            stop_failover_test(client, args.vpg_name)
        
    except Exception as e:
        logging.error(f"Failover test failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
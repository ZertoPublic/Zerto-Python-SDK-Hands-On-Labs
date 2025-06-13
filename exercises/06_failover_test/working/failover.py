#!/usr/bin/env python3
"""
Exercise 6: Failover Testing - Beginner-Friendly Instructions
This script demonstrates how to perform a failover test on a VPG.

PREREQUISITES (Complete these first):
1. ✅ Completed Exercise 5 (VPG Operations)
2. ✅ Make sure you have the zvml package installed
3. ✅ Updated prerequisites/config.py with your ZVM details
4. ✅ Have a VPG created and running (from Exercise 5)

WHAT YOU NEED TO DO:
In this exercise, you will:
1. Create a ZVMLClient to connect to your ZVM
2. Parse command line arguments (VPG name)
3. Find a VPG by its name
4. Start a failover test on the VPG
5. Monitor the test progress
6. Optionally stop the test

STEP-BY-STEP INSTRUCTIONS:
1. Look at the TODO comments below - they tell you exactly what to do
2. Replace the placeholder code with the actual code
3. Each step has hints and examples to help you
4. If you get stuck, check the solution file in the solution/ directory

WHAT IS A FAILOVER TEST?
- **Failover Test**: Tests if your VMs can be successfully started at the recovery site
- It creates test VMs at the peer site to verify everything works
- The test VMs are isolated and don't affect production
- You can stop the test at any time to clean up the test VMs

USAGE EXAMPLE:
python failover.py --vpg-name "My-VPG"
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

# Add prerequisites to Python path (this helps Python find your config file)
prerequisites_path = Path(__file__).parent.parent.parent.parent / "prerequisites"
sys.path.append(str(prerequisites_path))

# Import the Zerto SDK - this gives us the ZVMLClient class
from zvml import ZVMLClient

# Import your configuration settings
try:
    from config import (
        ZVM_HOST,        # Your ZVM IP address (e.g., "192.168.1.100")
        ZVM_PORT,        # Usually 443 for HTTPS
        ZVM_SSL_VERIFY,  # True/False for SSL certificate verification
        CLIENT_ID,       # Your Keycloak client ID (e.g., "my-api-client")
        CLIENT_SECRET    # Your Keycloak client secret
    )
except ImportError:
    print("❌ ERROR: Configuration file not found!")
    print("Please copy config.example.py to config.py and update with your values")
    print("Expected path:", prerequisites_path / "config.py")
    sys.exit(1)

def parse_arguments():
    """
    Parse command line arguments.
    
    TODO: Implement argument parsing
    HINT: Use this syntax:
    parser = argparse.ArgumentParser(description='Perform failover test on a VPG')
    parser.add_argument('--vpg-name', required=True,
                      help='Name of the VPG to test')
    return parser.parse_args()
    
    EXPLANATION:
    - argparse helps you get command line arguments
    - --vpg-name: Name of the VPG to test (required)
    """
    pass  # ← REPLACE WITH YOUR CODE

def find_vpg_by_name(client, vpg_name):
    """
    Find a VPG by its name.
    
    TODO: Implement the function to find a VPG by name
    HINT: Use this syntax:
    vpg = client.vpgs.list_vpgs(vpg_name=vpg_name)
    return vpg if vpg else None
    
    EXPLANATION:
    - client.vpgs.list_vpgs() gets VPGs with a specific name
    - Returns the VPG if found, None if not found
    """
    pass  # ← REPLACE WITH YOUR CODE

def start_failover_test(client, vpg_name):
    """
    Start a failover test for the specified VPG.
    
    TODO: Implement the function to start a failover test
    HINT: Use this syntax:
    response = client.vpgs.failover_test(
        vpg_name=vpg_name,
        sync=True  # Wait for the test to start
    )
    return response
    
    EXPLANATION:
    - client.vpgs.failover_test() starts a failover test
    - sync=True means wait for the test to start before returning
    - Returns the response from the API
    """
    pass  # ← REPLACE WITH YOUR CODE

def monitor_test_progress(client, vpg_name, test_id):
    """
    Monitor the progress of a failover test.
    
    TODO: Implement the function to monitor test progress
    HINT: Use this syntax:
    test_status = client.vpgs.get_vpg_test_status(vpg_name, test_id)
    status = test_status.get('Status')
    progress = test_status.get('Progress', 0)
    
    logging.info(f"Test status: {status} (Progress: {progress}%)")
    
    if status == 'Succeeded':
        return True
    elif status in ['Failed', 'Stopped']:
        return False
    
    return False  # Test is still running
    
    EXPLANATION:
    - client.vpgs.get_vpg_test_status() gets the current test status
    - Returns True if test succeeded, False if failed/stopped/still running
    """
    pass  # ← REPLACE WITH YOUR CODE

def stop_failover_test(client, vpg_name):
    """
    Stop a running failover test.
    
    TODO: Implement the function to stop a failover test
    HINT: Use this syntax:
    response = client.vpgs.stop_failover_test(vpg_name=vpg_name)
    
    EXPLANATION:
    - client.vpgs.stop_failover_test() stops the running test
    - This cleans up the test VMs at the recovery site
    """
    pass  # ← REPLACE WITH YOUR CODE

def main():
    """
    Main function - this is where your code goes!
    Follow the step-by-step instructions below.
    """
    # Set up logging so you can see what's happening
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    print("🚀 Starting Zerto Failover Testing Exercise")
    print("=" * 50)
    
    try:
        # ========================================
        # STEP 1: Parse command line arguments
        # ========================================
        print("\n📝 STEP 1: Parsing command line arguments...")
        print("You need to call the parse_arguments() function you created above.")
        
        # TODO: Add code to parse arguments
        # HINT: Use this syntax:
        # args = parse_arguments()
        # 
        # EXPLANATION:
        # This gets the VPG name from command line
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 2: Create ZVMLClient instance
        # ========================================
        print("\n📝 STEP 2: Creating ZVMLClient...")
        print("This is the same as previous exercises.")
        
        # TODO: Add code to create ZVMLClient
        # HINT: Use this syntax:
        # client = ZVMLClient(
        #     zvm_address=ZVM_HOST,
        #     client_id=CLIENT_ID,
        #     client_secret=CLIENT_SECRET,
        #     verify_certificate=ZVM_SSL_VERIFY
        # )
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 3: Find the VPG
        # ========================================
        print("\n📝 STEP 3: Finding the VPG...")
        print("You need to find the VPG by its name.")
        
        # TODO: Add code to find VPG
        # HINT: Use this syntax:
        # vpg = find_vpg_by_name(client, args.vpg_name)
        # if not vpg:
        #     logging.error(f"VPG '{args.vpg_name}' not found!")
        #     sys.exit(1)
        # 
        # EXPLANATION:
        # This checks if the VPG exists before trying to test it
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 4: Start failover test
        # ========================================
        print("\n📝 STEP 4: Starting failover test...")
        print("You need to start a failover test on the VPG.")
        
        # TODO: Add code to start failover test
        # HINT: Use this syntax:
        # response = start_failover_test(client, args.vpg_name)
        # 
        # EXPLANATION:
        # This starts the failover test and waits for it to begin
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 5: Handle test stop request
        # ========================================
        print("\n📝 STEP 5: Handling test stop request...")
        print("You can optionally stop the test.")
        
        # TODO: Add code for interactive test stopping
        # HINT: Use this syntax:
        # response = input("\nWould you like to stop the test? (yes/no): ").lower()
        # if response in ['yes', 'y']:
        #     stop_failover_test(client, args.vpg_name)
        # 
        # EXPLANATION:
        # This asks the user if they want to stop the test and cleans up if yes
        
        # ← ADD YOUR CODE HERE
        
    except Exception as e:
        # This catches any errors that might occur
        print(f"\n❌ ERROR: Something went wrong!")
        print(f"Error details: {str(e)}")
        logging.error(f"Failover test failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Exercise 2: Authentication - Beginner-Friendly Instructions
This script demonstrates how to authenticate with Zerto API using Keycloak.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

3. Update prerequisites/config.py with your ZVM details:
   - ZVM_HOST: Your Zerto Virtual Manager IP address or hostname
   - CLIENT_ID: Your Keycloak client ID
   - CLIENT_SECRET: Your Keycloak client secret

WHAT YOU NEED TO DO:
In this exercise, you will:
1. Create a ZVMLClient object to connect to your ZVM
2. Test the connection by getting information about your local site
3. Handle any errors that might occur

STEP-BY-STEP INSTRUCTIONS:
1. Look at the TODO comments below - they tell you exactly what to do
2. Replace the placeholder code with the actual code
3. Each step has hints and examples to help you
4. If you get stuck, check the solution file in the solution/ directory

WHAT IS A ZVMLClient?
- It's like a "remote control" for your Zerto Virtual Manager
- It handles all the communication with your ZVM
- You need to give it your ZVM address and login credentials
"""

import sys
import os
import logging
import json
from pathlib import Path
import urllib3

# Add prerequisites to Python path
prerequisites_path = Path(__file__).parent.parent.parent.parent / "prerequisites"
sys.path.append(str(prerequisites_path))

# Import the SDK modules
from zvml import ZVMLClient

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Import configuration
try:
    from config import (
        ZVM_HOST,        # Your ZVM IP address (e.g., "192.168.1.100")
        ZVM_PORT,        # Usually 443 for HTTPS
        ZVM_SSL_VERIFY,  # True/False for SSL certificate verification
        CLIENT_ID,       # Your Keycloak client ID (e.g., "my-api-client")
        CLIENT_SECRET    # Your Keycloak client secret
    )
except ImportError:
    print("Error: Please copy config.example.py to config.py and update with your values")
    print("Expected path:", prerequisites_path / "config.py")
    sys.exit(1)

def main():
    """
    Main function to demonstrate Zerto authentication.
    Shows how to:
    1. Initialize ZVMLClient with Keycloak credentials
    2. Test connection by retrieving local site info
    3. Handle authentication and connection errors
    """
    # Set up logging with timestamp
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    try:
        # ========================================
        # STEP 1: Create a ZVMLClient instance
        # ========================================
        print("\n📝 STEP 1: Creating ZVMLClient...")
        print("You need to replace the line 'client = None' with actual code.")
        print("Look at the hint below for the correct syntax.")
        
        # TODO: Replace this line with actual ZVMLClient creation
        # HINT: Use this syntax:
        # client = ZVMLClient(
        #     zvm_address=ZVM_HOST,
        #     client_id=CLIENT_ID,
        #     client_secret=CLIENT_SECRET,
        #     verify_certificate=ZVM_SSL_VERIFY
        # )
        # logging.info("Testing connection by retrieving local site information...")
        # 
        # EXPLANATION:
        # - zvm_address: Where your ZVM is located (from config.py)
        # - client_id: Your Keycloak client ID (from config.py)
        # - client_secret: Your Keycloak client secret (from config.py)
        # - verify_certificate: Whether to check SSL certificates (from config.py)

        # ← ADD YOUR CODE HERE

        # ========================================
        # STEP 2: Test the connection
        # ========================================
        print("\n📝 STEP 2: Testing connection...")
        print("You need to test if the connection works by getting local site info.")
        print("Look at the hint below for the correct syntax.")
        
        # TODO: Add code to test the connection
        # HINT: Use this syntax:
        # local_site = client.localsite.get_local_site()
        # version = local_site.get('Version')
        # logging.info(f"Successfully connected to ZVM version: {version}")
        # 
        # EXPLANATION:
        # - client.localsite.get_local_site() gets information about your local ZVM
        # - local_site.get('Version') extracts the ZVM version from the response
        # - logging.info() displays a success message
        
        # ← ADD YOUR CODE HERE
        
    except Exception as e:
        # This catches any errors that might occur
        logging.error(f"Authentication failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Exercise 2: Authentication
This script demonstrates how to authenticate with Zerto API using Keycloak.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

Your task:
1. Initialize ZVMLClient with Keycloak credentials
2. Test connection by retrieving local site information
3. Handle authentication and connection errors

If you need help, check the solution in the solution directory.
"""

import sys
import os
import logging
import json
from pathlib import Path

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
    Main function to demonstrate Zerto authentication.
    Complete the following steps:
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
        # Step 1: Create a ZVMLClient instance
        # TODO: Initialize the ZVMLClient with your ZVM host and credentials
        # Hint: Use ZVMLClient(zvm_address=ZVM_HOST, client_id=CLIENT_ID, 
        #       client_secret=CLIENT_SECRET, verify_certificate=ZVM_SSL_VERIFY)
        client = None  # Replace with actual client initialization
        
        # Step 2: Test the connection
        # TODO: Try to get local site information to verify the connection
        # Hint: Use client.localsite.get_local_site() and extract the Version
        # Hint: Log the version using logging.info()
        pass  # Replace with actual connection test
        
        # Step 3: Print connection status
        # TODO: Display whether the connection was successful
        # Hint: Use logging.info() to show the status
        
    except Exception as e:
        # TODO: Handle any authentication or connection errors
        # Hint: Use logging.error() to log the error message
        logging.error(f"Authentication failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
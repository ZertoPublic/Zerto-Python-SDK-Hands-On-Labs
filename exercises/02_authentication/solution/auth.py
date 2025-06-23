#!/usr/bin/env python3
"""
Exercise 2: Authentication - Solution
This script demonstrates how to authenticate with Zerto API using Keycloak.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

This solution demonstrates:
- ZVMLClient initialization with Keycloak authentication
- Connection testing using local site information
- Proper error handling and logging
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
        # Step 1: Create a ZVMLClient instance
        logging.info(f"Initializing ZVMLClient for ZVM at {ZVM_HOST}")
        client = ZVMLClient(
            zvm_address=ZVM_HOST,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            verify_certificate=ZVM_SSL_VERIFY
        )
        
        # Step 2: Test the connection by getting local site info
        logging.info("Testing connection by retrieving local site information...")
        
        # Extract and log version information
        local_site = client.localsite.get_local_site()
        version = local_site.get('Version')
        logging.info(f"Successfully connected to ZVM version: {version}")
        
        # Optional: Log additional site details if needed
        # logging.debug(f"Full site details: {json.dumps(local_site, indent=2)}")
        
        # Step 3: Print final connection status
        logging.info("Connection successful!")
        
    except Exception as e:
        logging.error(f"Authentication failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
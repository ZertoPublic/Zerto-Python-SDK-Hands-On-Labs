#!/usr/bin/env python3
"""
Exercise 3: Site Discovery
This script demonstrates how to discover and work with Zerto virtualization sites.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

Your task:
1. List all available virtualization sites
2. Get and display local site information

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
    Main function to demonstrate site discovery.
    Complete the following steps:
    1. List all available virtualization sites
    2. Get and display local site information
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
        
        # Step 2: List all available sites
        # TODO: Get the list of virtualization sites
        # Hint: Use client.virtualization_sites.get_virtualization_sites()
        # Hint: Log the number of sites found and their details using json.dumps()
        pass  # Replace with actual site listing
        
        # Step 3: Get and display local site information
        # TODO: Get and display local site information
        # Hint: Use client.localsite.get_local_site()
        # Hint: Log the local site details using json.dumps()
        pass  # Replace with actual local site retrieval
        
    except Exception as e:
        # TODO: Handle any site discovery errors
        # Hint: Use logging.error() to log the error message
        logging.error(f"Site discovery failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
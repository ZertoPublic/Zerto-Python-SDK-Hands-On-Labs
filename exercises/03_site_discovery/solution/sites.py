#!/usr/bin/env python3
"""
Exercise 3: Site Discovery - Solution
This script demonstrates how to discover and work with Zerto virtualization sites.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

This solution demonstrates:
- Listing all available virtualization sites
- Retrieving and displaying local site information
- Proper error handling and logging
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
    Shows how to:
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
        logging.info(f"Initializing ZVMLClient for ZVM at {ZVM_HOST}")
        client = ZVMLClient(
            zvm_address=ZVM_HOST,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            verify_certificate=ZVM_SSL_VERIFY
        )
        
        # Step 2: List all available sites
        logging.info("Retrieving list of available sites...")
        sites = client.virtualization_sites.get_virtualization_sites()
        
        if not sites:
            logging.warning("No sites found!")
        else:
            logging.info(f"Found {len(sites)} site(s):")
            logging.info(f'Sites Info: {json.dumps(sites, indent=4)}')
        
        # Step 3: Get and display local site information
        logging.info("\nRetrieving local site information...")
        local_site = client.localsite.get_local_site()
        logging.info(f"Local site details: {json.dumps(local_site, indent=4)}")
        
    except Exception as e:
        logging.error(f"Site discovery failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
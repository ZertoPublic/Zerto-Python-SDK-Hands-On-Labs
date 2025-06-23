#!/usr/bin/env python3
"""
Exercise 3: Site Discovery - Beginner-Friendly Instructions
This script demonstrates how to discover and work with Zerto virtualization sites.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

WHAT YOU NEED TO DO:
In this exercise, you will:
1. Create a ZVMLClient to connect to your ZVM (same as Exercise 2)
2. Get a list of all available virtualization sites
3. Get detailed information about your local site

STEP-BY-STEP INSTRUCTIONS:
1. Look at the TODO comments below - they tell you exactly what to do
2. Replace the placeholder code with the actual code
3. Each step has hints and examples to help you
4. If you get stuck, check the solution file in the solution/ directory

WHAT ARE VIRTUALIZATION SITES?
- A "site" in Zerto is a location where you have virtual machines
- Your "local site" is where your ZVM is running
- "Peer sites" are other locations you can replicate to/from
- Each site has information like name, type, version, etc.
"""

import sys
import os
import logging
import json
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
        # ========================================
        # STEP 1: Create a ZVMLClient instance
        # ========================================
        print("\n📝 STEP 1: Creating ZVMLClient...")
        print("This is the same as Exercise 2 - you need to create a client to connect to ZVM.")
        
        # TODO: Replace this line with actual ZVMLClient creation
        # HINT: Use this syntax (same as Exercise 2):
        # client = ZVMLClient(
        #     zvm_address=ZVM_HOST,
        #     client_id=CLIENT_ID,
        #     client_secret=CLIENT_SECRET,
        #     verify_certificate=ZVM_SSL_VERIFY
        # )
        # 
        # EXPLANATION:
        # This creates a connection to your ZVM (same as Exercise 2)
        
        # ← ADD YOUR CODE HERE
       
        # ========================================
        # STEP 2: List all available sites
        # ========================================
        print("\n📝 STEP 2: Getting list of sites...")
        print("You need to get a list of all virtualization sites available to your ZVM.")
        
        # TODO: Add code to get the list of sites
        # HINT: Use this syntax:
        # sites = client.virtualization_sites.get_virtualization_sites()
        # logging.info(f"Sites Info: {json.dumps(sites, indent=4)}")
        # 
        # EXPLANATION:
        # - client.virtualization_sites.get_virtualization_sites() gets all sites
        # - This returns a list of site information
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 3: Get local site information
        # ========================================
        # TODO: Add code to get local site information
        # HINT: Use this syntax:
        # local_site = client.localsite.get_local_site()
        # logging.info(f"Local site details: {json.dumps(local_site, indent=4)}")
        # 
        # EXPLANATION:
        # - client.localsite.get_local_site() gets info about your local ZVM
        # - This includes version, name, type, and other details
        # - json.dumps(local_site, indent=4) formats it nicely
        
        # ← ADD YOUR CODE HERE
        
    except Exception as e:
        logging.error(f"Site discovery failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
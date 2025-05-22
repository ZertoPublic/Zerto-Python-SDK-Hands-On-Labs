#!/usr/bin/env python3
"""
Exercise 4: Resource Discovery
This script demonstrates how to discover and work with resources in your Zerto environment.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

Your task:
1. Discover local site resources (VMs)
2. Work with peer site resources (datastores, hosts, folders, networks)

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
    Main function to demonstrate resource discovery.
    Complete the following steps:
    1. Discover local site resources (VMs)
    2. Work with peer site resources (datastores, hosts, folders, networks)
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
        
        # Step 2: Identify local and peer sites
        # Step 2.1: List all available sites
        # TODO: Get the list of available sites
        # Hint: Use client.virtualization_sites.get_virtualization_sites()
        # Hint: Log the number of sites found and their details using json.dumps()
        pass  # Replace with actual site listing
        
        # Step 2.2: Get local and peer site identifiers
        # TODO: Get local site identifier
        # Hint: Use client.localsite.get_local_site()
        # Hint: Extract the SiteIdentifier from the response
        local_site_identifier = None  # Replace with actual local site identifier
        
        # TODO: Get peer site identifier
        # Hint: Find the first site that is not the local site
        # Hint: Extract the SiteIdentifier from that site
        peer_site_identifier = None  # Replace with actual peer site identifier
        
        # Step 3: Get local site resources
        # Step 3.1: Get local site VMs
        # TODO: Get VMs for the local site
        # Hint: Use client.virtualization_sites.get_virtualization_site_vms()
        # Hint: Pass the local_site_identifier as site_identifier parameter
        # Hint: Log the VMs information using json.dumps()
        pass  # Replace with actual VM retrieval
        
        # Step 3.2: Get peer site datastores
        # TODO: Get datastores for the peer site
        # Hint: Use client.virtualization_sites.get_virtualization_site_datastores()
        # Hint: Pass the peer_site_identifier as site_identifier parameter
        # Hint: Log the datastores information using json.dumps()
        pass  # Replace with actual datastore retrieval
        
        # Step 3.3: Get peer site hosts
        # TODO: Get hosts for the peer site
        # Hint: Use client.virtualization_sites.get_virtualization_site_hosts()
        # Hint: Pass the peer_site_identifier as site_identifier parameter
        # Hint: Log the hosts information using json.dumps()
        pass  # Replace with actual host retrieval
        
        # Step 3.4: Get peer site folders
        # TODO: Get folders for the peer site
        # Hint: Use client.virtualization_sites.get_virtualization_site_folders()
        # Hint: Pass the peer_site_identifier as site_identifier parameter
        # Hint: Log the folders information using json.dumps()
        pass  # Replace with actual folder retrieval
        
        # Step 3.5: Get peer site networks
        # TODO: Get networks for the peer site
        # Hint: Use client.virtualization_sites.get_virtualization_site_networks()
        # Hint: Pass the peer_site_identifier as site_identifier parameter
        # Hint: Log the networks information using json.dumps()
        pass  # Replace with actual network retrieval
        
    except Exception as e:
        # TODO: Handle any resource discovery errors
        # Hint: Use logging.error() to log the error message
        logging.error(f"Resource discovery failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Exercise 4: Resource Discovery - Solution
This script demonstrates how to discover and work with resources in your Zerto environment.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

This solution demonstrates:
- Discovering local site resources (clusters, hosts, datastores)
- Working with peer site resources
- Proper error handling and logging
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
    Shows how to:
    1. Discover local site resources
    2. Work with peer site resources
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
        
        # Step 2: Identify local and peer sites
        # Step 2.1: List all available sites
        logging.info("Retrieving list of available sites...")
        sites = client.virtualization_sites.get_virtualization_sites()
        logging.info(f"Sites: {json.dumps(sites, indent=4)}")
        
        # Step 2.2: Get local and peer site Identifiers
        local_site_identifier = client.localsite.get_local_site().get('SiteIdentifier')
        logging.info(f"Local site identifier: {local_site_identifier}")
        
        # Get peer site identifier (first non-local site)
        peer_site = next((site for site in sites if site.get('SiteIdentifier') != local_site_identifier), None)
            
        peer_site_identifier = peer_site.get('SiteIdentifier')
        logging.info(f"Peer site identifier: {peer_site_identifier}")


        # Step 3: Get local site resources
        # Step 3: Get local site vms
        local_vms = client.virtualization_sites.get_virtualization_site_vms(site_identifier=local_site_identifier)
        logging.info(f"Local Vms Info: {json.dumps(local_vms, indent=4)}")

        peer_datastores = client.virtualization_sites.get_virtualization_site_datastores(site_identifier=peer_site_identifier)
        logging.info(f"Peer Datastores Info: {json.dumps(peer_datastores, indent=4)}")

        # Step 3.3: Get peer site hosts
        peer_hosts = client.virtualization_sites.get_virtualization_site_hosts(site_identifier=peer_site_identifier)
        logging.info(f"Peer Hosts Info: {json.dumps(peer_hosts, indent=4)}")

        # Step 3.4: Get peer site folders
        peer_folders = client.virtualization_sites.get_virtualization_site_folders(site_identifier=peer_site_identifier)
        logging.info(f"Peer Folders Info: {json.dumps(peer_folders, indent=4)}")

        # Step 3.5: Get peer site networks  
        peer_networks = client.virtualization_sites.get_virtualization_site_networks(site_identifier=peer_site_identifier)
        logging.info(f"Peer Networks Info: {json.dumps(peer_networks, indent=4)}")

    except Exception as e:
        logging.error(f"Resource discovery failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
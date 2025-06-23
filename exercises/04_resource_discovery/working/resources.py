#!/usr/bin/env python3
"""
Exercise 4: Resource Discovery - Beginner-Friendly Instructions
This script demonstrates how to discover and work with resources in your Zerto environment.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

WHAT YOU NEED TO DO:
In this exercise, you will:
1. Create a ZVMLClient to connect to your ZVM (same as previous exercises)
2. Get a list of all available sites
3. Identify your local site and a peer site
4. Discover different types of resources:
   - Local site: Virtual Machines (VMs)
   - Peer site: Datastores, Hosts, Folders, Networks

STEP-BY-STEP INSTRUCTIONS:
1. Look at the TODO comments below - they tell you exactly what to do
2. Replace the placeholder code with the actual code
3. Each step has hints and examples to help you
4. If you get stuck, check the solution file in the solution/ directory

WHAT ARE RESOURCES?
- **VMs**: Virtual machines that can be protected/replicated
- **Datastores**: Storage locations where VMs are stored
- **Hosts**: Physical servers that run the VMs
- **Folders**: Organizational containers for VMs
- **Networks**: Network connections for VMs
- **Local Site**: Your current ZVM location
- **Peer Site**: Another location you can replicate to/from
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
        # ========================================
        # STEP 1: Create a ZVMLClient instance
        # ========================================        
        # TODO: Replace this line with actual ZVMLClient creation
        # HINT: Use this syntax (same as previous exercises):
        # client = ZVMLClient(
        #     zvm_address=ZVM_HOST,
        #     client_id=CLIENT_ID,
        #     client_secret=CLIENT_SECRET,
        #     verify_certificate=ZVM_SSL_VERIFY
        # )

        # EXPLANATION:
        # connection to ZVM is established using the ZVMLClient class

        # ← ADD YOUR CODE HERE
        
                
        # ========================================
        # STEP 2: Identify local and peer sites
        # ========================================
        
        # ========================================
        # STEP 2.1: Get virtualization sites
        # ========================================
        # TODO: Add code to get the list of sites
        # HINT: Use this syntax:
        # sites = client.virtualization_sites.get_virtualization_sites()
        # logging.info(f"Sites: {json.dumps(sites, indent=4)}")
        
        # EXPLANATION:
        # This gets all sites available to your ZVM
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 2.2: Get local site identifier       
        # TODO: Add code to get local site identifier
        # HINT: Use this syntax:
        # local_site_identifier = client.localsite.get_local_site().get('SiteIdentifier')
        # logging.info(f"Local site identifier: {local_site_identifier}")
        # 
        # EXPLANATION:
        # - client.localsite.get_local_site() gets your local site info
        # - .get('SiteIdentifier') extracts the unique identifier
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 2.3: Get peer site identifier       
        # TODO: Add code to get peer site identifier
        # HINT: Use this syntax:
        # peer_site = next((site for site in sites if site.get('SiteIdentifier') != local_site_identifier), None)
        # peer_site_identifier = peer_site.get('SiteIdentifier')
        # logging.info(f"Peer site identifier: {peer_site_identifier}")

        # EXPLANATION:
        # - This finds the first site that's not your local site
        # - next() gets the first matching site from the list
        # - .get('SiteIdentifier') extracts the unique identifier
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 3: Get local site resources
        # ========================================
        # TODO: Add code to get local site VMs
        # HINT: Use this syntax:
        # local_vms = client.virtualization_sites.get_virtualization_site_vms(site_identifier=local_site_identifier)
        # logging.info(f"Local VMs: {json.dumps(local_vms, indent=4)}")
        # 
        # EXPLANATION:
        # This gets all VMs that can be protected/replicated from your local site
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 4: Get peer site resources
        # ========================================

        # ========================================
        # STEP 4.1: Get peer site datastores
        # ========================================       
        # TODO: Add code to get peer site datastores
        # HINT: Use this syntax:
        # peer_datastores = client.virtualization_sites.get_virtualization_site_datastores(site_identifier=peer_site_identifier)
        # logging.info(f"Peer datastores: {json.dumps(peer_datastores, indent=4)}")
        # 
        # EXPLANATION:
        # Datastores are storage locations where VMs can be stored on the peer site
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 4.2: Get peer site hosts
        # TODO: Add code to get peer site hosts
        # HINT: Use this syntax:
        # peer_hosts = client.virtualization_sites.get_virtualization_site_hosts(site_identifier=peer_site_identifier)
        # logging.info(f"Peer hosts: {json.dumps(peer_hosts, indent=4)}")
        # 
        # EXPLANATION:
        # Hosts are physical servers that can run VMs on the peer site
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 4.3: Get peer site folders
        # TODO: Add code to get peer site folders
        # HINT: Use this syntax:
        # peer_folders = client.virtualization_sites.get_virtualization_site_folders(site_identifier=peer_site_identifier)
        # logging.info(f"Peer folders: {json.dumps(peer_folders, indent=4)}")
        # 
        # EXPLANATION:
        # Folders are organizational containers for VMs on the peer site
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 4.4: Get peer site networks
        # TODO: Add code to get peer site networks
        # HINT: Use this syntax:
        # peer_networks = client.virtualization_sites.get_virtualization_site_networks(site_identifier=peer_site_identifier)
        # logging.info(f"Peer networks: {json.dumps(peer_networks, indent=4)}")
        # 
        # EXPLANATION:
        # Networks are network connections that VMs can use on the peer site
        
        # ← ADD YOUR CODE HERE
        
    except Exception as e:
        logging.error(f"Resource discovery failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
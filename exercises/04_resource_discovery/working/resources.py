#!/usr/bin/env python3
"""
Exercise 4: Resource Discovery - Beginner-Friendly Instructions
This script demonstrates how to discover and work with resources in your Zerto environment.

PREREQUISITES (Complete these first):
1. ✅ Completed Exercise 3 (Site Discovery)
2. ✅ Make sure you have the zvml package installed
3. ✅ Updated prerequisites/config.py with your ZVM details

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
    
    print("🚀 Starting Zerto Resource Discovery Exercise")
    print("=" * 50)
    
    try:
        # ========================================
        # STEP 1: Create a ZVMLClient instance
        # ========================================
        print("\n📝 STEP 1: Creating ZVMLClient...")
        print("This is the same as previous exercises - you need to create a client to connect to ZVM.")
        
        # TODO: Replace this line with actual ZVMLClient creation
        # HINT: Use this syntax (same as previous exercises):
        # client = ZVMLClient(
        #     zvm_address=ZVM_HOST,
        #     client_id=CLIENT_ID,
        #     client_secret=CLIENT_SECRET,
        #     verify_certificate=ZVM_SSL_VERIFY
        # )
        
        client = None  # ← REPLACE THIS LINE WITH YOUR CODE
        
        # ========================================
        # STEP 2: Identify local and peer sites
        # ========================================
        print("\n📝 STEP 2.1: Getting list of sites...")
        print("You need to get a list of all available sites (same as Exercise 3).")
        
        # TODO: Add code to get the list of sites
        # HINT: Use this syntax:
        # sites = client.virtualization_sites.get_virtualization_sites()
        # 
        # EXPLANATION:
        # This gets all sites available to your ZVM
        
        # ← ADD YOUR CODE HERE
        
        print("\n📝 STEP 2.2: Getting local site identifier...")
        print("You need to get the identifier for your local site.")
        
        # TODO: Add code to get local site identifier
        # HINT: Use this syntax:
        # local_site_identifier = client.localsite.get_local_site().get('SiteIdentifier')
        # 
        # EXPLANATION:
        # - client.localsite.get_local_site() gets your local site info
        # - .get('SiteIdentifier') extracts the unique identifier
        
        local_site_identifier = None  # ← REPLACE THIS LINE WITH YOUR CODE
        
        print("\n📝 STEP 2.3: Getting peer site identifier...")
        print("You need to find a peer site (any site that's not your local site).")
        
        # TODO: Add code to get peer site identifier
        # HINT: Use this syntax:
        # peer_site = next((site for site in sites if site.get('SiteIdentifier') != local_site_identifier), None)
        # peer_site_identifier = peer_site.get('SiteIdentifier')
        # 
        # EXPLANATION:
        # - This finds the first site that's not your local site
        # - next() gets the first matching site from the list
        # - .get('SiteIdentifier') extracts the unique identifier
        
        peer_site_identifier = None  # ← REPLACE THIS LINE WITH YOUR CODE
        
        # ========================================
        # STEP 3: Get local site resources
        # ========================================
        print("\n📝 STEP 3.1: Getting local site VMs...")
        print("You need to get all virtual machines from your local site.")
        
        # TODO: Add code to get local site VMs
        # HINT: Use this syntax:
        # local_vms = client.virtualization_sites.get_virtualization_site_vms(site_identifier=local_site_identifier)
        # 
        # EXPLANATION:
        # This gets all VMs that can be protected/replicated from your local site
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 4: Get peer site resources
        # ========================================
        print("\n📝 STEP 4.1: Getting peer site datastores...")
        print("You need to get datastores from the peer site.")
        
        # TODO: Add code to get peer site datastores
        # HINT: Use this syntax:
        # peer_datastores = client.virtualization_sites.get_virtualization_site_datastores(site_identifier=peer_site_identifier)
        # 
        # EXPLANATION:
        # Datastores are storage locations where VMs can be stored on the peer site
        
        # ← ADD YOUR CODE HERE
        
        print("\n📝 STEP 4.2: Getting peer site hosts...")
        print("You need to get hosts from the peer site.")
        
        # TODO: Add code to get peer site hosts
        # HINT: Use this syntax:
        # peer_hosts = client.virtualization_sites.get_virtualization_site_hosts(site_identifier=peer_site_identifier)
        # 
        # EXPLANATION:
        # Hosts are physical servers that can run VMs on the peer site
        
        # ← ADD YOUR CODE HERE
        
        print("\n📝 STEP 4.3: Getting peer site folders...")
        print("You need to get folders from the peer site.")
        
        # TODO: Add code to get peer site folders
        # HINT: Use this syntax:
        # peer_folders = client.virtualization_sites.get_virtualization_site_folders(site_identifier=peer_site_identifier)
        # 
        # EXPLANATION:
        # Folders are organizational containers for VMs on the peer site
        
        # ← ADD YOUR CODE HERE
        
        print("\n📝 STEP 4.4: Getting peer site networks...")
        print("You need to get networks from the peer site.")
        
        # TODO: Add code to get peer site networks
        # HINT: Use this syntax:
        # peer_networks = client.virtualization_sites.get_virtualization_site_networks(site_identifier=peer_site_identifier)
        # 
        # EXPLANATION:
        # Networks are network connections that VMs can use on the peer site
        
        # ← ADD YOUR CODE HERE
        
    except Exception as e:
        # This catches any errors that might occur
        print(f"\n❌ ERROR: Something went wrong!")
        print(f"Error details: {str(e)}")
        logging.error(f"Resource discovery failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
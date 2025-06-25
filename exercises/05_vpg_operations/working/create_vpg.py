#!/usr/bin/env python3
"""
Exercise 5: VPG Operations - Beginner-Friendly Instructions
This script demonstrates how to create and configure VPGs in your Zerto environment.

PREREQUISITES (Complete these first):
1. ✅ Completed Exercise 4 (Resource Discovery)
2. ✅ Make sure you have the zvml package installed
3. ✅ Updated prerequisites/config.py with your ZVM details
4. ✅ Have some unprotected VMs available in your local site

WHAT YOU NEED TO DO:
In this exercise, you will:
1. Create a ZVMLClient to connect to your ZVM
2. Parse command line arguments (VM names and VPG name)
3. Find VMs by their names in your local site
4. Get peer site resources (datastores, folders, networks, hosts)
5. Create a VPG configuration with all necessary settings
6. Create the VPG
7. Add VMs to the VPG
8. Optionally delete the VPG

STEP-BY-STEP INSTRUCTIONS:
1. Look at the TODO comments below - they tell you exactly what to do
2. Replace the placeholder code with the actual code
3. Each step has hints and examples to help you
4. If you get stuck, check the solution file in the solution/ directory

WHAT IS A VPG?
- **VPG** = Virtual Protection Group
- It's a group of VMs that are protected together
- All VMs in a VPG have the same protection settings
- You can replicate VMs from one site to another using VPGs

USAGE EXAMPLE:
python create_vpg.py --vm-name "vm1" --vpg-name "My-VPG"
"""

import sys
import os
import logging
# Set up logging with timestamp
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
import json
import argparse
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
    Main function to demonstrate VPG creation.
    Shows how to:
    1. Create a new VPG with basic settings
    2. Configure journal, recovery, and network settings
    3. Add specified VMs to the VPG
    4. Remove the last added VM from the VPG
    """
   
    try:
        # ========================================
        # STEP 1: Parse command line arguments
        # ========================================
        print("\n📝 STEP 1: Parsing command line arguments...")
        
        # TODO: Add code to parse arguments
        # HINT: Use this syntax:
        parser = argparse.ArgumentParser(description='Create VPG and add specified VMs')
        parser.add_argument('--vm-name', default="CRM-03",
                        help='VM name to add to the VPG')
        parser.add_argument('--vpg-name', default="Test-VPG-Python",
                        help='Name of the VPG to create (default: Test-VPG-Python)')
        args = parser.parse_args()
        # 
        # EXPLANATION:
        # This gets the VM name and VPG name from command line
        
        # ========================================
        # STEP 2: Create ZVMLClient instance
        # ========================================
        print("\n📝 STEP 2: Creating ZVMLClient...")
        print("This is the same as previous exercises.")
        
        # TODO: Add code to create ZVMLClient
        # HINT: Use this syntax:
        client = ZVMLClient(
            zvm_address=ZVM_HOST,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            verify_certificate=ZVM_SSL_VERIFY
        )
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 3: Identify local and peer sites
        # ========================================
        print("\n📝 STEP 3: Getting site information...")
        print("You need to get local and peer site identifiers.")
        
        # TODO: Add code to get sites and site identifiers
        # HINT: Use this syntax:
        sites = client.virtualization_sites.get_virtualization_sites()
        local_site = client.localsite.get_local_site()
        local_site_identifier = local_site.get('SiteIdentifier')
        peer_site = next((site for site in sites if site.get('SiteIdentifier') != local_site_identifier), None)
        peer_site_identifier = peer_site.get('SiteIdentifier')
        # 
        # EXPLANATION:
        # - client.virtualization_sites.get_virtualization_sites() gets all sites
        # - client.localsite.get_local_site() gets local site info
        # - next((site for site in sites if site.get('SiteIdentifier') != local_site_identifier), None) gets peer site
        # - peer_site_identifier = peer_site.get('SiteIdentifier') gets peer site identifier

        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 4: Get peer site resources
        # ========================================
        print("\n📝 STEP 4: Getting peer site resources...")
        print("You need to get datastores, folders, networks, and hosts from the peer site.")
        
        # TODO: Add code to get peer site resources
        # HINT: Use this syntax:
        peer_datastores = client.virtualization_sites.get_virtualization_site_datastores(site_identifier=peer_site_identifier)
        logging.info(f"Peer datastores: {json.dumps(peer_datastores, indent=4)}")
        target_datastore = peer_datastores[0]  # Use first available
        
        peer_folders = client.virtualization_sites.get_virtualization_site_folders(site_identifier=peer_site_identifier)
        logging.info(f"Peer folders: {json.dumps(peer_folders, indent=4)}")
        target_folder = peer_folders[0]  # Use first available
        
        peer_networks = client.virtualization_sites.get_virtualization_site_networks(site_identifier=peer_site_identifier)
        logging.info(f"Peer networks: {json.dumps(peer_networks, indent=4)}")
        target_network = peer_networks[0]  # Use first available
        
        peer_hosts = client.virtualization_sites.get_virtualization_site_hosts(site_identifier=peer_site_identifier)
        logging.info(f"Peer hosts: {json.dumps(peer_hosts, indent=4)}")
        target_host = peer_hosts[0]  # Use first available

        # EXPLANATION:
        # - client.virtualization_sites.get_virtualization_site_datastores(site_identifier=peer_site_identifier) gets datastores
        # - client.virtualization_sites.get_virtualization_site_folders(site_identifier=peer_site_identifier) gets folders
        # - client.virtualization_sites.get_virtualization_site_networks(site_identifier=peer_site_identifier) gets networks
        # - client.virtualization_sites.get_virtualization_site_hosts(site_identifier=peer_site_identifier) gets hosts
        # - target_datastore = peer_datastores[2]  # Use first available
        # - target_folder = peer_folders[0]  # Use first available
        # - target_network = peer_networks[0]  # Use first available

        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 5: Create VPG configuration
        # ========================================
        print("\n📝 STEP 5: Creating VPG configuration...")
        print("You need to create the basic, journal, recovery, and network settings.")
        
        # TODO: Add code to create VPG configuration
        # HINT: Use this syntax:
        # basic = {
        #     "Name": args.vpg_name,
        #     "VpgType": "Remote",
        #     "RpoInSeconds": 300,
        #     "JournalHistoryInHours": 24,
        #     "Priority": "Medium",
        #     "UseWanCompression": True,
        #     "ProtectedSiteIdentifier": local_site_identifier,
        #     "RecoverySiteIdentifier": peer_site_identifier
        # }
        # journal = {}  # Keep default settings
        # recovery = {
        #     "DefaultHostIdentifier": target_host.get('HostIdentifier'),
        #     "DefaultDatastoreIdentifier": target_datastore.get('DatastoreIdentifier'),
        #     "DefaultFolderIdentifier": target_folder.get('FolderIdentifier')
        # }
        # networks = {
        #     "Failover": {
        #         "Hypervisor": {
        #             "DefaultNetworkIdentifier": target_network.get('NetworkIdentifier')
        #         }
        #     },
        #     "FailoverTest": {
        #         "Hypervisor": {
        #             "DefaultNetworkIdentifier": target_network.get('NetworkIdentifier')
        #         }
        #     }
        # }
        # 
        # EXPLANATION:
        # - basic = {
        #     "Name": args.vpg_name,
        #     "VpgType": "Remote",
        #     "RpoInSeconds": 300,
        #     "JournalHistoryInHours": 24,
        #     "Priority": "Medium",
        #     "UseWanCompression": True,
        #     "ProtectedSiteIdentifier": local_site_identifier,
        #     "RecoverySiteIdentifier": peer_site_identifier
        # }
        # - journal = {}  # Keep default settings
        # - recovery = {
        #     "DefaultHostIdentifier": target_host.get('HostIdentifier'),
        #     "DefaultDatastoreIdentifier": target_datastore.get('DatastoreIdentifier'),

        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 6: Create VPG
        # ========================================
        print("\n📝 STEP 6: Creating the VPG...")
        print("You need to call the create_vpg method with your configuration.")
        
        # TODO: Add code to create VPG
        # HINT: Use this syntax:
        vpg_id = client.vpgs.create_vpg(basic=basic, journal=journal, recovery=recovery, networks=networks, sync=True)
        logging.info(f'vpg {args.vpg_name} successfully created, vpg_id is {vpg_id}')
        # 
        # EXPLANATION:
        # This creates the VPG with all your settings

        # ← ADD YOUR CODE HERE

        # ========================================
        # STEP 7: Add Vm to the VPG
        # ========================================
        # TODO: Add code to add VMs to VPG
        # HINT: Use this syntax:
        task_id = client.vpgs.add_vm_to_vpg_by_name(args.vpg_name, args.vm_name)
        logging.info(f'vm {args.vm_name} successfully added to vpg {args.vpg_name}')
        # EXPLANATION:
        # This adds vm to an existing VPG by Vm name
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 8: Interactive VM removal (optional)
        # ========================================
        print("\n📝 STEP 8: Interactive VPG deletion...")
        print("You can optionally delete the VPG.")
        
        # TODO: Add code for interactive VM removal
        # HINT: Use this syntax:
        response = input(f"Remove VPG{args.vpg_name}? (yes/no): ").lower()
        if response in ['yes', 'y']:
            client.vpgs.delete_vpg(args.vpg_name)
        
        # ← ADD YOUR CODE HERE
        
    except Exception as e:
        # This catches any errors that might occur
        print(f"\n❌ ERROR: Something went wrong!")
        print(f"Error details: {str(e)}")
        logging.error(f"VPG operation failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 

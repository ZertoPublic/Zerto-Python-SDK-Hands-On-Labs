#!/usr/bin/env python3
"""
Exercise 5: VPG Operations - Solution (Part 1: VPG Creation)
This script demonstrates how to create and configure VPGs in your Zerto environment.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

Usage:
    python create_vpg.py --vm-names "vm1" "vm2" "vm3" [--vpg-name "My-VPG"]

This solution demonstrates:
- Creating a new VPG with basic settings
- Configuring journal, recovery, and network settings
- Adding specified VMs to the VPG
- Proper error handling and logging
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
    Main function to demonstrate VPG creation.
    Shows how to:
    1. Create a new VPG with basic settings
    2. Configure journal, recovery, and network settings
    3. Add specified VMs to the VPG
    4. Remove the last added VM from the VPG
    """
    
    try:
        # Step 1: Create a ZVMLClient instance
        logging.info(f"Initializing ZVMLClient for ZVM at {ZVM_HOST}")
        parser = argparse.ArgumentParser(description='Create VPG and add specified VMs')
        parser.add_argument('--vm-name', default="CRM-3",
                        help='VM name to add to the VPG')
        parser.add_argument('--vpg-name', default="Test-VPG-Python",
                        help='Name of the VPG to create (default: Test-VPG-Python)')
        args = parser.parse_args()

# Step 2: Create a ZVMLClient instance
        client = ZVMLClient(
            zvm_address=ZVM_HOST,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            verify_certificate=ZVM_SSL_VERIFY
        )
        
        # Step 3: Identify local and peer sites
        logging.info("Retrieving list of available sites...")
        sites = client.virtualization_sites.get_virtualization_sites()
        local_site = client.localsite.get_local_site()
        local_site_identifier = local_site.get('SiteIdentifier')
        peer_site = next((site for site in sites if site.get('SiteIdentifier') != local_site_identifier), None)
        peer_site_identifier = peer_site.get('SiteIdentifier')
    
        
        # Step 3: Get peer site resources for VPG configuration
        logging.info("\nRetrieving peer site resources for VPG configuration...")
        
        # Step 4: Get peer resources
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

        # Step 5: Create VPG configuration
        logging.info("\nCreating VPG configuration...")
        vpg_name = args.vpg_name
        
        # Basic VPG settings
        basic = {
            "Name": args.vpg_name,
            "VpgType": "Remote",
            "RpoInSeconds": 300,
            "JournalHistoryInHours": 24,
            "Priority": "Medium",
            "UseWanCompression": True,
            "ProtectedSiteIdentifier": local_site_identifier,
            "RecoverySiteIdentifier": peer_site_identifier
        }
        journal = {}  # Keep default settings
        recovery = {
            "DefaultHostIdentifier": target_host.get('HostIdentifier'),
            "DefaultDatastoreIdentifier": target_datastore.get('DatastoreIdentifier'),
            "DefaultFolderIdentifier": target_folder.get('FolderIdentifier')
        }
        networks = {
            "Failover": {
                "Hypervisor": {
                    "DefaultNetworkIdentifier": target_network.get('NetworkIdentifier')
                }
            },
            "FailoverTest": {
                "Hypervisor": {
                    "DefaultNetworkIdentifier": target_network.get('NetworkIdentifier')
                }
            }
        }
        
        # Network settings
        networks = {
            "Failover": {
                "Hypervisor": {
                    "DefaultNetworkIdentifier": target_network.get('NetworkIdentifier')
                }
            },
            "FailoverTest": {
                "Hypervisor": {
                    "DefaultNetworkIdentifier": target_network.get('NetworkIdentifier')
                }
            }
        }
        
        # Step 5: Create VPG
        vpg_id = client.vpgs.create_vpg(basic=basic, journal=journal, recovery=recovery, networks=networks, sync=True)
        logging.info(f'vpg {args.vpg_name} successfully created, vpg_id is {vpg_id}')
        

        

        # Step 7: Add Vm to the VPG
        task_id = client.vpgs.add_vm_to_vpg_by_name(args.vpg_name, args.vm_name)
        logging.info(f'vm {args.vm_name} successfully added to vpg {args.vpg_name}')
        
        # Step 8: Interactive VM removal
        response = input(f"Remove VPG{args.vpg_name}? (yes/no): ").lower()
        if response in ['yes', 'y']:
            client.vpgs.delete_vpg(args.vpg_name)
         
    except Exception as e:
        logging.error(f"VPG operation failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 

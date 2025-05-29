#!/usr/bin/env python3
"""
Exercise 5: VPG Operations - Template
This script demonstrates how to create and configure VPGs in your Zerto environment.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

Usage:
    python create_vpg.py --vm-names "vm1" "vm2" "vm3" [--vpg-name "My-VPG"]

Your task:
1. Implement the find_vms_by_names function to locate VMs by their names
2. Complete the VPG configuration with appropriate settings
3. Add the found VMs to the VPG
4. Implement VM removal functionality

The script should:
- Create a new VPG with basic settings
- Configure journal, recovery, and network settings
- Add specified VMs to the VPG
- Allow removing VMs from the VPG
"""

import sys
import os
import logging
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

def parse_arguments():
    """Parse command line arguments."""
    # TODO: Implement argument parsing
    # Required arguments:
    # --vm-names: List of VM names to add to the VPG
    # Optional arguments:
    # --vpg-name: Name of the VPG to create (default: "Test-VPG-Python")
    pass

def find_vms_by_names(client, site_identifier, vm_names):
    """
    Find VMs by their names in the specified site.
    
    Args:
        client: ZVMLClient instance
        site_identifier: Identifier of the site to search in
        vm_names: List of VM names to find
        
    Returns:
        tuple: (list of found VMs, list of not found VM names)
        
    TODO: Implement the function to:
    1. Get all unprotected VMs from the site
    2. Create a dictionary for easy lookup
    3. Find requested as an argument VMs
    4. Return found and not found VMs
    """
    pass

def remove_vm_from_vpg(client, vpg_name, vm):
    """
    Remove a VM from the VPG.
    
    Args:
        client: ZVMLClient instance
        vpg_name: Name of the VPG
        vm: VM object to remove
        
    TODO: Implement the function to:
    1. Get VM identifier
    2. Call the appropriate API to remove the VM
    3. Log the operation
    """
    pass

def main():
    """
    Main function to demonstrate VPG creation.
    
    TODO: Implement the following steps:
    1. Parse command line arguments
    2. Create ZVMLClient instance
    3. Identify local and peer sites
    4. Get peer site resources (datastores, folders, networks, hosts)
    5. Create VPG configuration
    6. Create VPG
    7. Find and add VMs to VPG
    8. Implement interactive VM removal
    """
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    try:
        # TODO: Step 1: Parse command line arguments
        # args = parse_arguments()
        
        # TODO: Step 2: Create ZVMLClient instance
        # client = ZVMLClient(...)
        
        # TODO: Step 3: Identify local and peer sites
        # local_site = client.localsite.get_local_site()
        # sites = client.virtualization_sites.get_virtualization_sites()
        
        # TODO: Step 4: Get peer site resources
        # peer_datastores = client.virtualization_sites.get_virtualization_site_datastores(...)
        # peer_folders = client.virtualization_sites.get_virtualization_site_folders(...)
        # peer_networks = client.virtualization_sites.get_virtualization_site_networks(...)
        # peer_hosts = client.virtualization_sites.get_virtualization_site_hosts(...)
        
        # TODO: Step 5: Create VPG configuration
        # basic = {
        #     "Name": "Your VPG Name",
        #     "VpgType": "Remote",
        #     "RpoInSeconds": 300,
        #     "JournalHistoryInHours": 24,
        #     "Priority": "Medium",
        #     "UseWanCompression": True,
        #     "ProtectedSiteIdentifier": local_site_identifier,
        #     "RecoverySiteIdentifier": peer_site_identifier
        # }
        
        # TODO: Step 6: Create VPG
        # vpg_id = client.vpgs.create_vpg(...)
        
        # TODO: Step 7: Find and add VMs to VPG
        # found_vms, not_found = find_vms_by_names(...)
        # for vm in found_vms:
        #     # Add VM to VPG
        
        # TODO: Step 8: Implement interactive VM removal
        # if found_vms:
        #     # Ask user if they want to remove the last VM
        #     # If yes, remove it
        
    except Exception as e:
        logging.error(f"VPG operation failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Exercise 5: VPG Operations - Solution (Part 1: VPG Creation)
This script demonstrates how to create and configure VPGs in your Zerto environment.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details

This solution demonstrates:
- Creating a new VPG with basic settings
- Configuring journal, recovery, and network settings
- Adding VMs to the VPG
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
    Main function to demonstrate VPG creation.
    Shows how to:
    1. Create a new VPG with basic settings
    2. Configure journal, recovery, and network settings
    3. Add VMs to the VPG
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
        logging.info("Retrieving list of available sites...")
        sites = client.virtualization_sites.get_virtualization_sites()
        
        if not sites:
            logging.warning("No sites found!")
            sys.exit(1)
            
        logging.info(f"Found {len(sites)} site(s):")
        logging.info(f'Sites Info: {json.dumps(sites, indent=4)}')
        
        # Get local and peer site identifiers
        local_site = client.localsite.get_local_site()
        local_site_identifier = local_site.get('SiteIdentifier')
        logging.info(f"Local site identifier: {local_site_identifier}")
        
        peer_site = next((site for site in sites if site.get('SiteIdentifier') != local_site_identifier), None)
        if not peer_site:
            logging.warning("No peer site found!")
            sys.exit(1)
            
        peer_site_identifier = peer_site.get('SiteIdentifier')
        logging.info(f"Peer site identifier: {peer_site_identifier}")
        
        # Step 3: Get peer site resources for VPG configuration
        logging.info("\nRetrieving peer site resources for VPG configuration...")
        
        # Get peer datastores
        peer_datastores = client.virtualization_sites.get_virtualization_site_datastores(site_identifier=peer_site_identifier)
        if not peer_datastores:
            logging.warning("No datastores found in peer site!")
            sys.exit(1)
        target_datastore = peer_datastores[0]  # Use first available datastore
        
        # Get peer folders
        peer_folders = client.virtualization_sites.get_virtualization_site_folders(site_identifier=peer_site_identifier)
        if not peer_folders:
            logging.warning("No folders found in peer site!")
            sys.exit(1)
        target_folder = peer_folders[0]  # Use first available folder
        
        # Get peer networks
        peer_networks = client.virtualization_sites.get_virtualization_site_networks(site_identifier=peer_site_identifier)
        if not peer_networks:
            logging.warning("No networks found in peer site!")
            sys.exit(1)
        target_network = peer_networks[0]  # Use first available network
        
        # Get peer hosts
        peer_hosts = client.virtualization_sites.get_virtualization_site_hosts(site_identifier=peer_site_identifier)
        if not peer_hosts:
            logging.warning("No hosts found in peer site!")
            sys.exit(1)
        target_host = peer_hosts[0]  # Use first available host
        
        # Step 4: Create VPG configuration
        logging.info("\nCreating VPG configuration...")
        vpg_name = "Test-VPG-Python"
        
        # Basic VPG settings
        basic = {
            "Name": vpg_name,
            "VpgType": "Remote",
            "RpoInSeconds": 300,
            "JournalHistoryInHours": 24,
            "Priority": "Medium",
            "UseWanCompression": True,
            "ProtectedSiteIdentifier": local_site_identifier,
            "RecoverySiteIdentifier": peer_site_identifier
        }
        
        # Journal settings
        journal = {
            "DatastoreIdentifier": target_datastore.get('DatastoreIdentifier'),
            "Limitation": {
                "HardLimitInMB": 153600,
                "WarningThresholdInMB": 115200
            }
        }
        
        # Recovery settings
        recovery = {
            "DefaultHostIdentifier": target_host.get('HostIdentifier'),
            "DefaultDatastoreIdentifier": target_datastore.get('DatastoreIdentifier'),
            "DefaultFolderIdentifier": target_folder.get('FolderIdentifier')
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
        logging.info(f"\nCreating VPG '{vpg_name}'...")
        logging.info("VPG Settings:")
        logging.info(f"Basic: {json.dumps(basic, indent=4)}")
        logging.info(f"Journal: {json.dumps(journal, indent=4)}")
        logging.info(f"Recovery: {json.dumps(recovery, indent=4)}")
        logging.info(f"Networks: {json.dumps(networks, indent=4)}")
        
        # Create VPG
        vpg_id = client.vpgs.create_vpg(basic=basic, journal=journal, recovery=recovery, networks=networks, sync=True)
        logging.info(f"VPG created successfully with ID: {vpg_id}")
        
        # Step 6: Get available VMs for protection
        logging.info("\nRetrieving available VMs for protection...")
        vms = client.virtualization_sites.get_virtualization_site_vms(site_identifier=local_site_identifier)
        
        if not vms:
            logging.warning("No VMs found for protection!")
            sys.exit(1)
            
        # Filter out VMs that are already protected
        available_vms = [vm for vm in vms if not vm.get('IsProtected')]
        logging.info(f"Found {len(available_vms)} available VM(s) for protection")
        
        # Step 7: Add VMs to VPG
        for vm in available_vms[:2]:  # Add first two available VMs
            logging.info(f"\nAdding VM {vm.get('VmName')} to VPG...")
            vm_payload = {
                "VmIdentifier": vm.get('VmIdentifier'),
                "Recovery": {
                    "HostIdentifier": target_host.get('HostIdentifier'),
                    "DatastoreIdentifier": target_datastore.get('DatastoreIdentifier'),
                    "FolderIdentifier": target_folder.get('FolderIdentifier')
                }
            }
            task_id = client.vpgs.add_vm_to_vpg(vpg_name, vm_list_payload=vm_payload)
            logging.info(f"Task ID: {task_id} to add VM {vm.get('VmName')} to VPG")
        
    except Exception as e:
        logging.error(f"VPG creation failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
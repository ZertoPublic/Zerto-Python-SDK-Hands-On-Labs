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

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Create VPG and add specified VMs')
    parser.add_argument('--vm-names', nargs='+', required=True,
                      help='List of VM names to add to the VPG (can be space-separated or comma-separated)')
    parser.add_argument('--vpg-name', default="Test-VPG-Python",
                      help='Name of the VPG to create (default: Test-VPG-Python)')
    return parser.parse_args()

def find_vms_by_names(client, site_identifier, vm_names):
    """Find VMs by their names in the specified site."""
    vms = client.virtualization_sites.get_virtualization_site_vms(site_identifier=site_identifier)
    logging.info(f"find_vms_by_names: found vms {json.dumps(vms, indent=4)} VMs in site {site_identifier}")
    if not vms:
        return [], []
    
    # Create a dictionary of VM name to VM object for easy lookup
    vm_dict = {vm.get('VmName'): vm for vm in vms}
    
    # Find requested VMs
    found_vms = []
    not_found = []
    
    for vm_name in vm_names:
        if vm_name in vm_dict:
            found_vms.append(vm_dict[vm_name])
            logging.info(f"Found VM: {vm_name} (ID: {vm_dict[vm_name].get('VmIdentifier')})")
        else:
            not_found.append(vm_name)
            logging.warning(f"VM not found: {vm_name}")
    
    return found_vms, not_found

def remove_vm_from_vpg(client, vpg_name, vm):
    """Remove a VM from the VPG."""
    vm_name = vm.get('VmName')
    # vm_id = vm.get('VmIdentifier')
    logging.info(f"\nRemoving VM {vm_name} from VPG...")
    client.vpgs.remove_vm_from_vpg(vpg_name=vpg_name, vm_name=vm_name)

def main():
    """
    Main function to demonstrate VPG creation.
    Shows how to:
    1. Create a new VPG with basic settings
    2. Configure journal, recovery, and network settings
    3. Add specified VMs to the VPG
    4. Remove the last added VM from the VPG
    """
    # Parse command line arguments
    args = parse_arguments()
    
    # Handle both space-separated and comma-separated VM names
    vm_names = []
    for name in args.vm_names:
        vm_names.extend([n.strip() for n in name.split(',') if n.strip()])
    
    # Update args.vm_names with the processed list
    args.vm_names = vm_names
    
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
        vpg_name = args.vpg_name
        
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
        
        # Journal settings, keep the default settings
        journal = {
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
        
        # Step 6: Get specified VMs for protection
        logging.info(f"\nRetrieving specified VMs for protection: {args.vm_names}")
        found_vms, not_found = find_vms_by_names(client, local_site_identifier, args.vm_names)
        
        if not_found:
            logging.warning(f"The following VMs were not found: {not_found}")
        
        if not found_vms:
            logging.error("No VMs found for protection!")
            sys.exit(1)
            
        logging.info(f"Found {len(found_vms)} VM(s) for protection")
        
        # Step 7: Add VMs to VPG
        for vm in found_vms:
            vm_name = vm.get('VmName')
            vm_id = vm.get('VmIdentifier')
            logging.info(f"\nAdding VM {vm_name} (ID: {vm_id}) to VPG...")
            vm_payload = {
                "VmIdentifier": vm_id,
                "Recovery": {
                    "HostIdentifier": target_host.get('HostIdentifier'),
                    "DatastoreIdentifier": target_datastore.get('DatastoreIdentifier'),
                    "FolderIdentifier": target_folder.get('FolderIdentifier')
                }
            }
            task_id = client.vpgs.add_vm_to_vpg(args.vpg_name, vm_list_payload=vm_payload)
            logging.info(f"Task ID: {task_id} to add VM {vm_name} to VPG")
        
        # Step 8: Interactive VM removal
        if found_vms:
            last_vm = found_vms[-1]
            vm_name = last_vm.get('VmName')
            
            while True:
                response = input(f"\nWould you like to remove the last added VM ({vm_name}) from the VPG? (yes/no): ").lower()
                if response in ['yes', 'y']:
                    remove_vm_from_vpg(client, args.vpg_name, last_vm)
                    logging.info(f"Successfully removed VM {vm_name} from VPG {args.vpg_name}")
                    break
                elif response in ['no', 'n']:
                    logging.info("Skipping VM removal.")
                    break
                else:
                    print("Please answer 'yes' or 'no'")
        
    except Exception as e:
        logging.error(f"VPG operation failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
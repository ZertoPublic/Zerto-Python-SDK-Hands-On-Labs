#!/usr/bin/env python3
"""
Exercise 5: VPG Operations - Solution (Part 2: VM Management)
This script demonstrates how to manage VMs within VPGs in your Zerto environment.

Prerequisites:
1. Install the zvml package in development mode:
   cd /path/to/zvml-python-sdk
   pip install -e .
2. Update prerequisites/config.py with your ZVM details
3. Run create_vpg.py first to create a VPG

This solution demonstrates:
- Adding VMs to existing VPGs using add_vm_to_vpg
- Removing VMs from VPGs using remove_vm_from_vpg
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
    Main function to demonstrate VM management in VPGs.
    Shows how to:
    1. Add VMs to an existing VPG using add_vm_to_vpg
    2. Remove VMs from a VPG using remove_vm_from_vpg
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
        
        # Step 2: Find the VPG we created earlier
        logging.info("\nRetrieving VPGs...")
        vpgs = client.vpgs.get_vpgs()
        
        if not vpgs:
            logging.warning("No VPGs found!")
            sys.exit(1)
            
        # Find our test VPG
        test_vpg = next((vpg for vpg in vpgs if vpg.get('VpgName') == "Test-VPG-Python"), None)
        if not test_vpg:
            logging.warning("Test VPG not found! Please run create_vpg.py first.")
            sys.exit(1)
            
        vpg_name = test_vpg.get('VpgName')
        logging.info(f"Found VPG: {json.dumps(test_vpg, indent=4)}")
        
        # Step 3: Get available VMs for adding to VPG
        logging.info("\nRetrieving available VMs...")
        vms = client.virtualization_sites.get_virtualization_site_vms(site_identifier=test_vpg.get('SourceSiteIdentifier'))
        
        if not vms:
            logging.warning("No VMs found!")
            sys.exit(1)
            
        # Filter out VMs that are already protected
        available_vms = [vm for vm in vms if not vm.get('IsProtected')]
        logging.info(f"Found {len(available_vms)} available VM(s)")
        
        if not available_vms:
            logging.warning("No available VMs to add!")
            sys.exit(1)
        
        # Step 4: Get peer site resources for VM recovery settings
        logging.info("\nRetrieving peer site resources...")
        peer_site_identifier = test_vpg.get('TargetSiteIdentifier')
        
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
        
        # Get peer hosts
        peer_hosts = client.virtualization_sites.get_virtualization_site_hosts(site_identifier=peer_site_identifier)
        if not peer_hosts:
            logging.warning("No hosts found in peer site!")
            sys.exit(1)
        target_host = peer_hosts[0]  # Use first available host
        
        # Step 5: Add a new VM to the VPG
        logging.info("\nAdding a new VM to the VPG...")
        vm_to_add = available_vms[0]  # Use first available VM
        
        vm_payload = {
            "VmIdentifier": vm_to_add.get('VmIdentifier'),
            "Recovery": {
                "HostIdentifier": target_host.get('HostIdentifier'),
                "DatastoreIdentifier": target_datastore.get('DatastoreIdentifier'),
                "FolderIdentifier": target_folder.get('FolderIdentifier')
            }
        }
        
        task_id = client.vpgs.add_vm_to_vpg(vpg_name, vm_list_payload=vm_payload)
        logging.info(f"Task ID: {task_id} to add VM {vm_to_add.get('VmName')} to VPG")
        
        # Step 6: Remove a VM from the VPG
        logging.info("\nRemoving a VM from the VPG...")
        
        # Get VPG VMs
        vpg_vms = client.vpgs.get_vpg_vms(vpg_name)
        if len(vpg_vms) > 1:  # Keep at least one VM
            vm_to_remove = vpg_vms[-1]  # Remove the last VM
            vm_identifier = vm_to_remove.get('VmIdentifier')
            
            task_id = client.vpgs.remove_vm_from_vpg(vpg_name, vm_identifier)
            logging.info(f"Task ID: {task_id} to remove VM {vm_to_remove.get('VmName')} from VPG")
        else:
            logging.info("Skipping VM removal to maintain at least one VM in the VPG")
        
    except Exception as e:
        logging.error(f"VM management failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
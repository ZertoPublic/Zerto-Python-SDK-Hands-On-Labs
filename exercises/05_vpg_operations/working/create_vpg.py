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
8. Optionally remove a VM from the VPG

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
python create_vpg.py --vm-names "vm1" "vm2" "vm3" --vpg-name "My-VPG"
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

def parse_arguments():
    """
    Parse command line arguments.
    
    TODO: Implement argument parsing
    HINT: Use this syntax:
    parser = argparse.ArgumentParser(description='Create VPG and add specified VMs')
    parser.add_argument('--vm-names', nargs='+', required=True,
                      help='List of VM names to add to the VPG')
    parser.add_argument('--vpg-name', default="Test-VPG-Python",
                      help='Name of the VPG to create (default: Test-VPG-Python)')
    return parser.parse_args()
    
    EXPLANATION:
    - argparse helps you get command line arguments
    - --vm-names: List of VM names (required)
    - --vpg-name: Name for the VPG (optional, has default)
    """
    pass  # ← REPLACE WITH YOUR CODE

def find_vms_by_names(client, site_identifier, vm_names):
    """
    Find VMs by their names in the specified site.
    
    TODO: Implement the function to:
    1. Get all VMs from the site using client.virtualization_sites.get_virtualization_site_vms()
    2. Create a dictionary for easy lookup: {vm.get('VmName'): vm for vm in vms}
    3. Find requested VMs and return found/not found lists
    
    HINT: Use this syntax:
    vms = client.virtualization_sites.get_virtualization_site_vms(site_identifier=site_identifier)
    vm_dict = {vm.get('VmName'): vm for vm in vms}
    
    found_vms = []
    not_found = []
    
    for vm_name in vm_names:
        if vm_name in vm_dict:
            found_vms.append(vm_dict[vm_name])
        else:
            not_found.append(vm_name)
    
    return found_vms, not_found
    """
    pass  # ← REPLACE WITH YOUR CODE

def remove_vm_from_vpg(client, vpg_name, vm):
    """
    Remove a VM from the VPG.
    
    TODO: Implement the function to:
    1. Get VM name from vm object
    2. Call client.vpgs.remove_vm_from_vpg() to remove the VM
    
    HINT: Use this syntax:
    vm_name = vm.get('VmName')
    client.vpgs.remove_vm_from_vpg(vpg_name=vpg_name, vm_name=vm_name)
    """
    pass  # ← REPLACE WITH YOUR CODE

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
    
    print("🚀 Starting Zerto VPG Operations Exercise")
    print("=" * 50)
    
    try:
        # ========================================
        # STEP 1: Parse command line arguments
        # ========================================
        print("\n📝 STEP 1: Parsing command line arguments...")
        print("You need to call the parse_arguments() function you created above.")
        
        # TODO: Add code to parse arguments
        # HINT: Use this syntax:
        # args = parse_arguments()
        # 
        # EXPLANATION:
        # This gets the VM names and VPG name from command line
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 2: Create ZVMLClient instance
        # ========================================
        print("\n📝 STEP 2: Creating ZVMLClient...")
        print("This is the same as previous exercises.")
        
        # TODO: Add code to create ZVMLClient
        # HINT: Use this syntax:
        # client = ZVMLClient(
        #     zvm_address=ZVM_HOST,
        #     client_id=CLIENT_ID,
        #     client_secret=CLIENT_SECRET,
        #     verify_certificate=ZVM_SSL_VERIFY
        # )
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 3: Identify local and peer sites
        # ========================================
        print("\n📝 STEP 3: Getting site information...")
        print("You need to get local and peer site identifiers.")
        
        # TODO: Add code to get sites and site identifiers
        # HINT: Use this syntax:
        # sites = client.virtualization_sites.get_virtualization_sites()
        # local_site = client.localsite.get_local_site()
        # local_site_identifier = local_site.get('SiteIdentifier')
        # peer_site = next((site for site in sites if site.get('SiteIdentifier') != local_site_identifier), None)
        # peer_site_identifier = peer_site.get('SiteIdentifier')
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 4: Get peer site resources
        # ========================================
        print("\n📝 STEP 4: Getting peer site resources...")
        print("You need to get datastores, folders, networks, and hosts from the peer site.")
        
        # TODO: Add code to get peer site resources
        # HINT: Use this syntax:
        # peer_datastores = client.virtualization_sites.get_virtualization_site_datastores(site_identifier=peer_site_identifier)
        # target_datastore = peer_datastores[0]  # Use first available
        # 
        # peer_folders = client.virtualization_sites.get_virtualization_site_folders(site_identifier=peer_site_identifier)
        # target_folder = peer_folders[0]  # Use first available
        # 
        # peer_networks = client.virtualization_sites.get_virtualization_site_networks(site_identifier=peer_site_identifier)
        # target_network = peer_networks[0]  # Use first available
        # 
        # peer_hosts = client.virtualization_sites.get_virtualization_site_hosts(site_identifier=peer_site_identifier)
        # target_host = peer_hosts[0]  # Use first available
        
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
        # 
        # journal = {}  # Keep default settings
        # 
        # recovery = {
        #     "DefaultHostIdentifier": target_host.get('HostIdentifier'),
        #     "DefaultDatastoreIdentifier": target_datastore.get('DatastoreIdentifier'),
        #     "DefaultFolderIdentifier": target_folder.get('FolderIdentifier')
        # }
        # 
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
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 6: Create VPG
        # ========================================
        print("\n📝 STEP 6: Creating the VPG...")
        print("You need to call the create_vpg method with your configuration.")
        
        # TODO: Add code to create VPG
        # HINT: Use this syntax:
        # vpg_id = client.vpgs.create_vpg(basic=basic, journal=journal, recovery=recovery, networks=networks, sync=True)
        # 
        # EXPLANATION:
        # This creates the VPG with all your settings
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 7: Find and add VMs to VPG
        # ========================================
        print("\n📝 STEP 7: Finding and adding VMs...")
        print("You need to find the VMs and add them to the VPG.")
        
        # TODO: Add code to find VMs
        # HINT: Use this syntax:
        # found_vms, not_found = find_vms_by_names(client, local_site_identifier, args.vm_names)
        # 
        # EXPLANATION:
        # This finds the VMs you specified in the command line
        
        # ← ADD YOUR CODE HERE
        
        # TODO: Add code to add VMs to VPG
        # HINT: Use this syntax:
        # for vm in found_vms:
        #     vm_name = vm.get('VmName')
        #     vm_id = vm.get('VmIdentifier')
        #     vm_payload = {
        #         "VmIdentifier": vm_id,
        #         "Recovery": {
        #             "HostIdentifier": target_host.get('HostIdentifier'),
        #             "DatastoreIdentifier": target_datastore.get('DatastoreIdentifier'),
        #             "FolderIdentifier": target_folder.get('FolderIdentifier')
        #         }
        #     }
        #     task_id = client.vpgs.add_vm_to_vpg(args.vpg_name, vm_list_payload=vm_payload)
        
        # ← ADD YOUR CODE HERE
        
        # ========================================
        # STEP 8: Interactive VM removal (optional)
        # ========================================
        print("\n📝 STEP 8: Interactive VM removal...")
        print("You can optionally remove the last VM from the VPG.")
        
        # TODO: Add code for interactive VM removal
        # HINT: Use this syntax:
        # if found_vms:
        #     last_vm = found_vms[-1]
        #     vm_name = last_vm.get('VmName')
        #     response = input(f"Remove VM {vm_name} from VPG? (yes/no): ").lower()
        #     if response in ['yes', 'y']:
        #         remove_vm_from_vpg(client, args.vpg_name, last_vm)
        
        # ← ADD YOUR CODE HERE
        
    except Exception as e:
        # This catches any errors that might occur
        print(f"\n❌ ERROR: Something went wrong!")
        print(f"Error details: {str(e)}")
        logging.error(f"VPG operation failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
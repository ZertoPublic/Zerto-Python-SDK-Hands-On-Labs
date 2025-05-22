#!/usr/bin/env python3
"""
Exercise 7: Bulk Operations
This script demonstrates how to perform bulk IP modifications on multiple VMs.
"""

import sys
import csv
from pathlib import Path

# Add the parent directory to the Python path to import the SDK
sys.path.append(str(Path(__file__).parent.parent.parent.parent))

# Import the SDK modules
from zvml import ZertoClient
from zvml.vpgs import VPG
from zvml.common import ZertoVPGError

# Import configuration
try:
    from prerequisites.config import (
        ZVM_HOST,
        ZVM_PORT,
        ZVM_SSL_VERIFY,
        KEYCLOAK_SERVER_URL,
        KEYCLOAK_REALM,
        CLIENT_ID,
        CLIENT_SECRET
    )
except ImportError:
    print("Error: Please copy config.example.py to config.py and update with your values")
    sys.exit(1)

def read_vm_list(csv_file):
    """
    Read VM list from CSV file.
    Expected format: vm_name,ip_address,subnet_mask,gateway
    """
    # TODO: Implement CSV reading
    # Hint: Use csv.DictReader
    pass

def main():
    """
    Main function to demonstrate bulk IP operations.
    """
    # Step 1: Create and authenticate ZertoClient
    # TODO: Initialize ZertoClient and authenticate
    # Hint: Reuse the authentication code from previous exercises
    
    # Step 2: Read VM list
    # TODO: Read the VM list from CSV file
    # Hint: Use the read_vm_list function
    
    # Step 3: Get VPG
    # TODO: Find and get the VPG containing the VMs
    # Hint: Use client.vpgs.list() and client.vpgs.get()
    
    # Step 4: Prepare IP changes
    # TODO: Prepare the IP modification data
    # Required for each VM:
    # - VM identifier
    # - New IP settings
    # - Network information
    
    # Step 5: Apply IP changes
    # TODO: Apply the IP changes to all VMs
    # Hint: Use vpg.modify_vm_ips() method
    
    # Step 6: Monitor progress
    # TODO: Monitor the bulk operation progress
    # Required steps:
    # - Track operation status
    # - Handle any failures
    # - Report results
    
    # Step 7: Handle errors
    # TODO: Add error handling for bulk operations
    # Hint: Use try/except blocks for ZertoVPGError

if __name__ == "__main__":
    main() 
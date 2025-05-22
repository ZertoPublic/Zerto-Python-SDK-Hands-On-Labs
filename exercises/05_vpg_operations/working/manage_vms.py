#!/usr/bin/env python3
"""
Exercise 5: VPG Operations - VM Management
This script demonstrates how to manage VMs within a VPG.
"""

import sys
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

def main():
    """
    Main function to demonstrate VM management in VPGs.
    """
    # Step 1: Create and authenticate ZertoClient
    # TODO: Initialize ZertoClient and authenticate
    # Hint: Reuse the authentication code from previous exercises
    
    # Step 2: Get the VPG
    # TODO: Find and get the VPG you want to manage
    # Hint: Use client.vpgs.list() and client.vpgs.get()
    
    # Step 3: List current VMs in the VPG
    # TODO: Get a list of VMs currently in the VPG
    # Hint: Use vpg.get_vms() method
    
    # Step 4: Add VMs to the VPG
    # TODO: Add one or more VMs to the VPG
    # Required steps:
    # - Find eligible VMs
    # - Configure VM settings
    # - Add VMs to VPG
    # Hint: Use vpg.add_vms() method
    
    # Step 5: Remove VMs from the VPG
    # TODO: Remove one or more VMs from the VPG
    # Hint: Use vpg.remove_vms() method
    
    # Step 6: Validate VPG after changes
    # TODO: Validate the VPG after VM changes
    # Hint: Use vpg.validate() method
    
    # Step 7: Handle errors
    # TODO: Add error handling for VM operations
    # Hint: Use try/except blocks for ZertoVPGError

if __name__ == "__main__":
    main() 
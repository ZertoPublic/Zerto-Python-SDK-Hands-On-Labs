#!/usr/bin/env python3
"""
Exercise 5: VPG Operations - VPG Creation
This script demonstrates how to create and configure a VPG.
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
    Main function to demonstrate VPG creation.
    """
    # Step 1: Create and authenticate ZertoClient
    # TODO: Initialize ZertoClient and authenticate
    # Hint: Reuse the authentication code from previous exercises
    
    # Step 2: Get source and target sites
    # TODO: Get local site and a peer site
    # Hint: Use client.sites.get_local() and client.sites.list()
    
    # Step 3: Configure VPG settings
    # TODO: Create VPG settings with required parameters
    # Required settings:
    # - VPG name
    # - Source site
    # - Target site
    # - Journal history
    # - RPO
    # - Test network
    # - Recovery network
    
    # Step 4: Create the VPG
    # TODO: Create a new VPG with the configured settings
    # Hint: Use client.vpgs.create() method
    
    # Step 5: Validate the VPG
    # TODO: Validate the VPG configuration
    # Hint: Use vpg.validate() method
    
    # Step 6: Handle errors
    # TODO: Add error handling for VPG operations
    # Hint: Use try/except blocks for ZertoVPGError

if __name__ == "__main__":
    main() 
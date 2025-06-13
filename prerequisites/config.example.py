# Zerto API Configuration - EXAMPLE FILE
# 
# INSTRUCTIONS FOR BEGINNERS:
# 1. Copy this file to config.py: cp config.example.py config.py
# 2. Edit config.py with your actual ZVM details
# 3. Never commit your real config.py file (it contains secrets!)
#
# WHERE TO GET THESE VALUES:
# - ZVM_HOST: Ask your Zerto administrator for the ZVM IP address or hostname
# - CLIENT_ID: Create this in Keycloak (see Keycloak setup instructions)
# - CLIENT_SECRET: Generated when you create the client in Keycloak

# ZVM Connection Details
ZVM_HOST = "192.168.111.20"  # ← REPLACE: Your ZVM IP address (e.g., "10.0.0.100")
ZVM_PORT = 443                # ← USUALLY KEEP AS IS: Default HTTPS port
ZVM_SSL_VERIFY = False        # ← USUALLY KEEP AS IS: Set to False for self-signed certificates

# Keycloak Authentication
CLIENT_ID = "sdk-api"         # ← REPLACE: Your Keycloak client ID (e.g., "my-api-client")
CLIENT_SECRET = "your-secret-here"  # ← REPLACE: Your Keycloak client secret

# Optional: Proxy settings if needed (usually not required)
# PROXY = {
#     "http": "http://proxy.example.com:8080",
#     "https": "https://proxy.example.com:8080"
# }

# ========================================
# KEYCLOAK SETUP INSTRUCTIONS:
# ========================================
# 1. Open your browser and go to: https://YOUR_ZVM_IP/auth
# 2. Login with your Zerto admin credentials
# 3. In the left menu, click "Clients"
# 4. Click "Create" button
# 5. Fill in:
#    - Client ID: Choose a name (e.g., "python-sdk-client")
#    - Client Name: Same as Client ID
# 6. Click "Next"
# 7. Enable these options:
#    - Client authentication: ON
#    - Authorization: ON
#    - Standard flow: ON
#    - Direct access grants: ON
#    - Implicit flow: ON
#    - OAuth 2.0 Device Authorization Grant: ON
# 8. Click "Next" then "Save"
# 9. Go to "Service account roles" tab
# 10. Click "Assign role" and select "admin"
# 11. Go to "Credentials" tab
# 12. Copy the "Client Secret" value
# 13. Use the Client ID and Client Secret in your config.py 
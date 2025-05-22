# Zerto API Configuration
# Update these values with your ZVM details

# ZVM Connection Details
ZVM_HOST = "192.168.111.20" #"zvm.example.com"
ZVM_PORT = 443  # Default HTTPS port
ZVM_SSL_VERIFY = False  # Set to False for self-signed certificates

# Keycloak Authentication
CLIENT_ID = "zerto-api" #"your-client-id"
CLIENT_SECRET = "q0GUcbK1olq2Op27cpjvTHT5scKeQWBy" # "your-client-secret"

# Optional: Proxy settings if needed
# PROXY = {
#     "http": "http://proxy.example.com:8080",
#     "https": "https://proxy.example.com:8080"
# } 
# Zerto Python SDK Hands-On Lab

This hands-on lab provides practical experience with the Zerto Python SDK. The lab is designed to take approximately 60 minutes to complete and covers key aspects of the SDK including authentication, site discovery, VPG operations, and more.

## Prerequisites

- Python 3.8 or higher
- Access to a Zerto Virtual Manager (ZVM)
- API credentials (client ID and secret)
- Basic understanding of Python programming
- Basic understanding of Zerto concepts

## Lab Structure

The lab is divided into 7 exercises:

1. **Introduction to Zerto APIs** (5 min)
   - Understanding Zerto's REST API
   - API documentation overview
   - Keycloak authentication basics

2. **Authentication** (10 min)
   - Creating a Keycloak client
   - Establishing connection to ZVM
   - Testing authentication

3. **Site Discovery** (5 min)
   - Listing virtualization sites
   - Understanding site information
   - Basic site operations

4. **Resource Discovery** (10 min)
   - Discovering local site resources
   - Working with peer sites
   - Understanding resource identifiers

5. **VPG Operations** (15 min)
   - Creating VPGs
   - Adding VMs to VPGs
   - Managing VPG settings
   - VPG validation

6. **Failover Testing** (10 min)
   - Initiating failover tests
   - Monitoring test status
   - Stopping tests

7. **Bulk Operations** (5 min)
   - Performing bulk IP modifications
   - Managing multiple VMs

## Getting Started

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Zerto-Python-SDK-Hands-On-Labs
   ```

2. Create and activate a virtual environment:

   **On macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **On Windows:**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

   **On Windows PowerShell:**
   ```powershell
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```

3. Install the Zerto Python SDK (`zvml` module):

   **Option 1: Standard install**
   ```bash
   cd ../zvml-python-sdk
   pip install -r requirements.txt
   pip install .
   cd ../Zerto-Python-SDK-Hands-On-Labs
   ```

   **Option 2: Development mode (recommended for contributors)**
   ```bash
   cd ../zvml-python-sdk
   pip install -r requirements.txt
   pip install -e .
   cd ../Zerto-Python-SDK-Hands-On-Labs
   ```

4. Install required packages:
   ```bash
   pip install -r prerequisites/requirements.txt
   ```

5. Set up your environment:
   - Copy `prerequisites/config.example.py` to `prerequisites/config.py`
   - Update the configuration with your ZVM details:
     - **ZVM_HOST**: Your Zerto Virtual Manager IP address or hostname
     - **CLIENT_ID**: Your Keycloak client ID (see Keycloak setup in config.example.py)
     - **CLIENT_SECRET**: Your Keycloak client secret
   - **Important**: Never commit your `config.py` file as it contains sensitive credentials

6. Start with Exercise 1 in the `exercises` directory

**Note:** When you're done working on the project, you can deactivate the virtual environment by typing `deactivate` in your terminal.

## Lab Completion

Each exercise includes:
- Step-by-step instructions
- Working directory for your code
- Solution directory for reference
- Common issues and troubleshooting

Complete all exercises to gain a comprehensive understanding of the Zerto Python SDK.

## Support

If you encounter any issues during the lab:
1. Check the troubleshooting section in each exercise
2. Review the solution code
3. Consult the Zerto API documentation

## Feedback

Your feedback is valuable! Please complete the feedback form after finishing the lab to help us improve the content.
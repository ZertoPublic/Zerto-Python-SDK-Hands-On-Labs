# Exercise 2: Authentication

## Overview
In this exercise, you'll learn how to authenticate with the Zerto API using Keycloak. You'll create a client and establish a connection to your ZVM.

## What You'll Learn
- How to create a ZVMLClient object (your "remote control" for ZVM)
- How to connect to your Zerto Virtual Manager
- How to test if the connection works
- How to handle errors if something goes wrong

## Time
10 minutes

## Prerequisites
- ✅ Completed Exercise 1
- ✅ Valid ZVM credentials (IP address, client ID, client secret)
- ✅ Updated `prerequisites/config.py` with your details

## Step-by-Step Instructions

### Step 1: Open the Working File
1. Navigate to `exercises/02_authentication/working/`
2. Open `auth.py` in your code editor
3. Read through the detailed comments - they explain everything!

### Step 2: Complete the Code
The file has three main sections you need to complete:

1. **Create ZVMLClient** - Replace `client = None` with actual code
2. **Test Connection** - Add code to test if it works
3. **Success Message** - Add a final success message

### Step 3: Run Your Code
```bash
cd exercises/02_authentication/working/
python auth.py
```

### Step 4: Check the Results
- ✅ **Success**: You'll see "Connection successful!" and ZVM version info
- ❌ **Error**: Check the error message and review your config.py

## Working Directory
The `working` directory contains:
- `auth.py` - **Beginner-friendly template** with detailed instructions

## Solution
The `solution` directory contains:
- `auth.py` - Complete working example (check this if you get stuck!)

## Key Concepts Explained

### What is ZVMLClient?
- Think of it as a "remote control" for your Zerto Virtual Manager
- It handles all the communication between your Python code and ZVM
- You need to give it your ZVM address and login credentials

### What is Keycloak?
- It's the authentication system that Zerto uses
- You create a "client" (like a username) and get a "secret" (like a password)
- The ZVMLClient uses these to log into your ZVM

### What is SSL Verification?
- It's a security check to make sure you're connecting to the right server
- Usually set to `False` for Zerto (self-signed certificates)

## Common Issues & Solutions

### ❌ "Configuration file not found"
**Solution**: Copy `prerequisites/config.example.py` to `prerequisites/config.py`

### ❌ "Authentication failed"
**Solutions**:
- Check your ZVM_HOST is correct
- Verify your CLIENT_ID and CLIENT_SECRET
- Make sure your ZVM is running and accessible

### ❌ "SSL certificate" errors
**Solution**: Make sure `ZVM_SSL_VERIFY = False` in your config.py

### ❌ "Connection refused" or "Network unreachable"
**Solutions**:
- Check your ZVM IP address is correct
- Make sure you can ping the ZVM from your computer
- Check firewall settings

## Need Help?
1. Read the detailed comments in the code
2. Check the solution file
3. Review your `config.py` settings
4. Ask your Zerto administrator for help with credentials

## Next Steps
Once you successfully connect, proceed to **Exercise 3: Site Discovery** to start working with Zerto sites. 
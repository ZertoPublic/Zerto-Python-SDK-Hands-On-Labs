# Exercise 7: Bulk VPG NIC Settings Management

This exercise demonstrates how to perform bulk operations on VPG NIC settings using two provided scripts:
1. `export_vpg_settings_nics_to_csv.py` - Exports current VPG NIC settings to a CSV file
2. `import_vpg_settings_nics_from_csv.py` - Imports and applies NIC settings from a CSV file

## Prerequisites

1. Python 3.6 or higher
2. Zerto Python SDK (`zvml` package) installed in development mode:
   ```bash
   cd /path/to/zvml-python-sdk
   pip install -e .
   ```
3. Access to a Zerto Virtual Manager (ZVM) with appropriate permissions
4. VPGs already created and configured in your environment

## Exercise Overview

This exercise will guide you through the process of:
1. Exporting current VPG NIC settings to a CSV file
2. Modifying the CSV file to update IP configurations
3. Importing and applying the updated settings back to the VPGs

## Step 1: Export Current VPG Settings

Use the export script to save current VPG NIC settings to a CSV file:

```bash
python export_vpg_settings_nics_to_csv.py \
    --zvm_address "192.168.111.20" \
    --client_id "zerto-api" \
    --client_secret "your-secret-here" \
    --vpg_names "VpgTest1,VpgTest2" \
    --ignore_ssl
```

The script will create two files:
- `ExportedSettings_[timestamp].json` - Full VPG settings in JSON format
- `ExportedSettings_[timestamp].csv` - NIC settings in CSV format

## Step 2: Modify the CSV File

Open the generated CSV file in a spreadsheet application (e.g., Microsoft Excel, Google Sheets) and modify the following settings as needed:

1. **Failover Network Settings**:
   - `Failover ShouldReplaceIpConfiguration` - Set to "True" to modify IP settings
   - `Failover Network` - Network identifier for failover
   - `Failover DHCP` - Set to "True" for DHCP or "False" for static IP
   - `Failover IP` - Static IP address (required if DHCP is False)
   - `Failover Subnet` - Subnet mask (required if DHCP is False)
   - `Failover Gateway` - Default gateway (optional)
   - `Failover DNS1` - Primary DNS server (optional)
   - `Failover DNS2` - Secondary DNS server (optional)

2. **Failover Test Network Settings**:
   - `Failover Test ShouldReplaceIpConfiguration` - Set to "True" to modify IP settings
   - `Failover Test Network` - Network identifier for test failover
   - `Failover Test DHCP` - Set to "True" for DHCP or "False" for static IP
   - `Failover Test IP` - Static IP address (required if DHCP is False)
   - `Failover Test Subnet` - Subnet mask (required if DHCP is False)
   - `Failover Test Gateway` - Default gateway (optional)
   - `Failover Test DNS1` - Primary DNS server (optional)
   - `Failover Test DNS2` - Secondary DNS server (optional)

## Step 3: Import Updated Settings

Use the import script to apply the modified settings:

```bash
python import_vpg_settings_nics_from_csv.py \
    --zvm_address "192.168.111.20" \
    --client_id "zerto-api" \
    --client_secret "your-secret-here" \
    --csv_file "ExportedSettings_2024-03-14_12-34-56.csv" \
    --vpg_names "VpgTest1,VpgTest2" \
    --ignore_ssl
```

The script will:
1. Validate the settings in the CSV file
2. Show a summary of changes to be applied
3. Ask for confirmation before applying changes
4. Apply the changes and commit them to the VPGs

## Important Notes

1. **Backup**: Always keep a backup of the original CSV file before making changes
2. **Validation**: The import script validates settings before applying them:
   - Checks for conflicting DHCP and static IP settings
   - Verifies required fields are present
   - Ensures network identifiers are valid
3. **Safety**: The script requires explicit confirmation before applying changes
4. **Rollback**: If needed, you can re-import the original settings from the backup CSV

## Common Use Cases

1. **Bulk IP Address Changes**:
   - Export current settings
   - Update IP addresses in the CSV
   - Import modified settings

2. **Network Migration**:
   - Export current settings
   - Update network identifiers
   - Import modified settings

3. **DHCP to Static IP Conversion**:
   - Export current settings
   - Set `ShouldReplaceIpConfiguration` to "True"
   - Set `DHCP` to "False"
   - Add static IP settings
   - Import modified settings

## Troubleshooting

1. **Validation Errors**:
   - Ensure `ShouldReplaceIpConfiguration` is set to "True" when modifying IP settings
   - Check that DHCP and static IP settings are not conflicting
   - Verify all required fields are filled when using static IP

2. **Import Failures**:
   - Verify network identifiers exist in the target site
   - Check that IP addresses are in the correct format
   - Ensure you have sufficient permissions on the ZVM

3. **CSV Format Issues**:
   - Keep the original column headers
   - Don't modify the `VPG Name`, `VM Identifier`, or `NIC Identifier` columns
   - Use "True" or "False" (case-insensitive) for boolean values 
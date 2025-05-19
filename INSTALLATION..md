Installation Guide for Cuculus MeterExtension Integration for Home Assistant
This guide details the installation and setup process for the Cuculus MeterExtension Integration for Home Assistant.
Prerequisites

Home Assistant version 2025.5.2 or newer
A functioning Cuculus MeterExtension device on your network
The IP address of your Cuculus MeterExtension device

Installation via HACS (recommended)
HACS (Home Assistant Community Store) enables easy installation and updates of third-party integrations.
1. Install HACS (if not already installed)
If you haven't installed HACS yet, follow the official HACS installation guide.
2. Add Custom Repository

Open HACS in your Home Assistant
Click on the three dots in the top right corner
Select "Custom repositories"
Enter the following URL: https://github.com/ReneMronet/ha-cuculus-meterextension
Select "Integration" as the category
Click "Add"

3. Install the Integration

Go to HACS > "Integrations"
Search for "Cuculus MeterExtension"
Click on it and select "Download"
Read the information and click "Download"
Restart Home Assistant (via Settings > System > Restart)

Manual Installation
If you prefer not to use HACS, you can install the integration manually.
1. Download the Files

Visit the integration's GitHub page
Click on "Code" and then "Download ZIP"
Extract the downloaded ZIP file

2. Install in Home Assistant

Open the folder with the extracted files
Copy the entire cuculus_meterextension folder to the custom_components directory in your Home Assistant configuration folder

The path should look like: config/custom_components/cuculus_meterextension/
If the custom_components folder doesn't exist yet, create it


Restart Home Assistant

The complete directory structure should look like this:
custom_components/cuculus_meterextension/
├── __init__.py
├── config_flow.py
├── manifest.json
├── sensor.py
├── services.py
├── services.yaml
├── strings.json
├── translations/
│   └── de.json
└── logos/
    ├── logo.svg
    ├── dark_logo.svg
    └── icon.svg
Setting Up the Integration
After installation, you need to configure the integration:

Go to "Settings" > "Devices & Services" in your Home Assistant
Click on the "+ Add Integration" button (bottom right)
Search for "Cuculus MeterExtension"
Follow the configuration wizard:

Enter the IP address of your Cuculus MeterExtension device
The integration will attempt to connect and read data
Upon successful connection, all available sensors will be automatically set up



Configuration Options
After setup, you can configure additional options:

Go to "Settings" > "Devices & Services"
Find the Cuculus MeterExtension integration and click "Configure"
Here you can adjust the update interval:

Default: 60 seconds
Minimum: 10 seconds
Maximum: 3600 seconds (1 hour)



Verifying the Installation
To verify that the installation was successful:

Go to "Settings" > "Devices & Services" > "Entities"
Filter for "Cuculus" - you should see 12 sensors
Click on one of the sensors to check if it's displaying correct values

Updating the Integration
Via HACS

Open HACS in your Home Assistant
Go to "Integrations"
Check for updates (top right)
If an update is available, click on "Cuculus MeterExtension" and select "Update"
Restart Home Assistant

Manual Update

Download the latest version from GitHub
Remove the old cuculus_meterextension folder from your custom_components directory
Copy the new folder there
Restart Home Assistant

Troubleshooting Installation Issues
Problem: Integration Not Found

Check if the files are in the correct directory (custom_components/cuculus_meterextension/)
Make sure you've restarted Home Assistant after installation
Verify that the manifest.json file is properly formatted

Problem: Connection Error During Setup

Check if the IP address is correct
Test if the device is reachable: Open http://YOUR_IP/api in a browser
Check if the API response has the expected format
Check Home Assistant logs for specific error messages

Support
For issues or questions:

Create an issue on GitHub
Check Home Assistant logs under Settings > System > Logs
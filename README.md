<h1>KAIFA / Honeywell DM515 (HS330S H2LAT1) Smart Meter with Cuculus - EnergyRadar MeterExtension #1 Integration for Home Assistant</h1>

This integration connects your Cuculus MeterExtension electric meter to Home Assistant, providing real-time data on voltage, current, power, and energy consumption.
Features

Real-time energy monitoring - Voltage, current, and power for all three phases
Energy metering - Import/export values for active and reactive energy
Dashboard integration - All sensors can be easily added to the Home Assistant dashboard
Energy dashboard compatibility - Fully compatible with Home Assistant's energy dashboard
Configurable update rate - Adjustable polling intervals
User-friendly setup - Simple configuration through the Home Assistant UI

Cuculus MeterExtension #1:

![MeterExtension #1](https://github.com/user-attachments/assets/cf31232b-828a-49f7-9cfb-47d83e8427dc)

KAIFA / Honeywell Smart Meter:

![KAIFA](https://github.com/user-attachments/assets/31d9c65e-d366-4ac7-89a0-3967a34fde61)


<h2>LINKS</h2>

- Manufacturer:

https://www.cuculus.com/

https://energyradar.net/

https://energyradar.net/en/?page_id=7888


- OBIS List (German language):

https://oesterreichsenergie.at/fileadmin/user_upload/Smart_Meter-Plattform/20200201_Konzept_Kundenschnittstelle_SM.pdf


- Software (Postman) for interface request (optionally):
Just to see which values you could read out
You don’t have to register - neither for the download nor after starting the program.
It also works for this query without registration.

https://www.postman.com/


COMMAND

Raw:

{“cmd”: “meter_reading”,“id”: 0}

Send

Result:
```
{
    "meter": [
        {
            "meterid": "1ELSXXXXXXXXX",
            "data": [
                {
                    "OBIS": "1-0:32.7.0.255",
                    "scale": "-1",
                    "unit": "35",
                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "2358"
                        }
                    ]
                },
                {
                    "OBIS": "1-0:52.7.0.255",
                    "scale": "-1",
                    "unit": "35",
                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "2357"
                        }
                    ]
                },
                {
                    "OBIS": "1-0:72.7.0.255",
                    "scale": "-1",
                    "unit": "35",
                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "2364"
                        }
                    ]
                },
                {
                    "OBIS": "1-0:31.7.0.255",
                    "scale": "-2",
                    "unit": "33",
                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "568"
                        }
                    ]
                },
                {
                    "OBIS": "1-0:51.7.0.255",
                    "scale": "-2",
                    "unit": "33",
                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "572"
                        }
                    ]
                },
                {
                    "OBIS": "1-0:71.7.0.255",
                    "scale": "-2",
                    "unit": "33",
                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "573"
                        }
                    ]
                },
                {
                    "OBIS": "1-0:1.7.0.255",
                    "scale": "0",
                    "unit": "27",
                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "0"
                        }
                    ]
                },
                {
                    "OBIS": "1-0:2.7.0.255",
                    "scale": "0",
                    "unit": "27",
                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "3994"
                        }
                    ]
                },
                {
                    "OBIS": "1-0:1.8.0.255",
                    "scale": "0",
                    "unit": "30",
                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "5470178"
                        }
                    ]
                },
                {
                    "OBIS": "1-0:2.8.0.255",
                    "scale": "0",
                    "unit": "30",
                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "7640299"
                        }
                    ]
                },
                {
                    "OBIS": "1-0:3.8.0.255",
                    "scale": "0",
                    "unit": "32",
                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "4743"
                        }
                    ]
                },
                {
                    "OBIS": "1-0:4.8.0.255",
                    "scale": "0",
                    "unit": "0",

                    "entry": [
                        {
                            "ts": "1722007035",
                            "val": "6291429"
                        }
                    ]
                }
            ]
        }
    ],
    "result": "OK"
}
```
Then you can copy the following items - depending on which values you want to query - into the sensor.py.

To find out which value stands for what, compare the OBIS value with the values in the PDF file above.

```
Example: “OBIS”: “1-0:1.8.0.255”, = 1.8.0 (current drawn from the grid)
```

<h2>INSTALLATION</h2>

<h3>Option 1: Installation via HACS (recommended)</h3>

1. Make sure HACS is installed in your Home Assistant
2. Go to HACS > "Integrations"
3. Click the three dots in the top right corner and select "Custom repository"
4. Ad the URL https://github.com/ReneMronet/ha-cuculus-meterextension and select "Integration" as the category
5. Click "Add"
6. Search for "Cuculus MeterExtension" and install it
7. Restart Home Assistant

<h3>Option 2: Manual Installation</h3>h3>

1. Download the latest release
2. Extract the archive
3. Copy the cuculus_meterextension folder to the custom_components directory of your Home Assistant installation
The path should look like: config/custom_components/cuculus_meterextension/
4.Restart Home Assistant

<h3>Configuration</h3>

1. Go to Home Assistant > Settings > Devices & Services
2. Click the "+ Integration" button in the bottom right corner
3. Search for "Cuculus MeterExtension"
4. Enter the IP address of your Cuculus MeterExtension device
5. Done! The integration automatically creates all available sensors

<h3>Configuration Options</h3>
After setup, you can access configuration options:

1. Go to Settings > Devices & Services > Integrations
2. Find the Cuculus MeterExtension integration
3. Click "Configure"
4. Here you can adjust the update interval (default: 60 seconds)

<h3>Using with the Energy Dashboard</h3>h3>
The integration is optimized for use with the Home Assistant Energy Dashboard:

1. Go to Settings > Dashboards > Energy
2. Under "Electricity consumption" add the sensor sensor.cuculus_energy_import_1_8_0
3. If you have solar panels, you can add sensor.cuculus_energy_export_2_8_0 under "Return to grid"

<h3>Getting Started with the Dashboard</h3>
Here's a simple example dashboard to get started with the integration:

```
yaml

type: grid
cards:
  - type: gauge
    entity: sensor.cuculus_active_power_import_1_7_0
    name: Current Consumption
    min: 0
    max: 10000
    severity:
      green: 0
      yellow: 3000
      red: 6000
  - type: gauge
    entity: sensor.cuculus_voltage_l1
    name: Voltage L1
    min: 210
    max: 250
  - type: history-graph
    entities:
      - entity: sensor.cuculus_energy_import_1_8_0
        name: Energy Consumption
    hours_to_show: 24
    refresh_interval: 0
  - type: entities
    entities:
      - entity: sensor.cuculus_voltage_l1
      - entity: sensor.cuculus_voltage_l2
      - entity: sensor.cuculus_voltage_l3
      - entity: sensor.cuculus_current_l1
      - entity: sensor.cuculus_current_l2
      - entity: sensor.cuculus_current_l3
    title: Power Grid Overview
columns: 2
```

<h3>Available Services</h3>
The integration provides two services:

<b>cuculus_meterextension.refresh_data</b>

Immediately refreshes data from the MeterExtension device.

```
yaml

service: cuculus_meterextension.refresh_data
target:
  entity_id: sensor.cuculus_meter_id
```

<b>cuculus_meterextension.set_update_interval</b>
Sets the update interval for the MeterExtension device.

```
yaml

service: cuculus_meterextension.set_update_interval
target:
  entity_id: sensor.cuculus_meter_id
data:
  interval: 30  # seconds
```

<h3>Troubleshooting</h3>
If you're experiencing issues with the integration, check the following:

1. Connection problems

- Ensure the IP address is correct
- Check if the device is powered on and connected to the network
- Try accessing the API directly: http://YOUR_IP/api


2. Incorrect values

- Check the physical connection to the electric meter
- Restart the MeterExtension device
- Use the refresh_data service to force an update


3. Checking logs

- Increase the log level in your configuration.yaml:

```
yaml

logger:
  default: warning
  logs:
    custom_components.cuculus_meterextension: debug
```



<h3>Support</h3>

- GitHub Issues: Report a bug
- GitHub Discussions: Ask questions

<h3>License</h3>
This integration is licensed under the MIT License and is community-supported.
   

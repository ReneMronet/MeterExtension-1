<h1>KAIFA / Honeywell DM515 (HS330S H2LAT1) Smart Meter with Cuculus MeterExtension #1 in Home Assistant</h1>

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

- First install the Cuculus Meter Extension #1 as described by the manufacturer.
- Then connect the Cuculus Meter Extension #1 to your WLAN.
-If you want to find out all values from your Cuculus Meter Extension #1, install the Postman software (link above) and enter the following into your browser:

http://CUCULUS_METEREXTENSION_IP/api
(Replace CUCULUS_METEREXTENSION_IP with the IP address of your Cuculus Meter Extension #1)

- In Home Assistant, copy the files (__init__.py, sensor.py, manifest.json) with the file editor to /homeassistant/custom_components/cuculus_meterextension/
- Restart Home Assistant.
- Now you can display the values as an entity in Home Assistant.

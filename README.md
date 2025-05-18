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


- Software for interface request (Postman):
Just to see which values you could read out
You don’t have to register - neither for the download nor after starting the program.
It also works for this query without registration.

https://www.postman.com/


COMMAND

Raw:

{“cmd”: “meter_reading”,“id”: 0}

Send

Result:

...


<h2>INSTALLATION</h2>

- First install the Cuculus Meter Extension #1 as described by the manufacturer.
- Then connect the Cuculus Meter Extension #1 to your WLAN.
-If you want to find out all values from your Cuculus Meter Extension #1, install the Postman software (link above) and enter the following into your browser:

http://CUCULUS_METEREXTENSION_IP/api
(Replace CUCULUS_METEREXTENSION_IP with the IP address of your Cuculus Meter Extension #1)

- In Home Assistant, copy the files (__init__.py, sensor.py, manifest.json) with the file editor to /homeassistant/custom_components/cuculus_meterextension/
- Restart Home Assistant.
- Now you can display the values as an entity in Home Assistant.

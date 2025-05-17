import logging
import json
import requests
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import (
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
)

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=1)
RESOURCE_URL = "http://CUCULUS_METEREXTENSION_IP/api"
HEADERS = {"content-type": "application/json"}
PAYLOAD = '{"cmd": "meter_reading","id": 0}'

# Definiere die fehlenden Einheiten
UNIT_VOLT = "V"
UNIT_AMPERE = "A"
UNIT_WATT = "W"
UNIT_KILOWATT_HOUR = "kWh"
UNIT_WATT_HOUR = "Wh"

SENSORS = [
    {
        "name": "Cuculus_Power_Meter_ID",
        "unit_of_measurement": None,
        "device_class": None,
        "value_template": lambda data: data['meter'][0]['meterid'],
        "unique_id": 300,
    },
    {
        "name": "Cuculus_Power_Meter_Voltage_L1",
        "unit_of_measurement": UNIT_VOLT,
        "device_class": DEVICE_CLASS_POWER,
        "value_template": lambda data: data['meter'][0]['data'][0]['entry'][0]['val'],
        "unique_id": 301,
    },
    {
        "name": "Cuculus_Power_Meter_Voltage_L2",
        "unit_of_measurement": UNIT_VOLT,
        "device_class": DEVICE_CLASS_POWER,
        "value_template": lambda data: data['meter'][0]['data'][1]['entry'][0]['val'],
        "unique_id": 302,
    },
    {
        "name": "Cuculus_Power_Meter_Voltage_L3",
        "unit_of_measurement": UNIT_VOLT,
        "device_class": DEVICE_CLASS_POWER,
        "value_template": lambda data: data['meter'][0]['data'][2]['entry'][0]['val'],
        "unique_id": 303,
    },
    {
        "name": "Cuculus_Power_Meter_Power_L1",
        "unit_of_measurement": UNIT_AMPERE,
        "device_class": DEVICE_CLASS_POWER,
        "value_template": lambda data: data['meter'][0]['data'][3]['entry'][0]['val'],
        "unique_id": 304,
    },
    {
        "name": "Cuculus_Power_Meter_Power_L2",
        "unit_of_measurement": UNIT_AMPERE,
        "device_class": DEVICE_CLASS_POWER,
        "value_template": lambda data: data['meter'][0]['data'][4]['entry'][0]['val'],
        "unique_id": 305,
    },
    {
        "name": "Cuculus_Power_Meter_Power_L3",
        "unit_of_measurement": UNIT_AMPERE,
        "device_class": DEVICE_CLASS_POWER,
        "value_template": lambda data: data['meter'][0]['data'][5]['entry'][0]['val'],
        "unique_id": 306,
    },
    {
        "name": "Cuculus_Power_Meter_1.7.0",
        "unit_of_measurement": UNIT_WATT,
        "device_class": DEVICE_CLASS_ENERGY,
        "value_template": lambda data: data['meter'][0]['data'][6]['entry'][0]['val'],
        "unique_id": 307,
    },
    {
        "name": "Cuculus_Power_Meter_2.7.0",
        "unit_of_measurement": UNIT_WATT,
        "device_class": DEVICE_CLASS_ENERGY,
        "value_template": lambda data: data['meter'][0]['data'][7]['entry'][0]['val'],
        "unique_id": 308,
    },
    {
        "name": "Cuculus_Patsch_Power_Meter_1.8.0",
        "unit_of_measurement": UNIT_KILOWATT_HOUR,
        "device_class": DEVICE_CLASS_ENERGY,
        "value_template": lambda data: int(data['meter'][0]['data'][8]['entry'][0]['val']) / 1000,
        "unique_id": 309,
    },
    {
        "name": "Cuculus_Patsch_Power_Meter_2.8.0",
        "unit_of_measurement": UNIT_KILOWATT_HOUR,
        "device_class": DEVICE_CLASS_ENERGY,
        "value_template": lambda data: int(data['meter'][0]['data'][9]['entry'][0]['val']) / 1000,
        "unique_id": 310,
    },
    {
        "name": "Cuculus_Power_Meter_3.8.0",
        "unit_of_measurement": UNIT_WATT_HOUR,
        "device_class": DEVICE_CLASS_ENERGY,
        "value_template": lambda data: data['meter'][0]['data'][10]['entry'][0]['val'],
        "unique_id": 311,
    },
    {
        "name": "Cuculus_Power_Meter_4.8.0",
        "unit_of_measurement": UNIT_WATT_HOUR,
        "device_class": DEVICE_CLASS_ENERGY,
        "value_template": lambda data: data['meter'][0]['data'][11]['entry'][0]['val'],
        "unique_id": 312,
    },
]

def get_meter_data():
    try:
        response = requests.post(RESOURCE_URL, headers=HEADERS, data=PAYLOAD)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        _LOGGER.error(f"Error fetching data from {RESOURCE_URL}: {e}")
        return None

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    meter_data = get_meter_data()
    if meter_data is not None:
        sensors = [CuculusMeterSensor(sensor, meter_data) for sensor in SENSORS]
        async_add_entities(sensors, True)

class CuculusMeterSensor(SensorEntity):
    def __init__(self, sensor_config, meter_data):
        self._name = sensor_config["name"]
        self._unit_of_measurement = sensor_config["unit_of_measurement"]
        self._device_class = sensor_config["device_class"]
        self._unique_id = sensor_config["unique_id"]
        self._value_template = sensor_config["value_template"]
        self._state = None
        self._meter_data = meter_data

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    @property
    def device_class(self):
        return self._device_class

    async def async_update(self):
        self._meter_data = get_meter_data()
        if self._meter_data is not None:
            self._state = self._value_template(self._meter_data)

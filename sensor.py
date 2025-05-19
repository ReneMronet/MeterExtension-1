"""Support for Cuculus MeterExtension sensors."""
import logging
import json
import requests
from datetime import timedelta

from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    UnitOfElectricPotential, 
    UnitOfElectricCurrent,
    UnitOfPower,   
    UnitOfEnergy,  
    CONF_HOST,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

# Define the sensor specifications
SENSORS = [
    {
        "name": "Meter ID",
        "unit_of_measurement": None,
        "device_class": None,
        "state_class": None,
        "value_template": lambda data: data['meter'][0]['meterid'],
        "unique_id_suffix": "meter_id",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Voltage L1",
        "unit_of_measurement": UnitOfElectricPotential.VOLT,
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
        "value_template": lambda data: data['meter'][0]['data'][0]['entry'][0]['val'],
        "unique_id_suffix": "voltage_l1",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Voltage L2",
        "unit_of_measurement": UnitOfElectricPotential.VOLT,
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
        "value_template": lambda data: data['meter'][0]['data'][1]['entry'][0]['val'],
        "unique_id_suffix": "voltage_l2",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Voltage L3",
        "unit_of_measurement": UnitOfElectricPotential.VOLT,
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
        "value_template": lambda data: data['meter'][0]['data'][2]['entry'][0]['val'],
        "unique_id_suffix": "voltage_l3",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Current L1",
        "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "value_template": lambda data: data['meter'][0]['data'][3]['entry'][0]['val'],
        "unique_id_suffix": "current_l1",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Current L2",
        "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "value_template": lambda data: data['meter'][0]['data'][4]['entry'][0]['val'],
        "unique_id_suffix": "current_l2",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Current L3",
        "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
        "value_template": lambda data: data['meter'][0]['data'][5]['entry'][0]['val'],
        "unique_id_suffix": "current_l3",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Active Power Import (1.7.0)",
        "unit_of_measurement": UnitOfPower.WATT,
        "device_class": SensorDeviceClass.POWER,
        "state_class": SensorStateClass.MEASUREMENT,
        "value_template": lambda data: data['meter'][0]['data'][6]['entry'][0]['val'],
        "unique_id_suffix": "active_power_import",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Active Power Export (2.7.0)",
        "unit_of_measurement": UnitOfPower.WATT,
        "device_class": SensorDeviceClass.POWER,
        "state_class": SensorStateClass.MEASUREMENT,
        "value_template": lambda data: data['meter'][0]['data'][7]['entry'][0]['val'],
        "unique_id_suffix": "active_power_export",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Energy Import (1.8.0)",
        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "value_template": lambda data: int(data['meter'][0]['data'][8]['entry'][0]['val']) / 1000,
        "unique_id_suffix": "energy_import",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Energy Export (2.8.0)",
        "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "value_template": lambda data: int(data['meter'][0]['data'][9]['entry'][0]['val']) / 1000,
        "unique_id_suffix": "energy_export",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Reactive Energy Import (3.8.0)",
        "unit_of_measurement": UnitOfEnergy.WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "value_template": lambda data: data['meter'][0]['data'][10]['entry'][0]['val'],
        "unique_id_suffix": "reactive_energy_import",
        "entity_registry_enabled_default": True,
    },
    {
        "name": "Reactive Energy Export (4.8.0)",
        "unit_of_measurement": UnitOfEnergy.WATT_HOUR,
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "value_template": lambda data: data['meter'][0]['data'][11]['entry'][0]['val'],
        "unique_id_suffix": "reactive_energy_export",
        "entity_registry_enabled_default": True,
    },
]


async def get_meter_data(hass, host):
    """Get meter data from the MeterExtension device."""
    resource_url = f"http://{host}/api"
    headers = {"content-type": "application/json"}
    payload = '{"cmd": "meter_reading","id": 0}'
    
    try:
        # Use the async executor to prevent blocking the event loop
        response = await hass.async_add_executor_job(
            lambda: requests.post(resource_url, headers=headers, data=payload, timeout=10)
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as ex:
        _LOGGER.error("Error fetching data from %s: %s", resource_url, ex)
        return None


async def async_setup_entry(
    hass: HomeAssistant, 
    config_entry: ConfigEntry, 
    async_add_entities: AddEntitiesCallback
):
    """Set up the Cuculus MeterExtension sensors from a config entry."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    host = config_entry.data[CONF_HOST]
    
    if not coordinator.data:
        _LOGGER.error("Failed to retrieve data from MeterExtension at %s", host)
        return
    
    # Get the meter ID for device info
    meter_id = coordinator.data['meter'][0]['meterid']
    
    # Create entities
    entities = []
    for sensor_config in SENSORS:
        entities.append(
            CuculusMeterSensor(
                coordinator,
                sensor_config,
                host,
                meter_id,
                config_entry.entry_id,
            )
        )
    
    async_add_entities(entities)


class CuculusMeterSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Cuculus MeterExtension sensor."""

    def __init__(self, coordinator, sensor_config, host, meter_id, entry_id):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._sensor_config = sensor_config
        self._host = host
        self._meter_id = meter_id
        self._entry_id = entry_id
        
        # Entity properties
        self._attr_name = f"Cuculus {sensor_config['name']}"
        self._attr_unique_id = f"{DOMAIN}_{host}_{sensor_config['unique_id_suffix']}"
        self._attr_native_unit_of_measurement = sensor_config["unit_of_measurement"]
        self._attr_device_class = sensor_config["device_class"]
        self._attr_state_class = sensor_config["state_class"]
        self._attr_entity_registry_enabled_default = sensor_config["entity_registry_enabled_default"]
        
        # Device info
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"{DOMAIN}_{host}")},
            name=f"Cuculus MeterExtension ({meter_id})",
            manufacturer="Cuculus",
            model="MeterExtension",
            sw_version="1.0.0",
            configuration_url=f"http://{host}",
        )

    @property
    def native_value(self):
        """Return the state of the sensor."""
        if not self.coordinator.data:
            return None
        try:
            return self._sensor_config["value_template"](self.coordinator.data)
        except (KeyError, IndexError, ValueError) as ex:
            _LOGGER.error("Error extracting value: %s", ex)
            return None
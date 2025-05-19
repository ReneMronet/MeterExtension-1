"""Config flow for Cuculus MeterExtension integration."""
import logging
import voluptuous as vol
import requests

from homeassistant import config_entries
from homeassistant.core import HomeAssistant, callback
from homeassistant.const import CONF_HOST
import homeassistant.helpers.config_validation as cv

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_HOST): cv.string,
})

async def validate_input(hass: HomeAssistant, data):
    """Validate the user input allows us to connect."""
    host = data[CONF_HOST]
    
    resource_url = f"http://{host}/api"
    headers = {"content-type": "application/json"}
    payload = '{"cmd": "meter_reading","id": 0}'
    
    try:
        # Use async_add_executor_job to avoid blocking calls
        response = await hass.async_add_executor_job(
            lambda: requests.post(resource_url, headers=headers, data=payload, timeout=10)
        )
        response.raise_for_status()
        meter_data = response.json()
        
        # Check if meter_data has the expected structure
        if "meter" not in meter_data or not meter_data["meter"]:
            raise ValueError("Invalid data received from MeterExtension")
        
        # Extract meter ID for title
        meter_id = meter_data["meter"][0]["meterid"]
        title = f"Cuculus MeterExtension ({meter_id})"
        
        return {"title": title}
    except requests.exceptions.RequestException as ex:
        _LOGGER.error("Error connecting to Cuculus MeterExtension: %s", ex)
        raise ValueError("Cannot connect to specified Cuculus MeterExtension") from ex


class CuculusMeterExtensionConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Cuculus MeterExtension."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
                
                # Check if device already configured
                await self.async_set_unique_id(f"cuculus_meter_{user_input[CONF_HOST]}")
                self._abort_if_unique_id_configured()
                
                return self.async_create_entry(
                    title=info["title"],
                    data=user_input
                )
            except ValueError as ex:
                _LOGGER.error("Validation error: %s", ex)
                errors["base"] = "cannot_connect"
            except Exception as ex:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception: %s", ex)
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user", 
            data_schema=DATA_SCHEMA, 
            errors=errors
        )
    
    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return CuculusOptionsFlowHandler(config_entry)


class CuculusOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for Cuculus MeterExtension integration."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        options = {
            vol.Optional("scan_interval", default=self.config_entry.options.get("scan_interval", 60)): vol.All(
                vol.Coerce(int), vol.Range(min=10, max=3600)
            ),
        }

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(options),
        )
"""Config flow for Cuculus MeterExtension integration."""
import logging
import voluptuous as vol
import requests

from homeassistant import config_entries
from homeassistant.core import HomeAssistant, callback
from homeassistant.const import CONF_HOST
import homeassistant.helpers.config_validation as cv

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_HOST): cv.string,
})

async def validate_input(hass: HomeAssistant, data):
    """Validate the user input allows us to connect."""
    host = data[CONF_HOST]
    
    resource_url = f"http://{host}/api"
    headers = {"content-type": "application/json"}
    payload = '{"cmd": "meter_reading","id": 0}'
    
    try:
        response = await hass.async_add_executor_job(
            lambda: requests.post(resource_url, headers=headers, data=payload, timeout=10)
        )
        response.raise_for_status()
        meter_data = response.json()
        
        # Check if meter_data has the expected structure
        if "meter" not in meter_data or not meter_data["meter"]:
            raise ValueError("Invalid data received from MeterExtension")
        
        # Extract meter ID for title
        meter_id = meter_data["meter"][0]["meterid"]
        title = f"Cuculus MeterExtension ({meter_id})"
        
        return {"title": title}
    except requests.exceptions.RequestException as ex:
        _LOGGER.error("Error connecting to Cuculus MeterExtension: %s", ex)
        raise ValueError("Cannot connect to specified Cuculus MeterExtension") from ex


class CuculusMeterExtensionConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Cuculus MeterExtension."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
                
                # Check if device already configured
                await self.async_set_unique_id(f"cuculus_meter_{user_input[CONF_HOST]}")
                self._abort_if_unique_id_configured()
                
                return self.async_create_entry(
                    title=info["title"],
                    data=user_input
                )
            except ValueError as ex:
                _LOGGER.error("Validation error: %s", ex)
                errors["base"] = "cannot_connect"
            except Exception as ex:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception: %s", ex)
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user", 
            data_schema=DATA_SCHEMA, 
            errors=errors
        )
    
    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return CuculusOptionsFlowHandler(config_entry)


class CuculusOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for Cuculus MeterExtension integration."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        options = {
            vol.Optional("scan_interval", default=self.config_entry.options.get("scan_interval", 60)): vol.All(
                vol.Coerce(int), vol.Range(min=10, max=3600)
            ),
        }

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(options),
        )
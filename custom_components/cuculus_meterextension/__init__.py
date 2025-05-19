"""The Cuculus MeterExtension integration."""
import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

DOMAIN = "cuculus_meterextension"
PLATFORMS = [Platform.SENSOR]

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Cuculus MeterExtension component."""
    _LOGGER.info("Setting up Cuculus MeterExtension integration")
    hass.data.setdefault(DOMAIN, {})
    
    # Set up services
    from .services import async_setup_services
    await async_setup_services(hass)
    
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Cuculus MeterExtension from a config entry."""
    _LOGGER.info("Setting up Cuculus MeterExtension from config entry")
    host = entry.data[CONF_HOST]
    
    from .sensor import get_meter_data
    
    # Create update coordinator
    scan_interval = entry.options.get("scan_interval", 60)
    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"Cuculus MeterExtension ({host})",
        update_method=lambda: get_meter_data(hass, host),
        update_interval=timedelta(seconds=scan_interval),
    )
    
    # Fetch initial data
    await coordinator.async_config_entry_first_refresh()
    
    # Store coordinator in hass data
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator
    
    # Set up all platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    # Add update listener for options
    entry.async_on_unload(entry.add_update_listener(update_listener))
    
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
        
    return unload_ok


async def update_listener(hass: HomeAssistant, entry: ConfigEntry):
    """Update listener for options."""
    await hass.config_entries.async_reload(entry.entry_id)
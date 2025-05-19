"""Services for Cuculus MeterExtension."""
import logging
from datetime import timedelta

from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_component import EntityComponent

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_services(hass: HomeAssistant) -> None:
    """Set up services for Cuculus MeterExtension integration."""
    
    component = EntityComponent(_LOGGER, DOMAIN, hass)
    
    @callback
    async def async_refresh_data(call: ServiceCall) -> None:
        """Service to refresh data from MeterExtension device."""
        entity_ids = call.data.get("entity_id", [])
        target_entities = []
        
        # Get all coordinator entities 
        if entity_ids:
            entities = component.entities
            target_entities = [
                entity for entity in entities
                if entity.entity_id in entity_ids
            ]
        
        if not target_entities:
            # Use all entities if none specified
            for entry_id, coordinator in hass.data[DOMAIN].items():
                await coordinator.async_refresh()
                _LOGGER.debug("Refreshed all Cuculus MeterExtension entities for %s", entry_id)
            return
        
        # Get unique coordinators for targeted entities
        coordinators = set()
        for entity in target_entities:
            if hasattr(entity, "coordinator"):
                coordinators.add(entity.coordinator)
                
        # Refresh each coordinator
        for coordinator in coordinators:
            await coordinator.async_refresh()
            _LOGGER.debug("Refreshed Cuculus MeterExtension entities via service call")
    
    @callback
    async def async_set_update_interval(call: ServiceCall) -> None:
        """Service to set update interval for MeterExtension device."""
        entity_ids = call.data.get("entity_id", [])
        interval = call.data.get("interval")
        
        if interval is None or interval < 10:
            _LOGGER.error("Invalid interval value: %s. Must be >= 10 seconds", interval)
            return
            
        target_entities = []
        
        # Get all coordinator entities
        if entity_ids:
            entities = component.entities
            target_entities = [
                entity for entity in entities
                if entity.entity_id in entity_ids
            ]
        
        if not target_entities:
            # Use all entities if none specified
            for entry_id, coordinator in hass.data[DOMAIN].items():
                coordinator.update_interval = timedelta(seconds=interval)
                _LOGGER.debug(
                    "Set update interval to %s seconds for all Cuculus MeterExtension entities for %s", 
                    interval, 
                    entry_id
                )
            return
        
        # Get unique coordinators for targeted entities
        coordinators = set()
        for entity in target_entities:
            if hasattr(entity, "coordinator"):
                coordinators.add(entity.coordinator)
                
        # Set interval for each coordinator
        for coordinator in coordinators:
            coordinator.update_interval = timedelta(seconds=interval)
            _LOGGER.debug(
                "Set update interval to %s seconds for Cuculus MeterExtension entities via service call", 
                interval
            )
    
    # Register services
    hass.services.async_register(
        DOMAIN, 
        "refresh_data", 
        async_refresh_data
    )
    
    hass.services.async_register(
        DOMAIN, 
        "set_update_interval", 
        async_set_update_interval
    )
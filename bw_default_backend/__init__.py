__all__ = (
    "Activity",
    "catalogue",
    "CharacterizationFactor",
    "Collection",
    "config",
    "create",
    "delete",
    "Exchange",
    "Flow",
    "Geocollection",
    "label_mapping",
    "Location",
    "Method",
    "replace",
    "UncertaintyType",
    "update",
    "write_data",
)

__version__ = (0, 1)

from .backend import Config

config = Config()

from .schema import (
    Activity,
    Collection,
    collections,
    Exchange,
    Flow,
    Geocollection,
    Location,
    Method,
    CharacterizationFactor,
    UncertaintyType,
)

label_mapping = {
    "uncertainty types": UncertaintyType,
    "geocollections": Geocollection,
    "locations": Location,
    "collections": Collection,
    "flows": Flow,
    "methods": Method,
    "characterization factors": CharacterizationFactor,
    "activities": Activity,
    "exchanges": Exchange,
}

from brightway_projects import backend_mapping

backend_mapping["default"] = config

from .io import catalogue, create, delete, replace, update

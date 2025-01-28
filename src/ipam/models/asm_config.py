# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a Universal DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class ASMConfig(BaseModel):
    """
    The __ASMConfig__ object represents Automated Scope Management configuration.
    """ # noqa: E501
    asm_threshold: Optional[StrictInt] = Field(
        default=90,
        description=
        "ASM shows the number of addresses forecast to be used _forecast_period_ days in the future, if it is greater than _asm_threshold_ percent * _dhcp_total_ (see _dhcp_utilization_) then the subnet is flagged."
    )
    enable: Optional[StrictBool] = Field(
        default=True,
        description="Indicates if Automated Scope Management is enabled.")
    enable_notification: Optional[StrictBool] = Field(
        default=True,
        description="Indicates if ASM should send notifications to the user.")
    forecast_period: Optional[StrictInt] = Field(
        default=14, description="The forecast period in days.")
    growth_factor: Optional[StrictInt] = Field(
        default=20,
        description=
        "Indicates the growth in the number or percentage of IP addresses.")
    growth_type: Optional[StrictStr] = Field(
        default='percent',
        description="The type of factor to use: _percent_ or _count_.")
    history: Optional[StrictInt] = Field(
        default=30,
        description=
        "The minimum amount of history needed before ASM can run on this subnet."
    )
    min_total: Optional[StrictInt] = Field(
        default=10,
        description=
        "The minimum size of range needed for ASM to run on this subnet.")
    min_unused: Optional[StrictInt] = Field(
        default=10,
        description=
        "The minimum percentage of addresses that must be available outside of the DHCP ranges and fixed addresses when making a suggested change.."
    )
    reenable_date: Optional[datetime] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "asm_threshold", "enable", "enable_notification", "forecast_period",
        "growth_factor", "growth_type", "history", "min_total", "min_unused",
        "reenable_date"
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ASMConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ASMConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asm_threshold":
            obj.get("asm_threshold")
            if obj.get("asm_threshold") is not None else 90,
            "enable":
            obj.get("enable") if obj.get("enable") is not None else True,
            "enable_notification":
            obj.get("enable_notification")
            if obj.get("enable_notification") is not None else True,
            "forecast_period":
            obj.get("forecast_period")
            if obj.get("forecast_period") is not None else 14,
            "growth_factor":
            obj.get("growth_factor")
            if obj.get("growth_factor") is not None else 20,
            "growth_type":
            obj.get("growth_type")
            if obj.get("growth_type") is not None else 'percent',
            "history":
            obj.get("history") if obj.get("history") is not None else 30,
            "min_total":
            obj.get("min_total") if obj.get("min_total") is not None else 10,
            "min_unused":
            obj.get("min_unused") if obj.get("min_unused") is not None else 10,
            "reenable_date":
            obj.get("reenable_date")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

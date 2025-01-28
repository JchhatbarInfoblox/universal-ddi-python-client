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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class ASM(BaseModel):
    """
    The __ASM__ object is a synthetic object representing the suggestions from the Automated Scope Management suggestion engine for expanding subnet or range.
    """ # noqa: E501
    back_end: Optional[StrictStr] = Field(
        default=None,
        description="The end IP address when adding to the back.")
    back_start: Optional[StrictStr] = Field(
        default=None,
        description="The start IP address when adding to the back.")
    both_end: Optional[StrictStr] = Field(
        default=None,
        description="The end IP address when adding to the back.")
    both_start: Optional[StrictStr] = Field(
        default=None,
        description="The start IP address when adding to both front and back.")
    front_end: Optional[StrictStr] = Field(
        default=None,
        description="The end IP address when adding to the front.")
    front_start: Optional[StrictStr] = Field(
        default=None,
        description="The start IP address when adding to the front.")
    growth: Optional[StrictInt] = Field(
        default=None,
        description=
        "Calculated number of addresses to grow range; its value is determined by asm_config growth factor, type, and min_unused after the expansion."
    )
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    lookahead: Optional[StrictInt] = Field(
        default=None,
        description=
        "Either the value from the ASM configuration or -1 if the estimate is that utilization will not exceed the threshold."
    )
    range_end: Optional[StrictStr] = Field(
        default=None, description="The end IP address of the range.")
    range_id: Optional[StrictStr] = Field(
        default=None, description="The resource identifier.")
    range_start: Optional[StrictStr] = Field(
        default=None, description="The start IP address of the range.")
    subnet_address: Optional[StrictStr] = Field(
        default=None, description="The suggested subnet expansion.")
    subnet_cidr: Optional[StrictInt] = Field(
        default=None, description="The CIDR of the subnet.")
    subnet_direction: Optional[StrictStr] = Field(
        default=None,
        description=
        "Indicates where the subnet may expand. As the subnet can only be expanded by one bit at a time, it can only grow in one of the two directions. It is set to _none_ if the subnet can't be expanded.  Valid values are: * _front_ * _back_ * _none_"
    )
    subnet_id: StrictStr = Field(description="The resource identifier.")
    subnet_range: Optional[StrictStr] = Field(
        default=None, description="The resource identifier.")
    subnet_range_end: Optional[StrictStr] = Field(
        default=None,
        description="The suggested new range end in expanded subnet.")
    subnet_range_start: Optional[StrictStr] = Field(
        default=None,
        description="The suggested new range start in expanded subnet.")
    suppress: Optional[StrictStr] = Field(
        default=None,
        description=
        "Indicates if future notifications for this subnet should be suppressed.  Valid values are: * _no_ * _time_ * _permanent_  If set to _permanent_ notifications are suppressed until the administrator modifies the configuration for the subnet. If set to _time_ notifications are suppressed until the specified time. Defaults to _no_."
    )
    suppress_time: Optional[StrictInt] = Field(
        default=None,
        description=
        "The time duration in days to suppress the notifications for this subnet."
    )
    threshold_utilization: Optional[StrictInt] = Field(
        default=None,
        description="The utilization threshold as per ASM configuration.")
    update: Optional[StrictStr] = Field(
        default=None,
        description=
        "The object to update.  Valid values are: * _range_ * _subnet_ * _none_"
    )
    utilization: Optional[StrictInt] = Field(
        default=None,
        description="The utilization of DHCP addresses in the subnet.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "back_end", "back_start", "both_end", "both_start", "front_end",
        "front_start", "growth", "id", "lookahead", "range_end", "range_id",
        "range_start", "subnet_address", "subnet_cidr", "subnet_direction",
        "subnet_id", "subnet_range", "subnet_range_end", "subnet_range_start",
        "suppress", "suppress_time", "threshold_utilization", "update",
        "utilization"
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
        """Create an instance of ASM from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "back_end",
            "back_start",
            "both_end",
            "both_start",
            "front_end",
            "front_start",
            "growth",
            "id",
            "lookahead",
            "subnet_address",
            "subnet_cidr",
            "subnet_direction",
            "subnet_range_end",
            "subnet_range_start",
            "threshold_utilization",
            "utilization",
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
        """Create an instance of ASM from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "back_end":
            obj.get("back_end"),
            "back_start":
            obj.get("back_start"),
            "both_end":
            obj.get("both_end"),
            "both_start":
            obj.get("both_start"),
            "front_end":
            obj.get("front_end"),
            "front_start":
            obj.get("front_start"),
            "growth":
            obj.get("growth"),
            "id":
            obj.get("id"),
            "lookahead":
            obj.get("lookahead"),
            "range_end":
            obj.get("range_end"),
            "range_id":
            obj.get("range_id"),
            "range_start":
            obj.get("range_start"),
            "subnet_address":
            obj.get("subnet_address"),
            "subnet_cidr":
            obj.get("subnet_cidr"),
            "subnet_direction":
            obj.get("subnet_direction"),
            "subnet_id":
            obj.get("subnet_id"),
            "subnet_range":
            obj.get("subnet_range"),
            "subnet_range_end":
            obj.get("subnet_range_end"),
            "subnet_range_start":
            obj.get("subnet_range_start"),
            "suppress":
            obj.get("suppress"),
            "suppress_time":
            obj.get("suppress_time"),
            "threshold_utilization":
            obj.get("threshold_utilization"),
            "update":
            obj.get("update"),
            "utilization":
            obj.get("utilization")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

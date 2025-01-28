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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ipam.models.dhcp_packet_stats import DHCPPacketStats
from ipam.models.ha_group import HAGroup
from ipam.models.host import Host
from ipam.models.subnet import Subnet
from typing import Optional, Set
from typing_extensions import Self


class HostAssociationsResponse(BaseModel):
    """
    The response format to retrieve __HAGroup__, __Subnet__ and __DHCPPacketStats__ objects associated with the DHCP __Host__ object. The host in question is also included in the output, for the convenience reasons.
    """ # noqa: E501
    dhcp_pkt_stats: Optional[DHCPPacketStats] = Field(
        default=None, description="The DHCP packets statistics.")
    ha_groups: Optional[List[HAGroup]] = Field(
        default=None, description="The list of HA groups.")
    host: Optional[Host] = Field(
        default=None,
        description=
        "The host for which the associated objects, subnets and HA groups, are returned."
    )
    subnets: Optional[List[Subnet]] = Field(default=None,
                                            description="The list of subnets.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "dhcp_pkt_stats", "ha_groups", "host", "subnets"
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
        """Create an instance of HostAssociationsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dhcp_pkt_stats
        if self.dhcp_pkt_stats:
            _dict['dhcp_pkt_stats'] = self.dhcp_pkt_stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ha_groups (list)
        _items = []
        if self.ha_groups:
            for _item in self.ha_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ha_groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of host
        if self.host:
            _dict['host'] = self.host.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in subnets (list)
        _items = []
        if self.subnets:
            for _item in self.subnets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subnets'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HostAssociationsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dhcp_pkt_stats":
            DHCPPacketStats.from_dict(obj["dhcp_pkt_stats"])
            if obj.get("dhcp_pkt_stats") is not None else None,
            "ha_groups":
            [HAGroup.from_dict(_item) for _item in obj["ha_groups"]]
            if obj.get("ha_groups") is not None else None,
            "host":
            Host.from_dict(obj["host"])
            if obj.get("host") is not None else None,
            "subnets": [Subnet.from_dict(_item) for _item in obj["subnets"]]
            if obj.get("subnets") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

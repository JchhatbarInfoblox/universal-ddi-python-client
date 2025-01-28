# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a Universal DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured Universal DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

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
from dns_config.models.inheritance2_inherited_bool import Inheritance2InheritedBool
from dns_config.models.inherited_acl_items import InheritedACLItems
from dns_config.models.inherited_zone_authority import InheritedZoneAuthority
from typing import Optional, Set
from typing_extensions import Self


class AuthZoneInheritance(BaseModel):
    """
    AuthZoneInheritance
    """

  # noqa: E501
    gss_tsig_enabled: Optional[Inheritance2InheritedBool] = Field(
        default=None,
        description=
        "Optional. Field config for _gss_tsig_enabled_ field from _AuthZone_ object."
    )
    notify: Optional[Inheritance2InheritedBool] = Field(
        default=None,
        description="Field config for _notify_ field from _AuthZone_ object.")
    query_acl: Optional[InheritedACLItems] = Field(
        default=None,
        description=
        "Optional. Field config for _query_acl_ field from _AuthZone_ object.")
    transfer_acl: Optional[InheritedACLItems] = Field(
        default=None,
        description=
        "Optional. Field config for _transfer_acl_ field from _AuthZone_ object."
    )
    update_acl: Optional[InheritedACLItems] = Field(
        default=None,
        description=
        "Optional. Field config for _update_acl_ field from _AuthZone_ object."
    )
    use_forwarders_for_subzones: Optional[Inheritance2InheritedBool] = Field(
        default=None,
        description=
        "Optional. Field config for _use_forwarders_for_subzones_ field from _AuthZone_ object."
    )
    zone_authority: Optional[InheritedZoneAuthority] = Field(
        default=None,
        description=
        "Optional. Field config for _zone_authority_ field from _AuthZone_ object."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "gss_tsig_enabled", "notify", "query_acl", "transfer_acl",
        "update_acl", "use_forwarders_for_subzones", "zone_authority"
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
        """Create an instance of AuthZoneInheritance from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of gss_tsig_enabled
        if self.gss_tsig_enabled:
            _dict['gss_tsig_enabled'] = self.gss_tsig_enabled.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notify
        if self.notify:
            _dict['notify'] = self.notify.to_dict()
        # override the default output from pydantic by calling `to_dict()` of query_acl
        if self.query_acl:
            _dict['query_acl'] = self.query_acl.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transfer_acl
        if self.transfer_acl:
            _dict['transfer_acl'] = self.transfer_acl.to_dict()
        # override the default output from pydantic by calling `to_dict()` of update_acl
        if self.update_acl:
            _dict['update_acl'] = self.update_acl.to_dict()
        # override the default output from pydantic by calling `to_dict()` of use_forwarders_for_subzones
        if self.use_forwarders_for_subzones:
            _dict[
                'use_forwarders_for_subzones'] = self.use_forwarders_for_subzones.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of zone_authority
        if self.zone_authority:
            _dict['zone_authority'] = self.zone_authority.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthZoneInheritance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gss_tsig_enabled":
            Inheritance2InheritedBool.from_dict(obj["gss_tsig_enabled"])
            if obj.get("gss_tsig_enabled") is not None else None,
            "notify":
            Inheritance2InheritedBool.from_dict(obj["notify"])
            if obj.get("notify") is not None else None,
            "query_acl":
            InheritedACLItems.from_dict(obj["query_acl"])
            if obj.get("query_acl") is not None else None,
            "transfer_acl":
            InheritedACLItems.from_dict(obj["transfer_acl"])
            if obj.get("transfer_acl") is not None else None,
            "update_acl":
            InheritedACLItems.from_dict(obj["update_acl"])
            if obj.get("update_acl") is not None else None,
            "use_forwarders_for_subzones":
            Inheritance2InheritedBool.from_dict(
                obj["use_forwarders_for_subzones"])
            if obj.get("use_forwarders_for_subzones") is not None else None,
            "zone_authority":
            InheritedZoneAuthority.from_dict(obj["zone_authority"])
            if obj.get("zone_authority") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

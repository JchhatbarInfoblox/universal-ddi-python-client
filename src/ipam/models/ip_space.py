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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from ipam.models.asm_config import ASMConfig
from ipam.models.dhcp_config import DHCPConfig
from ipam.models.ip_space_inheritance import IPSpaceInheritance
from ipam.models.option_item import OptionItem
from ipam.models.utilization import Utilization
from ipam.models.utilization_threshold import UtilizationThreshold
from ipam.models.utilization_v6 import UtilizationV6
from typing import Optional, Set
from typing_extensions import Self


class IPSpace(BaseModel):
    """
    An __IPSpace__ object (_ipam/ip_space_) allows customers to represent their entire managed address space with no collision. A collision arises when two or more block of addresses overlap partially or fully.
    """ # noqa: E501
    asm_config: Optional[ASMConfig] = Field(
        default=None,
        description=
        "The Automated Scope Management configuration for the IP space.")
    asm_scope_flag: Optional[StrictInt] = Field(
        default=None,
        description=
        "The number of times the automated scope management usage limits have been exceeded for any of the subnets in this IP space."
    )
    comment: Optional[StrictStr] = Field(
        default=None,
        description=
        "The description for the IP space. May contain 0 to 1024 characters. Can include UTF-8."
    )
    compartment_id: Optional[StrictStr] = Field(
        default=None,
        description=
        "The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty."
    )
    created_at: Optional[datetime] = Field(
        default=None, description="Time when the object has been created.")
    ddns_client_update: Optional[StrictStr] = Field(
        default='client',
        description=
        "Controls who does the DDNS updates.  Valid values are: * _client_: DHCP server updates DNS if requested by client. * _server_: DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates. * _ignore_: DHCP server always updates DNS, even if the client says not to. * _over_client_update_: Same as _server_. DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates. * _over_no_update_: DHCP server updates DNS even if the client requests that no updates be done. If the client requests to do the update, DHCP server allows it.  Defaults to _client_."
    )
    ddns_conflict_resolution_mode: Optional[StrictStr] = Field(
        default='check_with_dhcid',
        description=
        "The mode used for resolving conflicts while performing DDNS updates.  Valid values are: * _check_with_dhcid_: It includes adding a DHCID record and checking that record via conflict detection as per RFC 4703. * _no_check_with_dhcid_: This will ignore conflict detection but add a DHCID record when creating/updating an entry. * _check_exists_with_dhcid_: This will check if there is an existing DHCID record but does not verify the value of the record matches the update. This will also update the DHCID record for the entry. * _no_check_without_dhcid_: This ignores conflict detection and will not add a DHCID record when creating/updating a DDNS entry.  Defaults to _check_with_dhcid_."
    )
    ddns_domain: Optional[StrictStr] = Field(
        default=None,
        description=
        "The domain suffix for DDNS updates. FQDN, may be empty.  Defaults to empty."
    )
    ddns_generate_name: Optional[StrictBool] = Field(
        default=False,
        description=
        "Indicates if DDNS needs to generate a hostname when not supplied by the client.  Defaults to _false_."
    )
    ddns_generated_prefix: Optional[StrictStr] = Field(
        default='myhost',
        description=
        "The prefix used in the generation of an FQDN.  When generating a name, DHCP server will construct the name in the format: [ddns-generated-prefix]-[address-text].[ddns-qualifying-suffix]. where address-text is simply the lease IP address converted to a hyphenated string.  Defaults to \"myhost\"."
    )
    ddns_send_updates: Optional[StrictBool] = Field(
        default=True,
        description=
        "Determines if DDNS updates are enabled at the IP space level. Defaults to _true_."
    )
    ddns_ttl_percent: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description=
        "DDNS TTL value - to be calculated as a simple percentage of the lease's lifetime, using the parameter's value as the percentage. It is specified as a percentage (e.g. 25, 75). Defaults to unspecified."
    )
    ddns_update_on_renew: Optional[StrictBool] = Field(
        default=False,
        description=
        "Instructs the DHCP server to always update the DNS information when a lease is renewed even if its DNS information has not changed.  Defaults to _false_."
    )
    ddns_use_conflict_resolution: Optional[StrictBool] = Field(
        default=True,
        description=
        "When true, DHCP server will apply conflict resolution, as described in RFC 4703, when attempting to fulfill the update request.  When false, DHCP server will simply attempt to update the DNS entries per the request, regardless of whether or not they conflict with existing entries owned by other DHCP4 clients.  Defaults to _true_."
    )
    default_realms: Optional[List[StrictStr]] = Field(
        default=None, description="Reserved for future use.")
    dhcp_config: Optional[DHCPConfig] = Field(
        default=None,
        description=
        "The shared DHCP configuration for the IP space that controls how leases are issued."
    )
    dhcp_options: Optional[List[OptionItem]] = Field(
        default=None,
        description=
        "The list of IPv4 DHCP options for IP space. May be either a specific option or a group of options."
    )
    dhcp_options_v6: Optional[List[OptionItem]] = Field(
        default=None,
        description=
        "The list of IPv6 DHCP options for IP space. May be either a specific option or a group of options."
    )
    header_option_filename: Optional[StrictStr] = Field(
        default=None,
        description="The configuration for header option filename field.")
    header_option_server_address: Optional[StrictStr] = Field(
        default=None,
        description="The configuration for header option server address field."
    )
    header_option_server_name: Optional[StrictStr] = Field(
        default=None,
        description="The configuration for header option server name field.")
    hostname_rewrite_char: Optional[StrictStr] = Field(
        default='-',
        description=
        "The character to replace non-matching characters with, when hostname rewrite is enabled.  Any single ASCII character or no character if the invalid characters should be removed without replacement.  Defaults to \"-\"."
    )
    hostname_rewrite_enabled: Optional[StrictBool] = Field(
        default=False,
        description=
        "Indicates if client supplied hostnames will be rewritten prior to DDNS update by replacing every character that does not match _hostname_rewrite_regex_ by _hostname_rewrite_char_.  Defaults to _false_."
    )
    hostname_rewrite_regex: Optional[StrictStr] = Field(
        default='[^a-zA-Z0-9_.]',
        description=
        "The regex bracket expression to match valid characters.  Must begin with \"[\" and end with \"]\" and be a compilable POSIX regex.  Defaults to \"[^a-zA-Z0-9_.]\"."
    )
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    inheritance_sources: Optional[IPSpaceInheritance] = Field(
        default=None, description="The inheritance configuration.")
    name: StrictStr = Field(
        description=
        "The name of the IP space. Must contain 1 to 256 characters. Can include UTF-8."
    )
    tags: Optional[Dict[str, Any]] = Field(
        default=None, description="The tags for the IP space in JSON format.")
    threshold: Optional[UtilizationThreshold] = Field(
        default=None,
        description="The utilization threshold settings for the IP space.")
    updated_at: Optional[datetime] = Field(
        default=None,
        description=
        "Time when the object has been updated. Equals to _created_at_ if not updated after creation."
    )
    utilization: Optional[Utilization] = Field(
        default=None,
        description="The utilization of IPV4 addresses in the IP space.")
    utilization_v6: Optional[UtilizationV6] = Field(
        default=None,
        description="The utilization of IPV6 addresses in the IP space.")
    vendor_specific_option_option_space: Optional[StrictStr] = Field(
        default=None, description="The resource identifier.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "asm_config", "asm_scope_flag", "comment", "compartment_id",
        "created_at", "ddns_client_update", "ddns_conflict_resolution_mode",
        "ddns_domain", "ddns_generate_name", "ddns_generated_prefix",
        "ddns_send_updates", "ddns_ttl_percent", "ddns_update_on_renew",
        "ddns_use_conflict_resolution", "default_realms", "dhcp_config",
        "dhcp_options", "dhcp_options_v6", "header_option_filename",
        "header_option_server_address", "header_option_server_name",
        "hostname_rewrite_char", "hostname_rewrite_enabled",
        "hostname_rewrite_regex", "id", "inheritance_sources", "name", "tags",
        "threshold", "updated_at", "utilization", "utilization_v6",
        "vendor_specific_option_option_space"
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
        """Create an instance of IPSpace from a JSON string"""
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
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "asm_scope_flag",
            "created_at",
            "id",
            "threshold",
            "updated_at",
            "utilization",
            "utilization_v6",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of asm_config
        if self.asm_config:
            _dict['asm_config'] = self.asm_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dhcp_config
        if self.dhcp_config:
            _dict['dhcp_config'] = self.dhcp_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in dhcp_options (list)
        _items = []
        if self.dhcp_options:
            for _item in self.dhcp_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dhcp_options'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dhcp_options_v6 (list)
        _items = []
        if self.dhcp_options_v6:
            for _item in self.dhcp_options_v6:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dhcp_options_v6'] = _items
        # override the default output from pydantic by calling `to_dict()` of inheritance_sources
        if self.inheritance_sources:
            _dict['inheritance_sources'] = self.inheritance_sources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of threshold
        if self.threshold:
            _dict['threshold'] = self.threshold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utilization
        if self.utilization:
            _dict['utilization'] = self.utilization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utilization_v6
        if self.utilization_v6:
            _dict['utilization_v6'] = self.utilization_v6.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IPSpace from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asm_config":
            ASMConfig.from_dict(obj["asm_config"])
            if obj.get("asm_config") is not None else None,
            "asm_scope_flag":
            obj.get("asm_scope_flag"),
            "comment":
            obj.get("comment"),
            "compartment_id":
            obj.get("compartment_id"),
            "created_at":
            obj.get("created_at"),
            "ddns_client_update":
            obj.get("ddns_client_update")
            if obj.get("ddns_client_update") is not None else 'client',
            "ddns_conflict_resolution_mode":
            obj.get("ddns_conflict_resolution_mode")
            if obj.get("ddns_conflict_resolution_mode") is not None else
            'check_with_dhcid',
            "ddns_domain":
            obj.get("ddns_domain"),
            "ddns_generate_name":
            obj.get("ddns_generate_name")
            if obj.get("ddns_generate_name") is not None else False,
            "ddns_generated_prefix":
            obj.get("ddns_generated_prefix")
            if obj.get("ddns_generated_prefix") is not None else 'myhost',
            "ddns_send_updates":
            obj.get("ddns_send_updates")
            if obj.get("ddns_send_updates") is not None else True,
            "ddns_ttl_percent":
            obj.get("ddns_ttl_percent"),
            "ddns_update_on_renew":
            obj.get("ddns_update_on_renew")
            if obj.get("ddns_update_on_renew") is not None else False,
            "ddns_use_conflict_resolution":
            obj.get("ddns_use_conflict_resolution")
            if obj.get("ddns_use_conflict_resolution") is not None else True,
            "default_realms":
            obj.get("default_realms"),
            "dhcp_config":
            DHCPConfig.from_dict(obj["dhcp_config"])
            if obj.get("dhcp_config") is not None else None,
            "dhcp_options":
            [OptionItem.from_dict(_item) for _item in obj["dhcp_options"]]
            if obj.get("dhcp_options") is not None else None,
            "dhcp_options_v6":
            [OptionItem.from_dict(_item) for _item in obj["dhcp_options_v6"]]
            if obj.get("dhcp_options_v6") is not None else None,
            "header_option_filename":
            obj.get("header_option_filename"),
            "header_option_server_address":
            obj.get("header_option_server_address"),
            "header_option_server_name":
            obj.get("header_option_server_name"),
            "hostname_rewrite_char":
            obj.get("hostname_rewrite_char")
            if obj.get("hostname_rewrite_char") is not None else '-',
            "hostname_rewrite_enabled":
            obj.get("hostname_rewrite_enabled")
            if obj.get("hostname_rewrite_enabled") is not None else False,
            "hostname_rewrite_regex":
            obj.get("hostname_rewrite_regex")
            if obj.get("hostname_rewrite_regex") is not None else
            '[^a-zA-Z0-9_.]',
            "id":
            obj.get("id"),
            "inheritance_sources":
            IPSpaceInheritance.from_dict(obj["inheritance_sources"])
            if obj.get("inheritance_sources") is not None else None,
            "name":
            obj.get("name"),
            "tags":
            obj.get("tags"),
            "threshold":
            UtilizationThreshold.from_dict(obj["threshold"])
            if obj.get("threshold") is not None else None,
            "updated_at":
            obj.get("updated_at"),
            "utilization":
            Utilization.from_dict(obj["utilization"])
            if obj.get("utilization") is not None else None,
            "utilization_v6":
            UtilizationV6.from_dict(obj["utilization_v6"])
            if obj.get("utilization_v6") is not None else None,
            "vendor_specific_option_option_space":
            obj.get("vendor_specific_option_option_space")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

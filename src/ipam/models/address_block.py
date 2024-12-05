# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

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
from typing_extensions import Annotated
from ipam.models.asm_config import ASMConfig
from ipam.models.dhcp_config import DHCPConfig
from ipam.models.dhcp_inheritance import DHCPInheritance
from ipam.models.dhcp_utilization import DHCPUtilization
from ipam.models.option_item import OptionItem
from ipam.models.utilization import Utilization
from ipam.models.utilization_threshold import UtilizationThreshold
from ipam.models.utilization_v6 import UtilizationV6
from typing import Optional, Set
from typing_extensions import Self


class AddressBlock(BaseModel):
    """
    An __AddressBlock__ object (_ipam/address_block_) is a set of contiguous IP addresses in the same IP space with no gap, expressed as a CIDR block. Address blocks are hierarchical and may be parented to other address blocks as long as the parent block fully contains the child and no sibling overlaps. Top level address blocks are parented to an IP space.
    """ # noqa: E501
    address: Optional[StrictStr] = Field(
        default=None,
        description=
        "The address field in form “a.b.c.d/n” where the “/n” may be omitted. In this case, the CIDR value must be defined in the _cidr_ field. When reading, the _address_ field is always in the form “a.b.c.d”."
    )
    asm_config: Optional[ASMConfig] = Field(
        default=None,
        description=
        "The Automated Scope Management configuration for the address block.")
    asm_scope_flag: Optional[StrictInt] = Field(
        default=None,
        description=
        "Incremented by 1 if the IP address usage limits for automated scope management are exceeded for any subnets in the address block."
    )
    cidr: Optional[Annotated[int, Field(le=128, strict=True, ge=1)]] = Field(
        default=None,
        description=
        "The CIDR of the address block. This is required, if _address_ does not specify it in its input."
    )
    comment: Optional[StrictStr] = Field(
        default=None,
        description=
        "The description for the address block. May contain 0 to 1024 characters. Can include UTF-8."
    )
    compartment_id: Optional[StrictStr] = Field(
        default=None,
        description=
        "The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty."
    )
    created_at: Optional[datetime] = Field(
        default=None, description="Time when the object has been created.")
    ddns_client_update: Optional[StrictStr] = Field(
        default=None,
        description=
        "Controls who does the DDNS updates.  Valid values are: * _client_: DHCP server updates DNS if requested by client. * _server_: DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates. * _ignore_: DHCP server always updates DNS, even if the client says not to. * _over_client_update_: Same as _server_. DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates. * _over_no_update_: DHCP server updates DNS even if the client requests that no updates be done. If the client requests to do the update, DHCP server allows it.  Defaults to _client_."
    )
    ddns_conflict_resolution_mode: Optional[StrictStr] = Field(
        default=None,
        description=
        "The mode used for resolving conflicts while performing DDNS updates.  Valid values are: * _check_with_dhcid_: It includes adding a DHCID record and checking that record via conflict detection as per RFC 4703. * _no_check_with_dhcid_: This will ignore conflict detection but add a DHCID record when creating/updating an entry. * _check_exists_with_dhcid_: This will check if there is an existing DHCID record but does not verify the value of the record matches the update. This will also update the DHCID record for the entry. * _no_check_without_dhcid_: This ignores conflict detection and will not add a DHCID record when creating/updating a DDNS entry.  Defaults to _check_with_dhcid_."
    )
    ddns_domain: Optional[StrictStr] = Field(
        default=None,
        description=
        "The domain suffix for DDNS updates. FQDN, may be empty.  Defaults to empty."
    )
    ddns_generate_name: Optional[StrictBool] = Field(
        default=None,
        description=
        "Indicates if DDNS needs to generate a hostname when not supplied by the client.  Defaults to _false_."
    )
    ddns_generated_prefix: Optional[StrictStr] = Field(
        default=None,
        description=
        "The prefix used in the generation of an FQDN.  When generating a name, DHCP server will construct the name in the format: [ddns-generated-prefix]-[address-text].[ddns-qualifying-suffix]. where address-text is simply the lease IP address converted to a hyphenated string.  Defaults to \"myhost\"."
    )
    ddns_send_updates: Optional[StrictBool] = Field(
        default=None,
        description=
        "Determines if DDNS updates are enabled at the address block level. Defaults to _true_."
    )
    ddns_ttl_percent: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description=
        "DDNS TTL value - to be calculated as a simple percentage of the lease's lifetime, using the parameter's value as the percentage. It is specified as a percentage (e.g. 25, 75). Defaults to unspecified."
    )
    ddns_update_on_renew: Optional[StrictBool] = Field(
        default=None,
        description=
        "Instructs the DHCP server to always update the DNS information when a lease is renewed even if its DNS information has not changed.  Defaults to _false_."
    )
    ddns_use_conflict_resolution: Optional[StrictBool] = Field(
        default=None,
        description=
        "When true, DHCP server will apply conflict resolution, as described in RFC 4703, when attempting to fulfill the update request.  When false, DHCP server will simply attempt to update the DNS entries per the request, regardless of whether or not they conflict with existing entries owned by other DHCP4 clients.  Defaults to _true_."
    )
    delegation: Optional[StrictStr] = Field(
        default=None,
        description=
        "The ID of the delegation associated with the address block.")
    dhcp_config: Optional[DHCPConfig] = Field(
        default=None,
        description=
        "The shared DHCP configuration that controls how leases are issued for the address block."
    )
    dhcp_options: Optional[List[OptionItem]] = Field(
        default=None,
        description=
        "The list of DHCP options for the address block. May be either a specific option or a group of options."
    )
    dhcp_utilization: Optional[DHCPUtilization] = Field(
        default=None,
        description=
        "The utilization of IP addresses within the DHCP ranges of the address block."
    )
    discovery_attrs: Optional[Dict[str, Any]] = Field(
        default=None,
        description=
        "The discovery attributes for this address block in JSON format.")
    discovery_metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description=
        "The discovery metadata for this address block in JSON format.")
    external_keys: Optional[Dict[str, Any]] = Field(
        default=None,
        description=
        "The external keys (source key) for this address block in JSON format."
    )
    federated_realms: Optional[List[StrictStr]] = Field(
        default=None, description="Reserved for future use.")
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
        default=None,
        description=
        "The character to replace non-matching characters with, when hostname rewrite is enabled.  Any single ASCII character or no character if the invalid characters should be removed without replacement.  Defaults to \"-\"."
    )
    hostname_rewrite_enabled: Optional[StrictBool] = Field(
        default=None,
        description=
        "Indicates if client supplied hostnames will be rewritten prior to DDNS update by replacing every character that does not match _hostname_rewrite_regex_ by _hostname_rewrite_char_.  Defaults to _false_."
    )
    hostname_rewrite_regex: Optional[StrictStr] = Field(
        default=None,
        description=
        "The regex bracket expression to match valid characters.  Must begin with \"[\" and end with \"]\" and be a compilable POSIX regex.  Defaults to \"[^a-zA-Z0-9_.]\"."
    )
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    inheritance_parent: Optional[StrictStr] = Field(
        default=None, description="The resource identifier.")
    inheritance_sources: Optional[DHCPInheritance] = Field(
        default=None,
        description="The DHCP inheritance configuration for the address block."
    )
    name: Optional[StrictStr] = Field(
        default=None,
        description=
        "The name of the address block. May contain 1 to 256 characters. Can include UTF-8."
    )
    parent: Optional[StrictStr] = Field(default=None,
                                        description="The resource identifier.")
    protocol: Optional[StrictStr] = Field(
        default=None,
        description="The type of protocol of address block (_ip4_ or _ip6_).")
    space: Optional[StrictStr] = Field(default=None,
                                       description="The resource identifier.")
    tags: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The tags for the address block in JSON format.")
    threshold: Optional[UtilizationThreshold] = Field(
        default=None,
        description=
        "The IP address utilization thresholds for the address block.")
    updated_at: Optional[datetime] = Field(
        default=None,
        description=
        "Time when the object has been updated. Equals to _created_at_ if not updated after creation."
    )
    usage: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "The usage is a combination of indicators, each tracking a specific associated use. Listed below are usage indicators with their meaning:  usage indicator        | description  ---------------------- | --------------------------------  _IPAM_                 |  AddressBlock is managed in BloxOne DDI.  _DISCOVERED_           |  AddressBlock is discovered by some network discovery probe like Network Insight or NetMRI in NIOS."
    )
    utilization: Optional[Utilization] = Field(
        default=None,
        description=
        "The IPV4 address utilization statistics for the address block.")
    utilization_v6: Optional[UtilizationV6] = Field(
        default=None,
        description="The utilization of IPV6 addresses in the Address block.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "address", "asm_config", "asm_scope_flag", "cidr", "comment",
        "compartment_id", "created_at", "ddns_client_update",
        "ddns_conflict_resolution_mode", "ddns_domain", "ddns_generate_name",
        "ddns_generated_prefix", "ddns_send_updates", "ddns_ttl_percent",
        "ddns_update_on_renew", "ddns_use_conflict_resolution", "delegation",
        "dhcp_config", "dhcp_options", "dhcp_utilization", "discovery_attrs",
        "discovery_metadata", "external_keys", "federated_realms",
        "header_option_filename", "header_option_server_address",
        "header_option_server_name", "hostname_rewrite_char",
        "hostname_rewrite_enabled", "hostname_rewrite_regex", "id",
        "inheritance_parent", "inheritance_sources", "name", "parent",
        "protocol", "space", "tags", "threshold", "updated_at", "usage",
        "utilization", "utilization_v6"
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
        """Create an instance of AddressBlock from a JSON string"""
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
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "asm_scope_flag",
            "created_at",
            "delegation",
            "dhcp_utilization",
            "discovery_attrs",
            "discovery_metadata",
            "id",
            "protocol",
            "updated_at",
            "usage",
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
        # override the default output from pydantic by calling `to_dict()` of dhcp_utilization
        if self.dhcp_utilization:
            _dict['dhcp_utilization'] = self.dhcp_utilization.to_dict()
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
        """Create an instance of AddressBlock from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address":
            obj.get("address"),
            "asm_config":
            ASMConfig.from_dict(obj["asm_config"])
            if obj.get("asm_config") is not None else None,
            "asm_scope_flag":
            obj.get("asm_scope_flag"),
            "cidr":
            obj.get("cidr"),
            "comment":
            obj.get("comment"),
            "compartment_id":
            obj.get("compartment_id"),
            "created_at":
            obj.get("created_at"),
            "ddns_client_update":
            obj.get("ddns_client_update"),
            "ddns_conflict_resolution_mode":
            obj.get("ddns_conflict_resolution_mode"),
            "ddns_domain":
            obj.get("ddns_domain"),
            "ddns_generate_name":
            obj.get("ddns_generate_name"),
            "ddns_generated_prefix":
            obj.get("ddns_generated_prefix"),
            "ddns_send_updates":
            obj.get("ddns_send_updates"),
            "ddns_ttl_percent":
            obj.get("ddns_ttl_percent"),
            "ddns_update_on_renew":
            obj.get("ddns_update_on_renew"),
            "ddns_use_conflict_resolution":
            obj.get("ddns_use_conflict_resolution"),
            "delegation":
            obj.get("delegation"),
            "dhcp_config":
            DHCPConfig.from_dict(obj["dhcp_config"])
            if obj.get("dhcp_config") is not None else None,
            "dhcp_options":
            [OptionItem.from_dict(_item) for _item in obj["dhcp_options"]]
            if obj.get("dhcp_options") is not None else None,
            "dhcp_utilization":
            DHCPUtilization.from_dict(obj["dhcp_utilization"])
            if obj.get("dhcp_utilization") is not None else None,
            "discovery_attrs":
            obj.get("discovery_attrs"),
            "discovery_metadata":
            obj.get("discovery_metadata"),
            "external_keys":
            obj.get("external_keys"),
            "federated_realms":
            obj.get("federated_realms"),
            "header_option_filename":
            obj.get("header_option_filename"),
            "header_option_server_address":
            obj.get("header_option_server_address"),
            "header_option_server_name":
            obj.get("header_option_server_name"),
            "hostname_rewrite_char":
            obj.get("hostname_rewrite_char"),
            "hostname_rewrite_enabled":
            obj.get("hostname_rewrite_enabled"),
            "hostname_rewrite_regex":
            obj.get("hostname_rewrite_regex"),
            "id":
            obj.get("id"),
            "inheritance_parent":
            obj.get("inheritance_parent"),
            "inheritance_sources":
            DHCPInheritance.from_dict(obj["inheritance_sources"])
            if obj.get("inheritance_sources") is not None else None,
            "name":
            obj.get("name"),
            "parent":
            obj.get("parent"),
            "protocol":
            obj.get("protocol"),
            "space":
            obj.get("space"),
            "tags":
            obj.get("tags"),
            "threshold":
            UtilizationThreshold.from_dict(obj["threshold"])
            if obj.get("threshold") is not None else None,
            "updated_at":
            obj.get("updated_at"),
            "usage":
            obj.get("usage"),
            "utilization":
            Utilization.from_dict(obj["utilization"])
            if obj.get("utilization") is not None else None,
            "utilization_v6":
            UtilizationV6.from_dict(obj["utilization_v6"])
            if obj.get("utilization_v6") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

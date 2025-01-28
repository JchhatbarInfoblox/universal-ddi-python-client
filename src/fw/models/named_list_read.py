# coding: utf-8

"""
    Infoblox FW API

    Infoblox Threat Defense Cloud is an extension of the Infoblox Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to Infoblox Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. Infoblox Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class NamedListRead(BaseModel):
    """
    The Named List object.  The Named List object represents several types of lists allowed for Infoblox Cloud such as predefined threat intelligence feeds that your subscription offers (Threat Insight, Fast Flux, DGA, DNSM). In addition to the predefined threat intelligence feeds that your subscription offers, you can create custom lists (containing domains and IP addresses) to define whitelists and blacklists for additional protection. You can use a custom list to complement existing feeds or override the Block, Allow, Log, or Redirect action that is currently defined for an existing feed. Note that lists representing predefined TI feeds cannot be created, updated and deleted.
    """ # noqa: E501
    confidence_level: Optional[StrictStr] = Field(
        default=None,
        description=
        "The confidence level for a custom list. The possible values are [\"LOW\", \"MEDIUM\", \"HIGH\"]"
    )
    created_time: Optional[datetime] = Field(
        default=None,
        description="The time when this Named List object was created.")
    description: Optional[StrictStr] = Field(
        default=None, description="The brief description for the named list.")
    id: Optional[StrictInt] = Field(
        default=None, description="The Named List object identifier.")
    item_count: Optional[StrictInt] = Field(
        default=None, description="The number of items in this named list.")
    name: Optional[StrictStr] = Field(
        default=None, description="The name of the named list.")
    policies: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "The list of the security policy names with which the named list is associated."
    )
    tags: Optional[Dict[str, Any]] = Field(
        default=None, description="Tags associated with this Named List")
    threat_level: Optional[StrictStr] = Field(
        default=None,
        description=
        "The threat level for a custom list. The possible values are [\"INFO\", \"LOW\", \"MEDIUM\", \"HIGH\"]"
    )
    type: Optional[StrictStr] = Field(
        default=None,
        description=
        "The type of the named list, that can be \"custom_list\", \"threat_insight\", \"fast_flux\", \"dga\", \"dnsm\", \"threat_insight_nde\", \"default_allow\", \"default_block\"."
    )
    updated_time: Optional[datetime] = Field(
        default=None,
        description="The time when this Named List object was last updated.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "confidence_level", "created_time", "description", "id", "item_count",
        "name", "policies", "tags", "threat_level", "type", "updated_time"
    ]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([
                'custom_list', 'threat_insight', 'fast_flux', 'dga', 'dnsm',
                'threat_insight_nde', 'default_allow', 'default_block'
        ]):
            raise ValueError(
                "must be one of enum values ('custom_list', 'threat_insight', 'fast_flux', 'dga', 'dnsm', 'threat_insight_nde', 'default_allow', 'default_block')"
            )
        return value

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
        """Create an instance of NamedListRead from a JSON string"""
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
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "confidence_level",
            "created_time",
            "description",
            "id",
            "item_count",
            "name",
            "policies",
            "threat_level",
            "type",
            "updated_time",
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
        """Create an instance of NamedListRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "confidence_level":
            obj.get("confidence_level"),
            "created_time":
            obj.get("created_time"),
            "description":
            obj.get("description"),
            "id":
            obj.get("id"),
            "item_count":
            obj.get("item_count"),
            "name":
            obj.get("name"),
            "policies":
            obj.get("policies"),
            "tags":
            obj.get("tags"),
            "threat_level":
            obj.get("threat_level"),
            "type":
            obj.get("type"),
            "updated_time":
            obj.get("updated_time")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fw.models.access_code_rule import AccessCodeRule
from typing import Optional, Set
from typing_extensions import Self


class AccessCode(BaseModel):
    """
    AccessCode
    """

  # noqa: E501
    access_key: Optional[StrictStr] = Field(
        default=None, description="Auto generated unique Bypass Code value")
    activation: Optional[datetime] = Field(
        default=None,
        description="The time when the Bypass Code object was activated.")
    created_time: Optional[datetime] = Field(
        default=None,
        description="The time when the Bypass Code object was created.")
    description: Optional[StrictStr] = None
    expiration: Optional[datetime] = Field(
        default=None,
        description="The time when the Bypass Code object was expired.")
    name: Optional[StrictStr] = Field(default=None,
                                      description="The name of Bypass Code")
    policy_ids: Optional[List[StrictInt]] = Field(
        default=None,
        description="The list of SecurityPolicy object identifiers.")
    rules: Optional[List[AccessCodeRule]] = Field(
        default=None, description="The list of selected security rules")
    updated_time: Optional[datetime] = Field(
        default=None,
        description="The time when the Bypass Code object was last updated.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "access_key", "activation", "created_time", "description",
        "expiration", "name", "policy_ids", "rules", "updated_time"
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
        """Create an instance of AccessCode from a JSON string"""
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
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "updated_time",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_key":
            obj.get("access_key"),
            "activation":
            obj.get("activation"),
            "created_time":
            obj.get("created_time"),
            "description":
            obj.get("description"),
            "expiration":
            obj.get("expiration"),
            "name":
            obj.get("name"),
            "policy_ids":
            obj.get("policy_ids"),
            "rules":
            [AccessCodeRule.from_dict(_item) for _item in obj["rules"]]
            if obj.get("rules") is not None else None,
            "updated_time":
            obj.get("updated_time")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

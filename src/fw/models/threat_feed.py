# coding: utf-8

"""
    BloxOne FW API

    BloxOne Threat Defense Cloud is an extension of the BloxOne Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to BloxOne Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. BloxOne Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fw.models.threat_feed_source import ThreatFeedSource
from typing import Optional, Set
from typing_extensions import Self


class ThreatFeed(BaseModel):
    """
    The Threat Feed object.  BloxOne Cloud provides predefined threat intelligence feeds based on your subscription. The Plus subscription offers a few more feeds than the Standard subscription. The Advanced subscription offers a few more feeds than the Plus subscription. A threat feed subscription for RPZ updates offers protection against malicious hostnames.
    """ # noqa: E501
    confidence_level: Optional[StrictStr] = Field(
        default=None, description="The Confidence Level of the Feed.")
    description: Optional[StrictStr] = Field(
        default=None, description="The brief description for the thread feed.")
    key: Optional[StrictStr] = Field(
        default=None, description="The TSIG key of the threat feed.")
    name: Optional[StrictStr] = Field(
        default=None, description="The name of the thread feed.")
    source: Optional[ThreatFeedSource] = Field(
        default=None, description="The source of the threat feed.")
    threat_level: Optional[StrictStr] = Field(
        default=None, description="The Threat Level of the Feed.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "confidence_level", "description", "key", "name", "source",
        "threat_level"
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
        """Create an instance of ThreatFeed from a JSON string"""
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
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "confidence_level",
            "description",
            "key",
            "name",
            "source",
            "threat_level",
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
        """Create an instance of ThreatFeed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "confidence_level":
            obj.get("confidence_level"),
            "description":
            obj.get("description"),
            "key":
            obj.get("key"),
            "name":
            obj.get("name"),
            "source":
            obj.get("source"),
            "threat_level":
            obj.get("threat_level")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

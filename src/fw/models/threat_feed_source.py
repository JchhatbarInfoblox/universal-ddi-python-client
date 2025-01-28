# coding: utf-8

"""
    Infoblox FW API

    Infoblox Threat Defense Cloud is an extension of the Infoblox Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to Infoblox Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. Infoblox Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ThreatFeedSource(str, Enum):
    """
    ThreatFeedSource
    """
    """
    allowed enum values
    """
    INFOBLOX = 'Infoblox'
    CUSTOM = 'Custom'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ThreatFeedSource from a JSON string"""
        return cls(json.loads(json_str))

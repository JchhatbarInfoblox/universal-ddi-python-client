# coding: utf-8

"""
    Infoblox FW API

    Infoblox Threat Defense Cloud is an extension of the Infoblox Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to Infoblox Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. Infoblox Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from fw.api.security_policy_rules_api import SecurityPolicyRulesApi

from universal_ddi_client.api_client import ApiClient


class TestSecurityPolicyRulesApi(unittest.TestCase):
    """SecurityPolicyRulesApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = SecurityPolicyRulesApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_list_security_policy_rules(self) -> None:
        """Test case for list_security_policy_rules

        List Security Policy Rules.
        """
        pass


if __name__ == '__main__':
    unittest.main()

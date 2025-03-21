# anycast
Anycast capability enables HA (High Availability) configuration of Universal DDI applications that run on equipment located on customer's premises (on-prem hosts). Anycast supports DNS, as well as DNS-forwarding services.  Anycast-enabled application setups use multiple on-premises installations for one particular application type. Multiple application instances are configured to use the same endpoint address. Anycast capability is collocated with such application instance, monitoring the local application instance and advertising to the upstream router (a customer equipment) a per-instance, local route to the common application endpoint address, as long as the local application instance is available. Depending on the type of the upstream router, the customer may configure local route advertisement via either BGP (Boarder Gateway Protocol) or OSPF (Open Shortest Path First) routing protocols. Both protocols may be enabled as well. Multiple routes to the common application service address provide redundancy without the need to reconfigure application clients.  Should an application instance become unavailable, the local route advertisements stop, resulting in withdrawal of the route (in the upstream router) to the application instance that has gone out of service and ensuring that subsequent application requests thus get routed to the remaining available application instances.  

The `anycast` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 0.1.0
- Generator version: 7.5.0
- Build package: com.infoblox.codegen.UniversalDdiPythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3
* python-dateutil
* pydantic

## Getting Started

In your own code, to use this library to connect and interact with anycast,
you can run the following:

```python

import anycast
from anycast.rest import ApiException
from pprint import pprint

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")


# Enter a context with an instance of the API client
with anycast.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = anycast.OnPremAnycastManagerApi(api_client)
    body = anycast.AnycastConfig() # AnycastConfig | 

    try:
        # Create Anycast Configuration
        api_response = api_instance.create_anycast_config(body)
        print("The response of OnPremAnycastManagerApi->create_anycast_config:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OnPremAnycastManagerApi->create_anycast_config: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://csp.infoblox.com/api/anycast/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OnPremAnycastManagerApi* | [**create_anycast_config**](anycast/docs/OnPremAnycastManagerApi.md#create_anycast_config) | **POST** /accm/ac_configs | Create Anycast Configuration
*OnPremAnycastManagerApi* | [**create_anycast_version**](anycast/docs/OnPremAnycastManagerApi.md#create_anycast_version) | **POST** /accm/ac_version/{id} | Create Anycast Version
*OnPremAnycastManagerApi* | [**delete_anycast_config**](anycast/docs/OnPremAnycastManagerApi.md#delete_anycast_config) | **DELETE** /accm/ac_configs/{id} | Delete Anycast Configuration
*OnPremAnycastManagerApi* | [**delete_anycast_version**](anycast/docs/OnPremAnycastManagerApi.md#delete_anycast_version) | **DELETE** /accm/ac_version/{id} | Delete anycast version
*OnPremAnycastManagerApi* | [**delete_onprem_host**](anycast/docs/OnPremAnycastManagerApi.md#delete_onprem_host) | **DELETE** /accm/op_hosts/{id} | Delete On-Prem Host
*OnPremAnycastManagerApi* | [**get_anycast_config**](anycast/docs/OnPremAnycastManagerApi.md#get_anycast_config) | **GET** /accm/ac_configs/{id} | Retrieve Anycast Configuration
*OnPremAnycastManagerApi* | [**get_anycast_config_list**](anycast/docs/OnPremAnycastManagerApi.md#get_anycast_config_list) | **GET** /accm/ac_configs | Retrieve Multiple Anycast Configurations
*OnPremAnycastManagerApi* | [**get_anycast_version**](anycast/docs/OnPremAnycastManagerApi.md#get_anycast_version) | **GET** /accm/ac_version/{id} | Retrieve Anycast Version
*OnPremAnycastManagerApi* | [**get_onprem_config**](anycast/docs/OnPremAnycastManagerApi.md#get_onprem_config) | **GET** /accm/oph_configs/{ophid}/{version} | Retrieve Generated, Per-Host Anycast Configuration
*OnPremAnycastManagerApi* | [**get_onprem_config2**](anycast/docs/OnPremAnycastManagerApi.md#get_onprem_config2) | **GET** /onprem_config/{ophid}/{version} | Retrieve Generated, Per-Host Anycast Configuration
*OnPremAnycastManagerApi* | [**get_onprem_host**](anycast/docs/OnPremAnycastManagerApi.md#get_onprem_host) | **GET** /accm/op_hosts/{id} | Retrieve On-Prem Host
*OnPremAnycastManagerApi* | [**get_status**](anycast/docs/OnPremAnycastManagerApi.md#get_status) | **GET** /accm/oph_config_statuses/{ophid}/latest | Retrieve Configuration Status
*OnPremAnycastManagerApi* | [**get_status2**](anycast/docs/OnPremAnycastManagerApi.md#get_status2) | **GET** /onprem_config_statuses/{ophid}/latest | Retrieve Configuration Status
*OnPremAnycastManagerApi* | [**list_anycast_configs_with_runtime_status**](anycast/docs/OnPremAnycastManagerApi.md#list_anycast_configs_with_runtime_status) | **GET** /accm/ac_runtime_statuses | Read list of Anycast Configurations
*OnPremAnycastManagerApi* | [**read_anycast_config_with_runtime_status**](anycast/docs/OnPremAnycastManagerApi.md#read_anycast_config_with_runtime_status) | **GET** /accm/ac_runtime_statuses/{id} | Read Anycast Configuration
*OnPremAnycastManagerApi* | [**update_anycast_config**](anycast/docs/OnPremAnycastManagerApi.md#update_anycast_config) | **PUT** /accm/ac_configs/{id} | Create or Update Anycast Configuration
*OnPremAnycastManagerApi* | [**update_onprem_host**](anycast/docs/OnPremAnycastManagerApi.md#update_onprem_host) | **PUT** /accm/op_hosts/{id} | Create or Update On-Prem Host


## Documentation For Models

 - [AnycastConfig](anycast/docs/AnycastConfig.md)
 - [AnycastConfigRef](anycast/docs/AnycastConfigRef.md)
 - [AnycastConfigResponse](anycast/docs/AnycastConfigResponse.md)
 - [AnycastVersion](anycast/docs/AnycastVersion.md)
 - [BgpConfig](anycast/docs/BgpConfig.md)
 - [BgpNeighbor](anycast/docs/BgpNeighbor.md)
 - [GetAnycastConfigListResponse](anycast/docs/GetAnycastConfigListResponse.md)
 - [OnpremHost](anycast/docs/OnpremHost.md)
 - [OnpremHostRef](anycast/docs/OnpremHostRef.md)
 - [OnpremHostResponse](anycast/docs/OnpremHostResponse.md)
 - [OspfConfig](anycast/docs/OspfConfig.md)
 - [Ospfv3Config](anycast/docs/Ospfv3Config.md)
 - [ProtobufFieldMask](anycast/docs/ProtobufFieldMask.md)
 - [ServiceConfig](anycast/docs/ServiceConfig.md)
 - [ServiceConfigObject](anycast/docs/ServiceConfigObject.md)
 - [ServiceStatusCode](anycast/docs/ServiceStatusCode.md)
 - [ServiceStatusUpdateRequest](anycast/docs/ServiceStatusUpdateRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author





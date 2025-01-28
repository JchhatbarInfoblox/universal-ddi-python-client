# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a Universal DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured Universal DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from dns_config.models.convert_domain_name_response import ConvertDomainNameResponse
from dns_config import models

from universal_ddi_client.api_client import ApiClient, RequestSerialized
from universal_ddi_client.api_response import ApiResponse
from universal_ddi_client.rest import RESTResponseType


class ConvertDomainNameApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def convert(
        self,
        domain_name: Annotated[
            StrictStr,
            Field(
                description=
                "Input domain name in either of IDN or punycode representations."
            )],
        _request_timeout: Union[None, Annotated[StrictFloat,
                                                Field(gt=0)],
                                Tuple[Annotated[StrictFloat,
                                                Field(gt=0)],
                                      Annotated[StrictFloat,
                                                Field(gt=0)]]] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ConvertDomainNameResponse:
        """Convert the object.

        Use this method to convert between Internationalized Domain Name (IDN) and ASCII domain name (Punycode).

        :param domain_name: Input domain name in either of IDN or punycode representations. (required)
        :type domain_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._convert_serialize(domain_name=domain_name,
                                         _request_auth=_request_auth,
                                         _content_type=_content_type,
                                         _headers=_headers,
                                         _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ConvertDomainNameResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            models=models,
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def convert_with_http_info(
        self,
        domain_name: Annotated[
            StrictStr,
            Field(
                description=
                "Input domain name in either of IDN or punycode representations."
            )],
        _request_timeout: Union[None, Annotated[StrictFloat,
                                                Field(gt=0)],
                                Tuple[Annotated[StrictFloat,
                                                Field(gt=0)],
                                      Annotated[StrictFloat,
                                                Field(gt=0)]]] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ConvertDomainNameResponse]:
        """Convert the object.

        Use this method to convert between Internationalized Domain Name (IDN) and ASCII domain name (Punycode).

        :param domain_name: Input domain name in either of IDN or punycode representations. (required)
        :type domain_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._convert_serialize(domain_name=domain_name,
                                         _request_auth=_request_auth,
                                         _content_type=_content_type,
                                         _headers=_headers,
                                         _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ConvertDomainNameResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            models=models,
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def convert_without_preload_content(
        self,
        domain_name: Annotated[
            StrictStr,
            Field(
                description=
                "Input domain name in either of IDN or punycode representations."
            )],
        _request_timeout: Union[None, Annotated[StrictFloat,
                                                Field(gt=0)],
                                Tuple[Annotated[StrictFloat,
                                                Field(gt=0)],
                                      Annotated[StrictFloat,
                                                Field(gt=0)]]] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Convert the object.

        Use this method to convert between Internationalized Domain Name (IDN) and ASCII domain name (Punycode).

        :param domain_name: Input domain name in either of IDN or punycode representations. (required)
        :type domain_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._convert_serialize(domain_name=domain_name,
                                         _request_auth=_request_auth,
                                         _content_type=_content_type,
                                         _headers=_headers,
                                         _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ConvertDomainNameResponse",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        return response_data.response

    def _convert_serialize(
        self,
        domain_name,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if domain_name is not None:
            _path_params['domain_name'] = self.api_client.path_param_value(
                'domain_name', domain_name)
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # authentication setting
        _auth_settings: List[str] = ['ApiKeyAuth']

        return self.api_client.param_serialize(
            method='GET',
            base_path='/api/ddi/v1',
            resource_path='/dns/convert_domain_name/{domain_name}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth)

# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._pricings_operations import (
    build_delete_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PricingsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2024_01_01.aio.SecurityCenter`'s
        :attr:`pricings` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace_async
    async def get(self, scope_id: str, pricing_name: str, **kwargs: Any) -> _models.Pricing:
        """Get the Defender plans pricing configurations of the selected scope (valid scopes are resource
        id or a subscription id). At the resource level, supported resource types are 'VirtualMachines,
        VMSS and ARC Machines'.

        :param scope_id: The scope id of the pricing. Valid scopes are: subscription (format:
         'subscriptions/{subscriptionId}'), or a specific resource (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName})
         - Supported resources are (VirtualMachines). Required.
        :type scope_id: str
        :param pricing_name: name of the pricing configuration. Required.
        :type pricing_name: str
        :return: Pricing or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2024_01_01.models.Pricing
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2024-01-01"))
        cls: ClsType[_models.Pricing] = kwargs.pop("cls", None)

        _request = build_get_request(
            scope_id=scope_id,
            pricing_name=pricing_name,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Pricing", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        scope_id: str,
        pricing_name: str,
        pricing: _models.Pricing,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Pricing:
        """Updates a provided Microsoft Defender for Cloud pricing configuration in the scope. Valid
        scopes are: subscription id or a specific resource id (Supported resources are:
        'VirtualMachines, VMSS and ARC Machines' and only for plan='VirtualMachines' and subPlan='P1').

        :param scope_id: The scope id of the pricing. Valid scopes are: subscription (format:
         'subscriptions/{subscriptionId}'), or a specific resource (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName})
         - Supported resources are (VirtualMachines). Required.
        :type scope_id: str
        :param pricing_name: name of the pricing configuration. Required.
        :type pricing_name: str
        :param pricing: Pricing object. Required.
        :type pricing: ~azure.mgmt.security.v2024_01_01.models.Pricing
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Pricing or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2024_01_01.models.Pricing
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        scope_id: str,
        pricing_name: str,
        pricing: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Pricing:
        """Updates a provided Microsoft Defender for Cloud pricing configuration in the scope. Valid
        scopes are: subscription id or a specific resource id (Supported resources are:
        'VirtualMachines, VMSS and ARC Machines' and only for plan='VirtualMachines' and subPlan='P1').

        :param scope_id: The scope id of the pricing. Valid scopes are: subscription (format:
         'subscriptions/{subscriptionId}'), or a specific resource (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName})
         - Supported resources are (VirtualMachines). Required.
        :type scope_id: str
        :param pricing_name: name of the pricing configuration. Required.
        :type pricing_name: str
        :param pricing: Pricing object. Required.
        :type pricing: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Pricing or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2024_01_01.models.Pricing
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self, scope_id: str, pricing_name: str, pricing: Union[_models.Pricing, IO[bytes]], **kwargs: Any
    ) -> _models.Pricing:
        """Updates a provided Microsoft Defender for Cloud pricing configuration in the scope. Valid
        scopes are: subscription id or a specific resource id (Supported resources are:
        'VirtualMachines, VMSS and ARC Machines' and only for plan='VirtualMachines' and subPlan='P1').

        :param scope_id: The scope id of the pricing. Valid scopes are: subscription (format:
         'subscriptions/{subscriptionId}'), or a specific resource (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName})
         - Supported resources are (VirtualMachines). Required.
        :type scope_id: str
        :param pricing_name: name of the pricing configuration. Required.
        :type pricing_name: str
        :param pricing: Pricing object. Is either a Pricing type or a IO[bytes] type. Required.
        :type pricing: ~azure.mgmt.security.v2024_01_01.models.Pricing or IO[bytes]
        :return: Pricing or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2024_01_01.models.Pricing
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2024-01-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Pricing] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(pricing, (IOBase, bytes)):
            _content = pricing
        else:
            _json = self._serialize.body(pricing, "Pricing")

        _request = build_update_request(
            scope_id=scope_id,
            pricing_name=pricing_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("Pricing", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("Pricing", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, scope_id: str, pricing_name: str, **kwargs: Any
    ) -> None:
        """Deletes a provided Microsoft Defender for Cloud pricing configuration in a specific resource.
        Valid only for resource scope (Supported resources are: 'VirtualMachines, VMSS and ARC
        MachinesS').

        :param scope_id: The identifier of the resource, (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}).
         Required.
        :type scope_id: str
        :param pricing_name: name of the pricing configuration. Required.
        :type pricing_name: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2024-01-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            scope_id=scope_id,
            pricing_name=pricing_name,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def list(self, scope_id: str, filter: Optional[str] = None, **kwargs: Any) -> _models.PricingList:
        """Lists Microsoft Defender for Cloud pricing configurations of the scopeId, that match the
        optional given $filter. Valid scopes are: subscription id or a specific resource id (Supported
        resources are: 'VirtualMachines, VMSS and ARC Machines'). Valid $filter is: 'name in
        ({planName1},{planName2},...)'. If $filter is not provided, the unfiltered list will be
        returned. If '$filter=name in (planName1,planName2)' is provided, the returned list includes
        the pricings set for 'planName1' and 'planName2' only.

        :param scope_id: The scope id of the pricing. Valid scopes are: subscription (format:
         'subscriptions/{subscriptionId}'), or a specific resource (format:
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName})
         - Supported resources are (VirtualMachines). Required.
        :type scope_id: str
        :param filter: OData filter. Optional. Default value is None.
        :type filter: str
        :return: PricingList or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2024_01_01.models.PricingList
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2024-01-01"))
        cls: ClsType[_models.PricingList] = kwargs.pop("cls", None)

        _request = build_list_request(
            scope_id=scope_id,
            filter=filter,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PricingList", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

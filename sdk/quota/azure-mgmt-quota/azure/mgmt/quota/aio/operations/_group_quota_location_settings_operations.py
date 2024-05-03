# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._group_quota_location_settings_operations import (
    build_create_or_update_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class GroupQuotaLocationSettingsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.quota.aio.QuotaMgmtClient`'s
        :attr:`group_quota_location_settings` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _create_or_update_initial(
        self,
        management_group_id: str,
        group_quota_name: str,
        resource_provider_name: str,
        location: str,
        location_settings: Optional[Union[_models.GroupQuotasEnforcementResponse, IO[bytes]]] = None,
        **kwargs: Any
    ) -> Union[_models.GroupQuotasEnforcementResponse, _models.LROResponse]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Union[_models.GroupQuotasEnforcementResponse, _models.LROResponse]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(location_settings, (IOBase, bytes)):
            _content = location_settings
        else:
            if location_settings is not None:
                _json = self._serialize.body(location_settings, "GroupQuotasEnforcementResponse")
            else:
                _json = None

        _request = build_create_or_update_request(
            management_group_id=management_group_id,
            group_quota_name=group_quota_name,
            resource_provider_name=resource_provider_name,
            location=location,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("GroupQuotasEnforcementResponse", pipeline_response)

        if response.status_code == 201:
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )

            deserialized = self._deserialize("LROResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create_or_update(
        self,
        management_group_id: str,
        group_quota_name: str,
        resource_provider_name: str,
        location: str,
        location_settings: Optional[_models.GroupQuotasEnforcementResponse] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.GroupQuotasEnforcementResponse]:
        """Enables the GroupQuotas enforcement settings for the resource provider and the location
        specified.

        Enables the GroupQuotas enforcement for the resource provider and the location specified. The
        resource provider will start using the group quotas as the overall quota for the subscriptions
        included in the GroupQuota. The subscriptions cannot request quota at subscription level.
        The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the
        GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource -
        provider/location/resource.
        Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To
        disable GroupQuota Enforcement -


        #. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions
        (Check the example - GroupQuotaSubscriptions_Delete).
        #. Ten delete the GroupQuota (Check the example - GroupQuotas_Delete).

        :param management_group_id: Management Group Id. Required.
        :type management_group_id: str
        :param group_quota_name: The GroupQuota name. The name should be unique for the provided
         context tenantId/MgId. Required.
        :type group_quota_name: str
        :param resource_provider_name: The resource provider name, such as - Microsoft.Compute.
         Currently only Microsoft.Compute resource provider supports this API. Required.
        :type resource_provider_name: str
        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_settings: The GroupQuota body details for creation or update of a GroupQuota
         entity. Default value is None.
        :type location_settings: ~azure.mgmt.quota.models.GroupQuotasEnforcementResponse
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either GroupQuotasEnforcementResponse or An
         instance of AsyncLROPoller that returns either LROResponse or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.GroupQuotasEnforcementResponse] or
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.LROResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update(
        self,
        management_group_id: str,
        group_quota_name: str,
        resource_provider_name: str,
        location: str,
        location_settings: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.GroupQuotasEnforcementResponse]:
        """Enables the GroupQuotas enforcement settings for the resource provider and the location
        specified.

        Enables the GroupQuotas enforcement for the resource provider and the location specified. The
        resource provider will start using the group quotas as the overall quota for the subscriptions
        included in the GroupQuota. The subscriptions cannot request quota at subscription level.
        The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the
        GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource -
        provider/location/resource.
        Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To
        disable GroupQuota Enforcement -


        #. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions
        (Check the example - GroupQuotaSubscriptions_Delete).
        #. Ten delete the GroupQuota (Check the example - GroupQuotas_Delete).

        :param management_group_id: Management Group Id. Required.
        :type management_group_id: str
        :param group_quota_name: The GroupQuota name. The name should be unique for the provided
         context tenantId/MgId. Required.
        :type group_quota_name: str
        :param resource_provider_name: The resource provider name, such as - Microsoft.Compute.
         Currently only Microsoft.Compute resource provider supports this API. Required.
        :type resource_provider_name: str
        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_settings: The GroupQuota body details for creation or update of a GroupQuota
         entity. Default value is None.
        :type location_settings: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either GroupQuotasEnforcementResponse or An
         instance of AsyncLROPoller that returns either LROResponse or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.GroupQuotasEnforcementResponse] or
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.LROResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_update(
        self,
        management_group_id: str,
        group_quota_name: str,
        resource_provider_name: str,
        location: str,
        location_settings: Optional[Union[_models.GroupQuotasEnforcementResponse, IO[bytes]]] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.GroupQuotasEnforcementResponse]:
        """Enables the GroupQuotas enforcement settings for the resource provider and the location
        specified.

        Enables the GroupQuotas enforcement for the resource provider and the location specified. The
        resource provider will start using the group quotas as the overall quota for the subscriptions
        included in the GroupQuota. The subscriptions cannot request quota at subscription level.
        The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the
        GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource -
        provider/location/resource.
        Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To
        disable GroupQuota Enforcement -


        #. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions
        (Check the example - GroupQuotaSubscriptions_Delete).
        #. Ten delete the GroupQuota (Check the example - GroupQuotas_Delete).

        :param management_group_id: Management Group Id. Required.
        :type management_group_id: str
        :param group_quota_name: The GroupQuota name. The name should be unique for the provided
         context tenantId/MgId. Required.
        :type group_quota_name: str
        :param resource_provider_name: The resource provider name, such as - Microsoft.Compute.
         Currently only Microsoft.Compute resource provider supports this API. Required.
        :type resource_provider_name: str
        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_settings: The GroupQuota body details for creation or update of a GroupQuota
         entity. Is either a GroupQuotasEnforcementResponse type or a IO[bytes] type. Default value is
         None.
        :type location_settings: ~azure.mgmt.quota.models.GroupQuotasEnforcementResponse or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either GroupQuotasEnforcementResponse or An
         instance of AsyncLROPoller that returns either LROResponse or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.GroupQuotasEnforcementResponse] or
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.LROResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.GroupQuotasEnforcementResponse] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                management_group_id=management_group_id,
                group_quota_name=group_quota_name,
                resource_provider_name=resource_provider_name,
                location=location,
                location_settings=location_settings,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("GroupQuotasEnforcementResponse", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.GroupQuotasEnforcementResponse].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.GroupQuotasEnforcementResponse](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _update_initial(
        self,
        management_group_id: str,
        group_quota_name: str,
        resource_provider_name: str,
        location: str,
        location_settings: Optional[Union[_models.GroupQuotasEnforcementResponse, IO[bytes]]] = None,
        **kwargs: Any
    ) -> Optional[_models.GroupQuotasEnforcementResponse]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.GroupQuotasEnforcementResponse]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(location_settings, (IOBase, bytes)):
            _content = location_settings
        else:
            if location_settings is not None:
                _json = self._serialize.body(location_settings, "GroupQuotasEnforcementResponse")
            else:
                _json = None

        _request = build_update_request(
            management_group_id=management_group_id,
            group_quota_name=group_quota_name,
            resource_provider_name=resource_provider_name,
            location=location,
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

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("GroupQuotasEnforcementResponse", pipeline_response)

        if response.status_code == 202:
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_update(
        self,
        management_group_id: str,
        group_quota_name: str,
        resource_provider_name: str,
        location: str,
        location_settings: Optional[_models.GroupQuotasEnforcementResponse] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.GroupQuotasEnforcementResponse]:
        """Enables the GroupQuotas enforcement settings for the resource provider and the location
        specified.

        Enables the GroupQuotas enforcement for the resource provider and the location specified. The
        resource provider will start using the group quotas as the overall quota for the subscriptions
        included in the GroupQuota. The subscriptions cannot request quota at subscription level.
        The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the
        GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource -
        provider/location/resource.
        Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To
        disable GroupQuota Enforcement -


        #. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions
        (Check the example - GroupQuotaSubscriptions_Delete).
        #. Ten delete the GroupQuota (Check the example - GroupQuotas_Delete).

        :param management_group_id: Management Group Id. Required.
        :type management_group_id: str
        :param group_quota_name: The GroupQuota name. The name should be unique for the provided
         context tenantId/MgId. Required.
        :type group_quota_name: str
        :param resource_provider_name: The resource provider name, such as - Microsoft.Compute.
         Currently only Microsoft.Compute resource provider supports this API. Required.
        :type resource_provider_name: str
        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_settings: The GroupQuota body details for creation or update of a GroupQuota
         entity. Default value is None.
        :type location_settings: ~azure.mgmt.quota.models.GroupQuotasEnforcementResponse
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either GroupQuotasEnforcementResponse or
         the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.GroupQuotasEnforcementResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        management_group_id: str,
        group_quota_name: str,
        resource_provider_name: str,
        location: str,
        location_settings: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.GroupQuotasEnforcementResponse]:
        """Enables the GroupQuotas enforcement settings for the resource provider and the location
        specified.

        Enables the GroupQuotas enforcement for the resource provider and the location specified. The
        resource provider will start using the group quotas as the overall quota for the subscriptions
        included in the GroupQuota. The subscriptions cannot request quota at subscription level.
        The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the
        GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource -
        provider/location/resource.
        Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To
        disable GroupQuota Enforcement -


        #. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions
        (Check the example - GroupQuotaSubscriptions_Delete).
        #. Ten delete the GroupQuota (Check the example - GroupQuotas_Delete).

        :param management_group_id: Management Group Id. Required.
        :type management_group_id: str
        :param group_quota_name: The GroupQuota name. The name should be unique for the provided
         context tenantId/MgId. Required.
        :type group_quota_name: str
        :param resource_provider_name: The resource provider name, such as - Microsoft.Compute.
         Currently only Microsoft.Compute resource provider supports this API. Required.
        :type resource_provider_name: str
        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_settings: The GroupQuota body details for creation or update of a GroupQuota
         entity. Default value is None.
        :type location_settings: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either GroupQuotasEnforcementResponse or
         the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.GroupQuotasEnforcementResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        management_group_id: str,
        group_quota_name: str,
        resource_provider_name: str,
        location: str,
        location_settings: Optional[Union[_models.GroupQuotasEnforcementResponse, IO[bytes]]] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.GroupQuotasEnforcementResponse]:
        """Enables the GroupQuotas enforcement settings for the resource provider and the location
        specified.

        Enables the GroupQuotas enforcement for the resource provider and the location specified. The
        resource provider will start using the group quotas as the overall quota for the subscriptions
        included in the GroupQuota. The subscriptions cannot request quota at subscription level.
        The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the
        GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource -
        provider/location/resource.
        Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To
        disable GroupQuota Enforcement -


        #. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions
        (Check the example - GroupQuotaSubscriptions_Delete).
        #. Ten delete the GroupQuota (Check the example - GroupQuotas_Delete).

        :param management_group_id: Management Group Id. Required.
        :type management_group_id: str
        :param group_quota_name: The GroupQuota name. The name should be unique for the provided
         context tenantId/MgId. Required.
        :type group_quota_name: str
        :param resource_provider_name: The resource provider name, such as - Microsoft.Compute.
         Currently only Microsoft.Compute resource provider supports this API. Required.
        :type resource_provider_name: str
        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_settings: The GroupQuota body details for creation or update of a GroupQuota
         entity. Is either a GroupQuotasEnforcementResponse type or a IO[bytes] type. Default value is
         None.
        :type location_settings: ~azure.mgmt.quota.models.GroupQuotasEnforcementResponse or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either GroupQuotasEnforcementResponse or
         the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.GroupQuotasEnforcementResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.GroupQuotasEnforcementResponse] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_initial(
                management_group_id=management_group_id,
                group_quota_name=group_quota_name,
                resource_provider_name=resource_provider_name,
                location=location,
                location_settings=location_settings,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("GroupQuotasEnforcementResponse", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.GroupQuotasEnforcementResponse].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.GroupQuotasEnforcementResponse](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @distributed_trace_async
    async def get(
        self, management_group_id: str, group_quota_name: str, resource_provider_name: str, location: str, **kwargs: Any
    ) -> _models.GroupQuotasEnforcementResponse:
        """Gets the GroupQuotas enforcement settings for the resource provider/location.

        Gets the GroupQuotas enforcement settings for the ResourceProvider/location. The locations,
        where GroupQuota enforcement is not enabled will return Not Found.

        :param management_group_id: Management Group Id. Required.
        :type management_group_id: str
        :param group_quota_name: The GroupQuota name. The name should be unique for the provided
         context tenantId/MgId. Required.
        :type group_quota_name: str
        :param resource_provider_name: The resource provider name, such as - Microsoft.Compute.
         Currently only Microsoft.Compute resource provider supports this API. Required.
        :type resource_provider_name: str
        :param location: The name of the Azure region. Required.
        :type location: str
        :return: GroupQuotasEnforcementResponse or the result of cls(response)
        :rtype: ~azure.mgmt.quota.models.GroupQuotasEnforcementResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.GroupQuotasEnforcementResponse] = kwargs.pop("cls", None)

        _request = build_get_request(
            management_group_id=management_group_id,
            group_quota_name=group_quota_name,
            resource_provider_name=resource_provider_name,
            location=location,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("GroupQuotasEnforcementResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(
        self, management_group_id: str, group_quota_name: str, resource_provider_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.GroupQuotasEnforcementResponse"]:
        """Returns a list of the Azure regions settings, where the GroupQuotas enforcement is enabled.

        Returns only the list of the Azure regions settings, where the GroupQuotas enforcement is
        enabled. The locations not included in GroupQuota Enforcement will not be listed, the regions
        in failed status with listed as status Failed.

        :param management_group_id: Management Group Id. Required.
        :type management_group_id: str
        :param group_quota_name: The GroupQuota name. The name should be unique for the provided
         context tenantId/MgId. Required.
        :type group_quota_name: str
        :param resource_provider_name: The resource provider name, such as - Microsoft.Compute.
         Currently only Microsoft.Compute resource provider supports this API. Required.
        :type resource_provider_name: str
        :return: An iterator like instance of either GroupQuotasEnforcementResponse or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.quota.models.GroupQuotasEnforcementResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.GroupQuotasEnforcementListResponse] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    management_group_id=management_group_id,
                    group_quota_name=group_quota_name,
                    resource_provider_name=resource_provider_name,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("GroupQuotasEnforcementListResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

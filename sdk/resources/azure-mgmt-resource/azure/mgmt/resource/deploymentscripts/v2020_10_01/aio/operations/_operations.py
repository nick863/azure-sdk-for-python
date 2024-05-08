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
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, Type, TypeVar, Union, cast, overload
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
from ...operations._operations import (
    build_deployment_scripts_create_request,
    build_deployment_scripts_delete_request,
    build_deployment_scripts_get_logs_default_request,
    build_deployment_scripts_get_logs_request,
    build_deployment_scripts_get_request,
    build_deployment_scripts_list_by_resource_group_request,
    build_deployment_scripts_list_by_subscription_request,
    build_deployment_scripts_update_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class DeploymentScriptsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.resource.deploymentscripts.v2020_10_01.aio.DeploymentScriptsClient`'s
        :attr:`deployment_scripts` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    async def _create_initial(
        self,
        resource_group_name: str,
        script_name: str,
        deployment_script: Union[_models.DeploymentScript, IO[bytes]],
        **kwargs: Any
    ) -> _models.DeploymentScript:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-10-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DeploymentScript] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(deployment_script, (IOBase, bytes)):
            _content = deployment_script
        else:
            _json = self._serialize.body(deployment_script, "DeploymentScript")

        _request = build_deployment_scripts_create_request(
            resource_group_name=resource_group_name,
            script_name=script_name,
            subscription_id=self._config.subscription_id,
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
            error = self._deserialize.failsafe_deserialize(_models.DeploymentScriptsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("DeploymentScript", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("DeploymentScript", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create(
        self,
        resource_group_name: str,
        script_name: str,
        deployment_script: _models.DeploymentScript,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.DeploymentScript]:
        """Creates a deployment script.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param script_name: Name of the deployment script. Required.
        :type script_name: str
        :param deployment_script: Deployment script supplied to the operation. Required.
        :type deployment_script:
         ~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScript
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either DeploymentScript or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScript]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create(
        self,
        resource_group_name: str,
        script_name: str,
        deployment_script: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.DeploymentScript]:
        """Creates a deployment script.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param script_name: Name of the deployment script. Required.
        :type script_name: str
        :param deployment_script: Deployment script supplied to the operation. Required.
        :type deployment_script: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either DeploymentScript or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScript]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create(
        self,
        resource_group_name: str,
        script_name: str,
        deployment_script: Union[_models.DeploymentScript, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.DeploymentScript]:
        """Creates a deployment script.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param script_name: Name of the deployment script. Required.
        :type script_name: str
        :param deployment_script: Deployment script supplied to the operation. Is either a
         DeploymentScript type or a IO[bytes] type. Required.
        :type deployment_script:
         ~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScript or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either DeploymentScript or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScript]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-10-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DeploymentScript] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_initial(
                resource_group_name=resource_group_name,
                script_name=script_name,
                deployment_script=deployment_script,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("DeploymentScript", pipeline_response)
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
            return AsyncLROPoller[_models.DeploymentScript].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.DeploymentScript](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @overload
    async def update(
        self,
        resource_group_name: str,
        script_name: str,
        deployment_script: Optional[_models.DeploymentScriptUpdateParameter] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DeploymentScript:
        """Updates deployment script tags with specified values.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param script_name: Name of the deployment script. Required.
        :type script_name: str
        :param deployment_script: Deployment script resource with the tags to be updated. Default value
         is None.
        :type deployment_script:
         ~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScriptUpdateParameter
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DeploymentScript or the result of cls(response)
        :rtype: ~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScript
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        script_name: str,
        deployment_script: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DeploymentScript:
        """Updates deployment script tags with specified values.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param script_name: Name of the deployment script. Required.
        :type script_name: str
        :param deployment_script: Deployment script resource with the tags to be updated. Default value
         is None.
        :type deployment_script: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DeploymentScript or the result of cls(response)
        :rtype: ~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScript
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        script_name: str,
        deployment_script: Optional[Union[_models.DeploymentScriptUpdateParameter, IO[bytes]]] = None,
        **kwargs: Any
    ) -> _models.DeploymentScript:
        """Updates deployment script tags with specified values.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param script_name: Name of the deployment script. Required.
        :type script_name: str
        :param deployment_script: Deployment script resource with the tags to be updated. Is either a
         DeploymentScriptUpdateParameter type or a IO[bytes] type. Default value is None.
        :type deployment_script:
         ~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScriptUpdateParameter or
         IO[bytes]
        :return: DeploymentScript or the result of cls(response)
        :rtype: ~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScript
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-10-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DeploymentScript] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(deployment_script, (IOBase, bytes)):
            _content = deployment_script
        else:
            if deployment_script is not None:
                _json = self._serialize.body(deployment_script, "DeploymentScriptUpdateParameter")
            else:
                _json = None

        _request = build_deployment_scripts_update_request(
            resource_group_name=resource_group_name,
            script_name=script_name,
            subscription_id=self._config.subscription_id,
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

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DeploymentScriptsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DeploymentScript", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def get(self, resource_group_name: str, script_name: str, **kwargs: Any) -> _models.DeploymentScript:
        """Gets a deployment script with a given name.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param script_name: Name of the deployment script. Required.
        :type script_name: str
        :return: DeploymentScript or the result of cls(response)
        :rtype: ~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScript
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-10-01"))
        cls: ClsType[_models.DeploymentScript] = kwargs.pop("cls", None)

        _request = build_deployment_scripts_get_request(
            resource_group_name=resource_group_name,
            script_name=script_name,
            subscription_id=self._config.subscription_id,
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
            error = self._deserialize.failsafe_deserialize(_models.DeploymentScriptsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DeploymentScript", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, script_name: str, **kwargs: Any
    ) -> None:
        """Deletes a deployment script. When operation completes, status code 200 returned without
        content.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param script_name: Name of the deployment script. Required.
        :type script_name: str
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-10-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_deployment_scripts_delete_request(
            resource_group_name=resource_group_name,
            script_name=script_name,
            subscription_id=self._config.subscription_id,
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
            error = self._deserialize.failsafe_deserialize(_models.DeploymentScriptsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def list_by_subscription(self, **kwargs: Any) -> AsyncIterable["_models.DeploymentScript"]:
        """Lists all deployment scripts for a given subscription.

        :return: An iterator like instance of either DeploymentScript or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScript]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-10-01"))
        cls: ClsType[_models.DeploymentScriptListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_deployment_scripts_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
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
                _next_request_params["api-version"] = self._api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("DeploymentScriptListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.DeploymentScriptsError, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get_logs(self, resource_group_name: str, script_name: str, **kwargs: Any) -> _models.ScriptLogsList:
        """Gets deployment script logs for a given deployment script name.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param script_name: Name of the deployment script. Required.
        :type script_name: str
        :return: ScriptLogsList or the result of cls(response)
        :rtype: ~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.ScriptLogsList
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-10-01"))
        cls: ClsType[_models.ScriptLogsList] = kwargs.pop("cls", None)

        _request = build_deployment_scripts_get_logs_request(
            resource_group_name=resource_group_name,
            script_name=script_name,
            subscription_id=self._config.subscription_id,
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
            error = self._deserialize.failsafe_deserialize(_models.DeploymentScriptsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ScriptLogsList", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def get_logs_default(
        self, resource_group_name: str, script_name: str, tail: Optional[int] = None, **kwargs: Any
    ) -> _models.ScriptLog:
        """Gets deployment script logs for a given deployment script name.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param script_name: Name of the deployment script. Required.
        :type script_name: str
        :param tail: The number of lines to show from the tail of the deployment script log. Valid
         value is a positive number up to 1000. If 'tail' is not provided, all available logs are shown
         up to container instance log capacity of 4mb. Default value is None.
        :type tail: int
        :return: ScriptLog or the result of cls(response)
        :rtype: ~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.ScriptLog
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-10-01"))
        cls: ClsType[_models.ScriptLog] = kwargs.pop("cls", None)

        _request = build_deployment_scripts_get_logs_default_request(
            resource_group_name=resource_group_name,
            script_name=script_name,
            subscription_id=self._config.subscription_id,
            tail=tail,
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
            error = self._deserialize.failsafe_deserialize(_models.DeploymentScriptsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ScriptLog", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self, resource_group_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.DeploymentScript"]:
        """Lists deployments scripts.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :return: An iterator like instance of either DeploymentScript or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.deploymentscripts.v2020_10_01.models.DeploymentScript]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2020-10-01"))
        cls: ClsType[_models.DeploymentScriptListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_deployment_scripts_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
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
                _next_request_params["api-version"] = self._api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("DeploymentScriptListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.DeploymentScriptsError, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

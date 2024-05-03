# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.10.1, generator: @autorest/python@6.13.13)
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

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._synonym_maps_operations import (
    build_create_or_update_request,
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_request,
)
from .._vendor import SearchServiceClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SynonymMapsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.search.documents.indexes.aio.SearchServiceClient`'s
        :attr:`synonym_maps` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_or_update(
        self,
        synonym_map_name: str,
        prefer: Union[str, _models.Enum0],
        synonym_map: _models.SynonymMap,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map or updates a synonym map if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Synonym-Map

        :param synonym_map_name: The name of the synonym map to create or update. Required.
        :type synonym_map_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~azure.search.documents.indexes.models.Enum0
        :param synonym_map: The definition of the synonym map to create or update. Required.
        :type synonym_map: ~azure.search.documents.indexes.models.SynonymMap
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SynonymMap or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        synonym_map_name: str,
        prefer: Union[str, _models.Enum0],
        synonym_map: IO[bytes],
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map or updates a synonym map if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Synonym-Map

        :param synonym_map_name: The name of the synonym map to create or update. Required.
        :type synonym_map_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~azure.search.documents.indexes.models.Enum0
        :param synonym_map: The definition of the synonym map to create or update. Required.
        :type synonym_map: IO[bytes]
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SynonymMap or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        synonym_map_name: str,
        prefer: Union[str, _models.Enum0],
        synonym_map: Union[_models.SynonymMap, IO[bytes]],
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map or updates a synonym map if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Synonym-Map

        :param synonym_map_name: The name of the synonym map to create or update. Required.
        :type synonym_map_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~azure.search.documents.indexes.models.Enum0
        :param synonym_map: The definition of the synonym map to create or update. Is either a
         SynonymMap type or a IO[bytes] type. Required.
        :type synonym_map: ~azure.search.documents.indexes.models.SynonymMap or IO[bytes]
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: SynonymMap or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SynonymMap] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(synonym_map, (IOBase, bytes)):
            _content = synonym_map
        else:
            _json = self._serialize.body(synonym_map, "SynonymMap")

        _request = build_create_or_update_request(
            synonym_map_name=synonym_map_name,
            prefer=prefer,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize("SynonymMap", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("SynonymMap", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        synonym_map_name: str,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a synonym map.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Delete-Synonym-Map

        :param synonym_map_name: The name of the synonym map to delete. Required.
        :type synonym_map_name: str
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        _request = build_delete_request(
            synonym_map_name=synonym_map_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def get(
        self, synonym_map_name: str, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> _models.SynonymMap:
        """Retrieves a synonym map definition.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Get-Synonym-Map

        :param synonym_map_name: The name of the synonym map to retrieve. Required.
        :type synonym_map_name: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: SynonymMap or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.SynonymMap] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        _request = build_get_request(
            synonym_map_name=synonym_map_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SynonymMap", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def list(
        self, select: Optional[str] = None, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> _models.ListSynonymMapsResult:
        """Lists all synonym maps available for a search service.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/List-Synonym-Maps

        :param select: Selects which top-level properties of the synonym maps to retrieve. Specified as
         a comma-separated list of JSON property names, or '*' for all properties. The default is all
         properties. Default value is None.
        :type select: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: ListSynonymMapsResult or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.ListSynonymMapsResult
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ListSynonymMapsResult] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        _request = build_list_request(
            select=select,
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ListSynonymMapsResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create(
        self,
        synonym_map: _models.SynonymMap,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Synonym-Map

        :param synonym_map: The definition of the synonym map to create. Required.
        :type synonym_map: ~azure.search.documents.indexes.models.SynonymMap
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SynonymMap or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        synonym_map: IO[bytes],
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Synonym-Map

        :param synonym_map: The definition of the synonym map to create. Required.
        :type synonym_map: IO[bytes]
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SynonymMap or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        synonym_map: Union[_models.SynonymMap, IO[bytes]],
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Synonym-Map

        :param synonym_map: The definition of the synonym map to create. Is either a SynonymMap type or
         a IO[bytes] type. Required.
        :type synonym_map: ~azure.search.documents.indexes.models.SynonymMap or IO[bytes]
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: SynonymMap or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SynonymMap
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SynonymMap] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(synonym_map, (IOBase, bytes)):
            _content = synonym_map
        else:
            _json = self._serialize.body(synonym_map, "SynonymMap")

        _request = build_create_request(
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SynonymMap", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

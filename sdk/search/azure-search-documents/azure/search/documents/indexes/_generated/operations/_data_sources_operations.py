# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.10.1, generator: @autorest/python@6.13.8)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._serialization import Serializer
from .._vendor import SearchServiceClientMixinABC, _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_create_or_update_request(
    data_source_name: str,
    *,
    prefer: Union[str, _models.Enum0],
    x_ms_client_request_id: Optional[str] = None,
    if_match: Optional[str] = None,
    if_none_match: Optional[str] = None,
    skip_indexer_reset_requirement_for_cache: Optional[bool] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-03-01-Preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/datasources('{dataSourceName}')")
    path_format_arguments = {
        "dataSourceName": _SERIALIZER.url("data_source_name", data_source_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if skip_indexer_reset_requirement_for_cache is not None:
        _params["ignoreResetRequirements"] = _SERIALIZER.query(
            "skip_indexer_reset_requirement_for_cache", skip_indexer_reset_requirement_for_cache, "bool"
        )

    # Construct headers
    if x_ms_client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, "str")
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if if_none_match is not None:
        _headers["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")
    _headers["Prefer"] = _SERIALIZER.header("prefer", prefer, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    data_source_name: str,
    *,
    x_ms_client_request_id: Optional[str] = None,
    if_match: Optional[str] = None,
    if_none_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-03-01-Preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/datasources('{dataSourceName}')")
    path_format_arguments = {
        "dataSourceName": _SERIALIZER.url("data_source_name", data_source_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if x_ms_client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, "str")
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if if_none_match is not None:
        _headers["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    data_source_name: str, *, x_ms_client_request_id: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-03-01-Preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/datasources('{dataSourceName}')")
    path_format_arguments = {
        "dataSourceName": _SERIALIZER.url("data_source_name", data_source_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if x_ms_client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_request(
    *, select: Optional[str] = None, x_ms_client_request_id: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-03-01-Preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/datasources")

    # Construct parameters
    if select is not None:
        _params["$select"] = _SERIALIZER.query("select", select, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if x_ms_client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_request(*, x_ms_client_request_id: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-03-01-Preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/datasources")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if x_ms_client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class DataSourcesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.search.documents.indexes.SearchServiceClient`'s
        :attr:`data_sources` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def create_or_update(
        self,
        data_source_name: str,
        prefer: Union[str, _models.Enum0],
        data_source: _models.SearchIndexerDataSource,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        skip_indexer_reset_requirement_for_cache: Optional[bool] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchIndexerDataSource:
        """Creates a new datasource or updates a datasource if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Data-Source

        :param data_source_name: The name of the datasource to create or update. Required.
        :type data_source_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~azure.search.documents.indexes.models.Enum0
        :param data_source: The definition of the datasource to create or update. Required.
        :type data_source: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param skip_indexer_reset_requirement_for_cache: Ignores cache reset requirements. Default
         value is None.
        :type skip_indexer_reset_requirement_for_cache: bool
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SearchIndexerDataSource or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        data_source_name: str,
        prefer: Union[str, _models.Enum0],
        data_source: IO[bytes],
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        skip_indexer_reset_requirement_for_cache: Optional[bool] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchIndexerDataSource:
        """Creates a new datasource or updates a datasource if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Data-Source

        :param data_source_name: The name of the datasource to create or update. Required.
        :type data_source_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~azure.search.documents.indexes.models.Enum0
        :param data_source: The definition of the datasource to create or update. Required.
        :type data_source: IO[bytes]
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param skip_indexer_reset_requirement_for_cache: Ignores cache reset requirements. Default
         value is None.
        :type skip_indexer_reset_requirement_for_cache: bool
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SearchIndexerDataSource or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        data_source_name: str,
        prefer: Union[str, _models.Enum0],
        data_source: Union[_models.SearchIndexerDataSource, IO[bytes]],
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        skip_indexer_reset_requirement_for_cache: Optional[bool] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SearchIndexerDataSource:
        """Creates a new datasource or updates a datasource if it already exists.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Update-Data-Source

        :param data_source_name: The name of the datasource to create or update. Required.
        :type data_source_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~azure.search.documents.indexes.models.Enum0
        :param data_source: The definition of the datasource to create or update. Is either a
         SearchIndexerDataSource type or a IO[bytes] type. Required.
        :type data_source: ~azure.search.documents.indexes.models.SearchIndexerDataSource or IO[bytes]
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param skip_indexer_reset_requirement_for_cache: Ignores cache reset requirements. Default
         value is None.
        :type skip_indexer_reset_requirement_for_cache: bool
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: SearchIndexerDataSource or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
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
        cls: ClsType[_models.SearchIndexerDataSource] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(data_source, (IOBase, bytes)):
            _content = data_source
        else:
            _json = self._serialize.body(data_source, "SearchIndexerDataSource")

        _request = build_create_or_update_request(
            data_source_name=data_source_name,
            prefer=prefer,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            skip_indexer_reset_requirement_for_cache=skip_indexer_reset_requirement_for_cache,
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize("SearchIndexerDataSource", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("SearchIndexerDataSource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self,
        data_source_name: str,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a datasource.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Delete-Data-Source

        :param data_source_name: The name of the datasource to delete. Required.
        :type data_source_name: str
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
        cls: ClsType[None] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        _request = build_delete_request(
            data_source_name=data_source_name,
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def get(
        self, data_source_name: str, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> _models.SearchIndexerDataSource:
        """Retrieves a datasource definition.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Get-Data-Source

        :param data_source_name: The name of the datasource to retrieve. Required.
        :type data_source_name: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: SearchIndexerDataSource or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndexerDataSource
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
        cls: ClsType[_models.SearchIndexerDataSource] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        _request = build_get_request(
            data_source_name=data_source_name,
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SearchIndexerDataSource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(
        self, select: Optional[str] = None, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> _models.ListDataSourcesResult:
        """Lists all datasources available for a search service.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/List-Data-Sources

        :param select: Selects which top-level properties of the data sources to retrieve. Specified as
         a comma-separated list of JSON property names, or '*' for all properties. The default is all
         properties. Default value is None.
        :type select: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: ListDataSourcesResult or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.ListDataSourcesResult
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
        cls: ClsType[_models.ListDataSourcesResult] = kwargs.pop("cls", None)

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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ListDataSourcesResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create(
        self,
        data_source: _models.SearchIndexerDataSource,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchIndexerDataSource:
        """Creates a new datasource.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Data-Source

        :param data_source: The definition of the datasource to create. Required.
        :type data_source: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SearchIndexerDataSource or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self,
        data_source: IO[bytes],
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SearchIndexerDataSource:
        """Creates a new datasource.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Data-Source

        :param data_source: The definition of the datasource to create. Required.
        :type data_source: IO[bytes]
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SearchIndexerDataSource or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create(
        self,
        data_source: Union[_models.SearchIndexerDataSource, IO[bytes]],
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SearchIndexerDataSource:
        """Creates a new datasource.

        .. seealso::
           - https://docs.microsoft.com/rest/api/searchservice/Create-Data-Source

        :param data_source: The definition of the datasource to create. Is either a
         SearchIndexerDataSource type or a IO[bytes] type. Required.
        :type data_source: ~azure.search.documents.indexes.models.SearchIndexerDataSource or IO[bytes]
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: SearchIndexerDataSource or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchIndexerDataSource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
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
        cls: ClsType[_models.SearchIndexerDataSource] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(data_source, (IOBase, bytes)):
            _content = data_source
        else:
            _json = self._serialize.body(data_source, "SearchIndexerDataSource")

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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SearchIndexerDataSource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

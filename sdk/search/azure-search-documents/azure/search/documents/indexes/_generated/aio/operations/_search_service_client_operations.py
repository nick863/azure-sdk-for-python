# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.10.1, generator: @autorest/python@6.13.13)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, Type, TypeVar

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
from ...operations._search_service_client_operations import build_get_service_statistics_request
from .._vendor import SearchServiceClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SearchServiceClientOperationsMixin(SearchServiceClientMixinABC):

    @distributed_trace_async
    async def get_service_statistics(
        self, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> _models.SearchServiceStatistics:
        """Gets service level statistics for a search service.

        :param request_options: Parameter group. Default value is None.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :return: SearchServiceStatistics or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.SearchServiceStatistics
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
        cls: ClsType[_models.SearchServiceStatistics] = kwargs.pop("cls", None)

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        _request = build_get_service_statistics_request(
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
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SearchServiceStatistics", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

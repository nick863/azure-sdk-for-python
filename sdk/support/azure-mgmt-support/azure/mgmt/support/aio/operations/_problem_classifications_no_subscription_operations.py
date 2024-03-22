# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
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
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._problem_classifications_no_subscription_operations import build_classify_problems_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ProblemClassificationsNoSubscriptionOperations:  # pylint: disable=name-too-long
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.support.aio.MicrosoftSupport`'s
        :attr:`problem_classifications_no_subscription` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def classify_problems(
        self,
        problem_service_name: str,
        problem_classifications_classification_input: _models.ProblemClassificationsClassificationInput,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ProblemClassificationsClassificationOutput:
        """Classify the right problem classifications (categories) available for a specific Azure service.

        :param problem_service_name: Name of the Azure service for which the problem classifications
         need to be retrieved. Required.
        :type problem_service_name: str
        :param problem_classifications_classification_input: Input to check. Required.
        :type problem_classifications_classification_input:
         ~azure.mgmt.support.models.ProblemClassificationsClassificationInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ProblemClassificationsClassificationOutput or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.ProblemClassificationsClassificationOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def classify_problems(
        self,
        problem_service_name: str,
        problem_classifications_classification_input: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ProblemClassificationsClassificationOutput:
        """Classify the right problem classifications (categories) available for a specific Azure service.

        :param problem_service_name: Name of the Azure service for which the problem classifications
         need to be retrieved. Required.
        :type problem_service_name: str
        :param problem_classifications_classification_input: Input to check. Required.
        :type problem_classifications_classification_input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ProblemClassificationsClassificationOutput or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.ProblemClassificationsClassificationOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def classify_problems(
        self,
        problem_service_name: str,
        problem_classifications_classification_input: Union[
            _models.ProblemClassificationsClassificationInput, IO[bytes]
        ],
        **kwargs: Any
    ) -> _models.ProblemClassificationsClassificationOutput:
        """Classify the right problem classifications (categories) available for a specific Azure service.

        :param problem_service_name: Name of the Azure service for which the problem classifications
         need to be retrieved. Required.
        :type problem_service_name: str
        :param problem_classifications_classification_input: Input to check. Is either a
         ProblemClassificationsClassificationInput type or a IO[bytes] type. Required.
        :type problem_classifications_classification_input:
         ~azure.mgmt.support.models.ProblemClassificationsClassificationInput or IO[bytes]
        :return: ProblemClassificationsClassificationOutput or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.ProblemClassificationsClassificationOutput
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
        cls: ClsType[_models.ProblemClassificationsClassificationOutput] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(problem_classifications_classification_input, (IOBase, bytes)):
            _content = problem_classifications_classification_input
        else:
            _json = self._serialize.body(
                problem_classifications_classification_input, "ProblemClassificationsClassificationInput"
            )

        _request = build_classify_problems_request(
            problem_service_name=problem_service_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ProblemClassificationsClassificationOutput", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

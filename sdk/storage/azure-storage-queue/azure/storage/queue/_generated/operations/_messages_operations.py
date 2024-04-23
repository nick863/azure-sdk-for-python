# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Literal, Optional, TypeVar

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
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_dequeue_request(
    url: str,
    *,
    number_of_messages: Optional[int] = None,
    visibilitytimeout: Optional[int] = None,
    timeout: Optional[int] = None,
    request_id_parameter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    version: Literal["2018-03-28"] = kwargs.pop("version", _headers.pop("x-ms-version", "2018-03-28"))
    accept = _headers.pop("Accept", "application/xml")

    # Construct URL
    _url = kwargs.pop("template_url", "{url}/messages")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str", skip_quote=True),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if number_of_messages is not None:
        _params["numofmessages"] = _SERIALIZER.query("number_of_messages", number_of_messages, "int", minimum=1)
    if visibilitytimeout is not None:
        _params["visibilitytimeout"] = _SERIALIZER.query(
            "visibilitytimeout", visibilitytimeout, "int", maximum=604800, minimum=0
        )
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int", minimum=0)

    # Construct headers
    _headers["x-ms-version"] = _SERIALIZER.header("version", version, "str")
    if request_id_parameter is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("request_id_parameter", request_id_parameter, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_clear_request(
    url: str, *, timeout: Optional[int] = None, request_id_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    version: Literal["2018-03-28"] = kwargs.pop("version", _headers.pop("x-ms-version", "2018-03-28"))
    accept = _headers.pop("Accept", "application/xml")

    # Construct URL
    _url = kwargs.pop("template_url", "{url}/messages")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str", skip_quote=True),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int", minimum=0)

    # Construct headers
    _headers["x-ms-version"] = _SERIALIZER.header("version", version, "str")
    if request_id_parameter is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("request_id_parameter", request_id_parameter, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_enqueue_request(
    url: str,
    *,
    content: Any,
    visibilitytimeout: Optional[int] = None,
    message_time_to_live: Optional[int] = None,
    timeout: Optional[int] = None,
    request_id_parameter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    version: Literal["2018-03-28"] = kwargs.pop("version", _headers.pop("x-ms-version", "2018-03-28"))
    accept = _headers.pop("Accept", "application/xml")

    # Construct URL
    _url = kwargs.pop("template_url", "{url}/messages")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str", skip_quote=True),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if visibilitytimeout is not None:
        _params["visibilitytimeout"] = _SERIALIZER.query(
            "visibilitytimeout", visibilitytimeout, "int", maximum=604800, minimum=0
        )
    if message_time_to_live is not None:
        _params["messagettl"] = _SERIALIZER.query("message_time_to_live", message_time_to_live, "int", minimum=-1)
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int", minimum=0)

    # Construct headers
    _headers["x-ms-version"] = _SERIALIZER.header("version", version, "str")
    if request_id_parameter is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("request_id_parameter", request_id_parameter, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, content=content, **kwargs)


def build_peek_request(
    url: str,
    *,
    number_of_messages: Optional[int] = None,
    timeout: Optional[int] = None,
    request_id_parameter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    peekonly: Literal["true"] = kwargs.pop("peekonly", _params.pop("peekonly", "true"))
    version: Literal["2018-03-28"] = kwargs.pop("version", _headers.pop("x-ms-version", "2018-03-28"))
    accept = _headers.pop("Accept", "application/xml")

    # Construct URL
    _url = kwargs.pop("template_url", "{url}/messages")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str", skip_quote=True),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["peekonly"] = _SERIALIZER.query("peekonly", peekonly, "str")
    if number_of_messages is not None:
        _params["numofmessages"] = _SERIALIZER.query("number_of_messages", number_of_messages, "int", minimum=1)
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int", minimum=0)

    # Construct headers
    _headers["x-ms-version"] = _SERIALIZER.header("version", version, "str")
    if request_id_parameter is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("request_id_parameter", request_id_parameter, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class MessagesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.queue.AzureQueueStorage`'s
        :attr:`messages` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def dequeue(
        self,
        number_of_messages: Optional[int] = None,
        visibilitytimeout: Optional[int] = None,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> List[_models.DequeuedMessageItem]:
        """The Dequeue operation retrieves one or more messages from the front of the queue.

        :param number_of_messages: Optional. A nonzero integer value that specifies the number of
         messages to retrieve from the queue, up to a maximum of 32. If fewer are visible, the visible
         messages are returned. By default, a single message is retrieved from the queue with this
         operation. Default value is None.
        :type number_of_messages: int
        :param visibilitytimeout: Optional. Specifies the new visibility timeout value, in seconds,
         relative to server time. The default value is 30 seconds. A specified value must be larger than
         or equal to 1 second, and cannot be larger than 7 days, or larger than 2 hours on REST protocol
         versions prior to version 2011-08-18. The visibility timeout of a message can be set to a value
         later than the expiry time. Default value is None.
        :type visibilitytimeout: int
        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :return: list of DequeuedMessageItem or the result of cls(response)
        :rtype: list[~azure.storage.queue.models.DequeuedMessageItem]
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
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.DequeuedMessageItem]] = kwargs.pop("cls", None)

        _request = build_dequeue_request(
            url=self._config.url,
            number_of_messages=number_of_messages,
            visibilitytimeout=visibilitytimeout,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            version=self._config.version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        deserialized = self._deserialize("[DequeuedMessageItem]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def clear(  # pylint: disable=inconsistent-return-statements
        self, timeout: Optional[int] = None, request_id_parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """The Clear operation deletes all messages from the specified queue.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
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
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_clear_request(
            url=self._config.url,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            version=self._config.version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace
    def enqueue(
        self,
        queue_message: _models.QueueMessage,
        visibilitytimeout: Optional[int] = None,
        message_time_to_live: Optional[int] = None,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> List[_models.EnqueuedMessage]:
        """The Enqueue operation adds a new message to the back of the message queue. A visibility timeout
        can also be specified to make the message invisible until the visibility timeout expires. A
        message must be in a format that can be included in an XML request with UTF-8 encoding. The
        encoded message can be up to 64 KB in size for versions 2011-08-18 and newer, or 8 KB in size
        for previous versions.

        :param queue_message: A Message object which can be stored in a Queue. Required.
        :type queue_message: ~azure.storage.queue.models.QueueMessage
        :param visibilitytimeout: Optional. If specified, the request must be made using an
         x-ms-version of 2011-08-18 or later. If not specified, the default value is 0. Specifies the
         new visibility timeout value, in seconds, relative to server time. The new value must be larger
         than or equal to 0, and cannot be larger than 7 days. The visibility timeout of a message
         cannot be set to a value later than the expiry time. visibilitytimeout should be set to a value
         smaller than the time-to-live value. Default value is None.
        :type visibilitytimeout: int
        :param message_time_to_live: Optional. Specifies the time-to-live interval for the message, in
         seconds. Prior to version 2017-07-29, the maximum time-to-live allowed is 7 days. For version
         2017-07-29 or later, the maximum time-to-live can be any positive number, as well as -1
         indicating that the message does not expire. If this parameter is omitted, the default
         time-to-live is 7 days. Default value is None.
        :type message_time_to_live: int
        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :return: list of EnqueuedMessage or the result of cls(response)
        :rtype: list[~azure.storage.queue.models.EnqueuedMessage]
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
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/xml"))
        cls: ClsType[List[_models.EnqueuedMessage]] = kwargs.pop("cls", None)

        _content = self._serialize.body(queue_message, "QueueMessage", is_xml=True)

        _request = build_enqueue_request(
            url=self._config.url,
            visibilitytimeout=visibilitytimeout,
            message_time_to_live=message_time_to_live,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            content_type=content_type,
            version=self._config.version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        deserialized = self._deserialize("[EnqueuedMessage]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def peek(
        self,
        number_of_messages: Optional[int] = None,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> List[_models.PeekedMessageItem]:
        """The Peek operation retrieves one or more messages from the front of the queue, but does not
        alter the visibility of the message.

        :param number_of_messages: Optional. A nonzero integer value that specifies the number of
         messages to retrieve from the queue, up to a maximum of 32. If fewer are visible, the visible
         messages are returned. By default, a single message is retrieved from the queue with this
         operation. Default value is None.
        :type number_of_messages: int
        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :return: list of PeekedMessageItem or the result of cls(response)
        :rtype: list[~azure.storage.queue.models.PeekedMessageItem]
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

        peekonly: Literal["true"] = kwargs.pop("peekonly", _params.pop("peekonly", "true"))
        cls: ClsType[List[_models.PeekedMessageItem]] = kwargs.pop("cls", None)

        _request = build_peek_request(
            url=self._config.url,
            number_of_messages=number_of_messages,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            peekonly=peekonly,
            version=self._config.version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        deserialized = self._deserialize("[PeekedMessageItem]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore
